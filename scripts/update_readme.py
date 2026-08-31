import os
import re
import pandas as pd
from datetime import datetime

DATA_DIR = "data"
README_PATH = "README.md"

def format_value(val):
    """Convierte el valor numérico (ej. 185000000) a formato moneda (ej. €185.0M)"""
    try:
        val = float(val)
        if pd.isna(val) or val == 0:
            return "€0"
        if val >= 1_000_000:
            return f"€{val / 1_000_000:.1f}M"
        elif val >= 1_000:
            return f"€{val / 1_000:.0f}K"
        else:
            return f"€{int(val)}"
    except:
        return "N/A"

def generate_season_markdown(csv_path, game_name, is_latest=False):
    """Genera el bloque Markdown del Top 10 para una edición específica."""
    df = pd.read_csv(csv_path)
    
    # Ordenar por Overall (descendente) y luego por Valor (descendente) en caso de empate
    top_10 = df.sort_values(by=["overall", "value_eur"], ascending=[False, False]).head(10)
    
    open_attr = " open" if is_latest else ""
    
    md = [
        f"<details{open_attr}>",
        f"<summary><b>⚽ {game_name}</b></summary>",
        "",
        "#### 👤 Top 10 Players",
        "",
        "| Player | Club | Position | Overall | Value |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]
    
    for _, row in top_10.iterrows():
        name = row.get("short_name", "N/A")
        club = row.get("club_name", "N/A")
        pos = row.get("positions", "N/A")
        ovr = row.get("overall", 0)
        val = format_value(row.get("value_eur", 0))
        
        md.append(f"| **{name}** | {club} | {pos} | {int(ovr)} | {val} |")
        
    md.extend(["", "</details>"])
    return "\n".join(md)

def update_readme():
    if not os.path.exists(DATA_DIR):
        print(f"Directory '{DATA_DIR}' not found.")
        return

    # Buscar carpetas de años (ej: '2024', '2025')
    seasons = [s for s in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, s)) and s.isdigit()]
    if not seasons:
        print("No season directories found in data/.")
        return

    # Ordenar de más reciente a más antiguo
    seasons.sort(reverse=True)
    summary_blocks = []
    
    for idx, year in enumerate(seasons):
        season_dir = os.path.join(DATA_DIR, year)
        # Buscar el archivo CSV de ese año
        csv_files = [f for f in os.listdir(season_dir) if f.endswith(".csv")]
        
        if not csv_files:
            continue
            
        csv_path = os.path.join(season_dir, csv_files[0])
        game_name = f"EA FC {year[-2:]}" if int(year) >= 2024 else f"FIFA {year[-2:]}"
        
        block = generate_season_markdown(csv_path, game_name, is_latest=(idx == 0))
        summary_blocks.append(block)

    full_summary_md = "\n\n".join(summary_blocks)

    if not os.path.exists(README_PATH):
        print(f"'{README_PATH}' not found.")
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Inyectar el bloque de temporadas
    summary_pattern = r"(<!-- SEASONS_SUMMARY_START -->)(.*?)(<!-- SEASONS_SUMMARY_END -->)"
    if re.search(summary_pattern, readme_content, flags=re.DOTALL):
        readme_content = re.sub(summary_pattern, f"\\1\n{full_summary_md}\n\\3", readme_content, flags=re.DOTALL)

    # Actualizar la fecha del "Last checked"
    today_str = datetime.now().strftime("%Y-%m-%d")
    checked_pattern = r"(<!-- LAST_CHECKED_START -->)(.*?)(<!-- LAST_CHECKED_END -->)"
    if re.search(checked_pattern, readme_content, flags=re.DOTALL):
        readme_content = re.sub(checked_pattern, f"\\1Last checked: {today_str}\\3", readme_content, flags=re.DOTALL)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme_content)

    print(f"README.md updated successfully with date {today_str}!")

if __name__ == "__main__":
    update_readme()
