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
    
    # Ordenar por Overall (descendente) y luego por Potential (descendente) en caso de empate
    top_10 = df.sort_values(by=["overall", "potential"], ascending=[False, False]).head(10)
    
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
        # Usamos el alias para que salga limpio
        name = row.get("alias", "N/A")
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

    # Buscar archivos CSV directamente en la carpeta data/
    csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]
    
    if not csv_files:
        print("No CSV files found in data/.")
        return

    # Ordenar alfabéticamente inverso (dataset_ea_fc_26.csv irá antes que el 25)
    csv_files.sort(reverse=True)
    summary_blocks = []
    
    for idx, filename in enumerate(csv_files):
        csv_path = os.path.join(DATA_DIR, filename)
        
        # Extraer el año del nombre del archivo (ej: de "dataset_ea_fc_26.csv" saca "26")
        match = re.search(r'_(\d{2})\.csv', filename)
        if match:
            year_suffix = match.group(1)
            game_name = f"EA FC {year_suffix}" if int(year_suffix) >= 24 else f"FIFA {year_suffix}"
        else:
            game_name = filename.replace('.csv', '') # Fallback por si el nombre es raro
            
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
