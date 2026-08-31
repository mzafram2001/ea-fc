# ⚽ ea-fc

![Status](https://img.shields.io/badge/Status-Available-green)
![License](https://img.shields.io/badge/License-MIT-blue)
![Format](https://img.shields.io/badge/Format-CSV-orange)
![Stack](https://img.shields.io/badge/Stack-Python-yellow)
![Last updated](https://img.shields.io/github/last-commit/mzafram2001/ea-fc?label=Last%20update)

An open-source historical dataset of EA FC (formerly FIFA) men's football players.

This repository provides clean, standardized, and structured CSV data containing in-depth player statistics, potentials, market values, and demographics for analytical purposes, machine learning models, and career mode scouting.

---

## 📂 Repository structure

```text
ea-fc/
│
├── .github/
│   ├── workflows/
│   │   └── get_data.yml
│   └── FUNDING.yml
│ 
├── data/
│   ├── 2024/
│   │   └── dataset_ea_fc_24.csv
│   ├── 2025/
│   │   └── dataset_ea_fc_25.csv
│   └── 2026/
│       └── dataset_ea_fc_26.csv
│
├── scripts/
│   ├── get_data.py
│   └── update_readme.py
│
├── AUTHORS.md
├── LICENSE.md
└── README.md
```

---

## 📊 Data schema

Each version file (`data/{year}/dataset_ea_fc_{year}.csv`) follows a standardized flat CSV schema, enabling easy cross-year analysis. The schema contains over 50 columns divided into **Demographics**, **Core Stats**, **Face Stats**, and **In-Game Attributes**.

| Attribute | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `game_version` | `String` | The game edition the data belongs to | `"EA FC 24"` |
| `sofifa_id` | `Integer` | Unique internal identifier (matches EA ID) | `231747` |
| `short_name` | `String` | Standardized initial and surname | `"K. Mbappé"` |
| `long_name` | `String` | Full name of the player | `"Kylian Mbappé Lottin"` |
| `club_name` | `String` | Current domestic club | `"Real Madrid"` |
| `positions` | `String` | Playable positions separated by commas | `"ST, LW"` |
| `age` | `Integer` | Player age at the time of the roster update | `24` |
| `overall` | `Integer` | Overall rating (0-99) | `91` |
| `potential` | `Integer` | Maximum potential rating (0-99) | `94` |
| `value_eur` | `Integer` | Career Mode market value in Euros | `181500000` |
| `wage_eur` | `Integer` | Career Mode weekly wage in Euros | `230000` |
| `pace`, `shooting`... | `Integer` | FUT Face Stats categories (0-99) | `97`, `90` |
| `finishing`, `stamina`...| `Integer` | Detailed in-game statistics (0-99) | `93`, `88` |
| `playstyles` | `String` | Regular PlayStyles separated by commas | `"Rapid, Finesse Shot"` |

---

## 💻 Data results

<!-- SEASONS_SUMMARY_START -->
<details open>
<summary><b>⚽ EA FC 26</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **E. Haaland** | Manchester City | ST | 91 | €172.5M |
| **K. Mbappé** | Real Madrid | ST, LW, LM | 91 | €157.0M |
| **Pedri** | FC Barcelona | CM, CDM, CAM | 90 | €165.0M |
| **Vitinha** | Paris Saint-Germain | CM, CDM, CAM | 90 | €149.0M |
| **O. Dembélé** | Paris Saint-Germain | ST, RW, CAM | 90 | €122.5M |
| **H. Kane** | Bayern München | ST | 90 | €101.0M |
| **T. Courtois** | Real Madrid | GK | 90 | €39.0M |
| **Lamine Yamal** | FC Barcelona | RW, RM | 89 | €147.0M |
| **J. Bellingham** | Real Madrid | CAM, CM, LM | 89 | €150.5M |
| **Vini Jr.** | Real Madrid | LW, ST, LM | 89 | €141.0M |

</details>

<details>
<summary><b>⚽ EA FC 25</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **Rodri** | Manchester City | CDM, CM | 91 | €115.5M |
| **M. Salah** | Liverpool FC | RM, RW | 91 | €104.0M |
| **J. Bellingham** | Real Madrid | CAM, CM | 90 | €174.5M |
| **Vini Jr.** | Real Madrid | LW, ST | 90 | €171.5M |
| **K. Mbappé** | Real Madrid | ST, LW | 90 | €160.0M |
| **E. Haaland** | Manchester City | ST | 90 | €157.0M |
| **V. van Dijk** | Liverpool FC | CB | 90 | €77.5M |
| **H. Kane** | Bayern München | ST | 90 | €117.5M |
| **F. Wirtz** | Bayer 04 Leverkusen | CAM, ST | 89 | €143.5M |
| **Alisson** | Liverpool FC | GK | 89 | €54.5M |

</details>

<details>
<summary><b>⚽ EA FC 24</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **E. Haaland** | Manchester City | ST | 91 | €185.0M |
| **K. Mbappé** | Paris Saint-Germain | ST, LW | 91 | €181.5M |
| **K. De Bruyne** | Manchester City | CM, CAM | 91 | €103.0M |
| **Rodri** | Manchester City | CDM, CM | 90 | €129.5M |
| **H. Kane** | Bayern München | ST | 90 | €119.5M |
| **T. Courtois** | Real Madrid | GK | 90 | €63.0M |
| **R. Lewandowski** | FC Barcelona | ST | 90 | €58.0M |
| **L. Messi** | Inter Miami | CF, CAM | 90 | €41.0M |
| **Vini Jr.** | Real Madrid | LW, ST | 89 | €158.5M |
| **Rúben Dias** | Manchester City | CB | 89 | €106.5M |

</details>
<!-- SEASONS_SUMMARY_END -->

---

## ⚡ Quick start

```
import pandas as pd

# Load EA FC 24 data directly from GitHub
url = "https://raw.githubusercontent.com/mzafram2001/ea-fc/main/data/dataset_ea_fc_24.csv"
df_fc24 = pd.read_csv(url)

# Find the top 5 young players with the highest potential
wonderkids = df_fc24[df_fc24['age'] <= 21].sort_values(by="potential", ascending=False)
print(wonderkids[['short_name', 'club_name', 'overall', 'potential', 'value_eur']].head())
```
---

> [!CAUTION]
> **Disclaimer:** Data is collected from public sources. This repository is for educational and research purposes only. Not financial advice.

> [!TIP]
> **Want to help?**
> ⭐ Do you like this project? If you find this data useful, please give it a star! It helps me keep updating it.
>
> ☕ If this dataset saves you time in your analysis or fantasy leagues, you can also [buy me a coffee on Ko-fi](https://ko-fi.com/mzm0102).
<br>
<!-- LAST_CHECKED_START -->Last checked: 2026-08-31<!-- LAST_CHECKED_END -->
