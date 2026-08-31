import time
import re
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Headers to simulate a real browser request and avoid bot protections
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

BASE_URL = "https://sofifa.com"

# --- VERSION CODES ---
# Se mantiene únicamente EA FC 26 para que el scraper solo procese este juego
VERSION_CODES = {
    "EA FC 26": "260046"
}

# --- COLUMNS TO EXTRACT ---
SOFIFA_COLUMNS = [
    "pi", "ae", "hi", "wi", "pf", "oa", "pt", "vl", "wg", "cr", "fi", "he", "sh", "vo",
    "dr", "cu", "fr", "lo", "bl", "ac", "sp", "ag", "re", "ba", "so", "ju",
    "st", "sr", "ln", "ar", "in", "po", "vi", "pe", "cm", "ma", "sa", "sl",
    "gd", "gh", "gc", "gp", "gr", "pac", "sho", "pas", "dri", "def", "phy", "ps1", "ps2"
]

def parse_money(val_str: str) -> int:
    if not val_str or val_str == "€0" or val_str == "":
        return 0
    val_str = val_str.replace("€", "").strip()
    if "M" in val_str:
        return int(float(val_str.replace("M", "")) * 1_000_000)
    elif "K" in val_str:
        return int(float(val_str.replace("K", "")) * 1_000)
    try:
        return int(val_str)
    except ValueError:
        return 0

def extract_number(text: str) -> int:
    if not text:
        return None
    match = re.search(r'\d+', text)
    return int(match.group()) if match else None

def translate_foot(text: str) -> str:
    if not text: return None
    text = text.lower().strip()
    if "izq" in text or "left" in text: return "Left"
    if "der" in text or "right" in text: return "Right"
    return text

def build_sofifa_url(offset: int, version_code: str) -> str:
    base = f"{BASE_URL}/players?col=oa&sort=desc&offset={offset}&r={version_code}&set=true&hl=en-US"
    col_params = "&".join([f"showCol%5B%5D={col}" for col in SOFIFA_COLUMNS])
    return f"{base}&{col_params}"

def build_short_name(alias_name: str, long_name: str) -> str:
    """Intelligent heuristic to format short names across different cultures."""
    alias_lower = alias_name.lower()
    particles = {
        "de", "van", "von", "da", "das", "dos", "del", "la", "le", "di", 
        "mac", "mc", "ter", "al", "el", "bin", "ibn", "abu", "der", "den", 
        "ten", "zu", "st", "st.", "san", "santa", "do", "du"
    }
    
    name_parts = long_name.split()
    if len(name_parts) <= 1:
        return long_name
        
    first_initial = f"{name_parts[0][0]}."
    
    # 1. Agrupar partículas con los apellidos correspondientes
    grouped_parts = []
    i = 0
    while i < len(name_parts):
        part = name_parts[i]
        if part.lower() in particles and i + 1 < len(name_parts):
            # Verifica si hay partículas dobles (ej. "van" + "de" + "Beek")
            if name_parts[i+1].lower() in particles and i + 2 < len(name_parts):
                grouped_parts.append(f"{part} {name_parts[i+1]} {name_parts[i+2]}")
                i += 3
            else:
                grouped_parts.append(f"{part} {name_parts[i+1]}")
                i += 2
        else:
            grouped_parts.append(part)
            i += 1

    # 2. Heurística de selección
    if len(grouped_parts) == 2:
        # Caso estándar (Nombre + Apellido)
        surname = grouped_parts[1]
    elif len(grouped_parts) > 2:
        last_word = grouped_parts[-1].lower()
        last_word_clean = last_word.replace(".", "").replace(",", "")
        
        # Si la última palabra está en el alias o es un sufijo
        if last_word_clean in alias_lower or last_word_clean in ["jr", "junior"]:
            surname = grouped_parts[-1]
        else:
            # Convención hispana por defecto
            surname = grouped_parts[1]
    else:
        surname = alias_name
        
    return f"{first_initial} {surname}"

def get_players_page(offset: int = 0, version_code: str = "") -> list[dict]:
    url = build_sofifa_url(offset, version_code)
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=HEADERS, timeout=15)
            if response.status_code == 200:
                break
            print(f"[!] Error fetching offset {offset}. Status: {response.status_code}. Retrying...")
            time.sleep(2)
        except requests.RequestException as e:
            print(f"[!] Request Exception at offset {offset}: {e}. Retrying...")
            time.sleep(2)
    else:
        print(f"[-] Max retries reached for offset {offset}. Skipping.")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.select("tbody tr")
    players = []

    for row in rows:
        link_elem = row.select_one("td a[href^='/player/']")
        if not link_elem: continue
        
        alias_name = link_elem.text.strip()
        long_name = link_elem.get("data-tippy-content", alias_name).strip()
        
        # Generar nombre formateado inteligentemente
        short_name = build_short_name(alias_name, long_name)
        
        id_elem = row.select_one("td[data-col='pi']")
        sofifa_id = int(id_elem.text.strip()) if id_elem else None

        nation_elem = row.select_one("a[href*='/players?na='] img")
        nation_name = nation_elem.get("title") if nation_elem else None
        
        club_elem = row.select_one("a[href*='/team/']")
        club_name = club_elem.text.strip() if club_elem else None

        pos_tags = row.select("a[href*='pn='] span.pos")
        positions = [p.text.strip() for p in pos_tags if p.text.strip()]

        def get_val(col_code, is_money=False, is_text=False, is_dirty_number=False):
            cell = row.select_one(f"td[data-col='{col_code}']")
            if not cell: return None
            
            if col_code in ["ps1", "ps2"]:
                spans = cell.find_all("span", class_="inline-block")
                if spans:
                    return ", ".join([span.text.strip() for span in spans if span.text.strip()])
                else:
                     return None
            
            val_text = cell.select_one("em").text.strip() if cell.select_one("em") else cell.text.strip()
            
            if is_money: return parse_money(val_text)
            if is_text: return val_text
            if is_dirty_number: return extract_number(val_text)
            try: return int(val_text)
            except ValueError: return None

        player_data = {
            "sofifa_id": sofifa_id,
            "alias": alias_name,
            "short_name": short_name,
            "long_name": long_name,
            "player_url": f"{BASE_URL}{link_elem['href']}",
            "nationality": nation_name,
            "club_name": club_name,
            "positions": ", ".join(positions),
            
            "age": get_val("ae"),
            "height_cm": get_val("hi", is_dirty_number=True),
            "weight_kg": get_val("wi", is_dirty_number=True),
            "preferred_foot": translate_foot(get_val("pf", is_text=True)),
            
            "overall": get_val("oa"),
            "potential": get_val("pt"),
            "value_eur": get_val("vl", is_money=True),
            "wage_eur": get_val("wg", is_money=True),
            
            "pace": get_val("pac"),
            "shooting": get_val("sho"),
            "passing": get_val("pas"),
            "dribbling": get_val("dri"),
            "defending": get_val("def"),
            "physical": get_val("phy"),
            
            "crossing": get_val("cr"),
            "finishing": get_val("fi"),
            "heading_accuracy": get_val("he"),
            "short_passing": get_val("sh"),
            "volleys": get_val("vo"),
            "dribbling_stat": get_val("dr"),
            "curve": get_val("cu"),
            "fk_accuracy": get_val("fr"),
            "long_passing": get_val("lo"),
            "ball_control": get_val("bl"),
            "acceleration": get_val("ac"),
            "sprint_speed": get_val("sp"),
            "agility": get_val("ag"),
            "reactions": get_val("re"),
            "balance": get_val("ba"),
            "shot_power": get_val("so"),
            "jumping": get_val("ju"),
            "stamina": get_val("st"),
            "strength": get_val("sr"),
            "long_shots": get_val("ln"),
            "aggression": get_val("ar"),
            "interceptions": get_val("in"),
            "positioning": get_val("po"),
            "vision": get_val("vi"),
            "penalties": get_val("pe"),
            "composure": get_val("cm"),
            
            "defensive_awareness": get_val("ma"),
            "standing_tackle": get_val("sa"),
            "sliding_tackle": get_val("sl"),
            "gk_diving": get_val("gd"),
            "gk_handling": get_val("gh"),
            "gk_kicking": get_val("gc"),
            "gk_positioning": get_val("gp"),
            "gk_reflexes": get_val("gr"),
            
            "playstyles": get_val("ps1", is_text=True),
            "playstyles_plus": get_val("ps2", is_text=True)
        }

        players.append(player_data)

    return players

# ==========================================
# Main Execution Block
# ==========================================
if __name__ == "__main__":
    
    TEST_MODE = False
    MAX_TEST_PAGES = 1 
    
    # Aseguramos que existe la carpeta base de datos
    os.makedirs("data", exist_ok=True)
    
    # Identificamos cuál es el último juego de la lista
    latest_game = list(VERSION_CODES.keys())[0]
    
    for game_name, version_code in VERSION_CODES.items():
            
        friendly_name = game_name.replace(' ', '_').lower()
        file_prefix = "test_" if TEST_MODE else ""
        OUTPUT_FILE = os.path.join("data", f"{file_prefix}dataset_{friendly_name}.csv")
    
        is_latest = (game_name == latest_game)
    
        print("\n" + "="*60)
        print(f"[*] Starting EXTRACTION for {game_name} (Roster: {version_code})")
        print(f"[*] Destination: {OUTPUT_FILE}")
        print("="*60)
        
        # --- LÓGICA DE ACTUALIZACIÓN / SKIP ---
        scraped_ids = set()
        
        if os.path.exists(OUTPUT_FILE):
            if not is_latest and not TEST_MODE:
                print(f"[+] Historical data for {game_name} already exists.")
                print(f"[+] Skipping to save time and resources.\n")
                continue
            else:
                print(f"[*] Active game detected. Removing old dataset to pull fresh updates.")
                os.remove(OUTPUT_FILE)
        else:
            print("[+] Starting a fresh dataset.")
            
        full_dataset = []
        max_offset = (MAX_TEST_PAGES * 60) if TEST_MODE else 18500 
        
        for offset in range(0, max_offset, 60):
            print(f"[>] Fetching page offset {offset} for {game_name}...")
            players_page = get_players_page(offset=offset, version_code=version_code)
            
            if not players_page:
                 print(f"[!] No more players found. Ending extraction for {game_name}.")
                 break
                
            new_players = []
            for player in players_page:
                # Omitimos duplicados si los hubiera
                if player["sofifa_id"] in scraped_ids:
                    continue
                
                player["game_version"] = game_name
                new_players.append(player)
                scraped_ids.add(player["sofifa_id"])
                
            if not new_players:
                 time.sleep(1.0)
                 continue
                 
            # Guardar el lote en el CSV
            df_page = pd.DataFrame(new_players)
            cols = ['game_version'] + [c for c in df_page.columns if c != 'game_version']
            df_page = df_page[cols]
            
            if not os.path.exists(OUTPUT_FILE):
                 df_page.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
            else:
                 df_page.to_csv(OUTPUT_FILE, mode='a', header=False, index=False, encoding="utf-8-sig")

            full_dataset.extend(new_players)
            time.sleep(1.5) 
                
        print(f"\n[✓] DONE! {len(full_dataset)} players exported to {OUTPUT_FILE}")
