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
│   ├── dataset_ea_fc_26.csv
│   ├── dataset_ea_fc_25.csv
│   ├── dataset_ea_fc_24.csv
│   ├── dataset_fifa_23.csv
│   ├── dataset_fifa_22.csv
│   └── ...
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
<summary><b>⚽ FIFA 23</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **K. Mbappé** | Paris Saint-Germain | ST, LW | 91 | €190.5M |
| **K. De Bruyne** | Manchester City | CM, CAM | 91 | €107.5M |
| **R. Lewandowski** | FC Barcelona | ST | 91 | €84.0M |
| **K. Benzema** | Real Madrid | CF, ST | 91 | €64.0M |
| **L. Messi** | Paris Saint-Germain | RW | 91 | €54.0M |
| **E. Haaland** | Manchester City | ST | 90 | €176.5M |
| **T. Courtois** | Real Madrid | GK | 90 | €79.5M |
| **Alisson** | Liverpool FC | GK | 89 | €79.0M |
| **J. Kimmich** | Bayern München | CDM, RB, CM | 89 | €105.5M |
| **J. Oblak** | Atlético Madrid | GK | 89 | €79.0M |

</details>

<details>
<summary><b>⚽ FIFA 22</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **R. Lewandowski** | Bayern München | ST | 92 | €119.5M |
| **L. Messi** | Paris Saint-Germain | RW, ST, CF | 92 | €69.5M |
| **K. Mbappé** | Paris Saint-Germain | ST, LW | 91 | €194.0M |
| **M. Salah** | Liverpool FC | RW | 91 | €129.0M |
| **K. De Bruyne** | Manchester City | CM, CAM | 91 | €125.5M |
| **K. Benzema** | Real Madrid | CF, ST | 91 | €84.0M |
| **Cristiano Ronaldo** | Manchester United | ST | 91 | €45.0M |
| **N. Kanté** | Chelsea FC | CDM, CM | 90 | €100.0M |
| **V. van Dijk** | Liverpool FC | CB | 90 | €100.0M |
| **Neymar Jr** | Paris Saint-Germain | LW, CAM | 90 | €117.5M |

</details>

<details>
<summary><b>⚽ FIFA 21</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **L. Messi** | Paris Saint-Germain | RW, ST, CF | 93 | €103.5M |
| **R. Lewandowski** | Bayern München | ST | 92 | €124.5M |
| **Cristiano Ronaldo** | Juventus FC | ST, LW | 92 | €63.0M |
| **J. Oblak** | Atlético Madrid | GK | 91 | €120.0M |
| **K. De Bruyne** | Manchester City | CM, CAM, CF | 91 | €127.5M |
| **Neymar Jr** | Paris Saint-Germain | LW, CAM | 91 | €132.0M |
| **K. Mbappé** | Paris Saint-Germain | ST, LW | 90 | €185.5M |
| **M. ter Stegen** | FC Barcelona | GK | 90 | €102.0M |
| **V. van Dijk** | Liverpool FC | CB | 90 | €113.0M |
| **M. Salah** | Liverpool FC | RW | 90 | €120.5M |

</details>

<details>
<summary><b>⚽ FIFA 20</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **L. Messi** | FC Barcelona | RW, ST, CF | 94 | €95.5M |
| **Cristiano Ronaldo** | Juventus FC | ST, LW | 93 | €58.5M |
| **Neymar Jr** | Paris Saint-Germain | LW, CAM | 92 | €105.5M |
| **J. Oblak** | Atlético Madrid | GK | 91 | €77.5M |
| **V. van Dijk** | Liverpool FC | CB | 91 | €90.0M |
| **K. De Bruyne** | Manchester City | CAM, CM | 91 | €90.0M |
| **R. Lewandowski** | Bayern München | ST | 91 | €86.0M |
| **E. Hazard** | Real Madrid | LW, ST | 91 | €90.0M |
| **M. ter Stegen** | FC Barcelona | GK | 90 | €67.5M |
| **Alisson** | Liverpool FC | GK | 90 | €64.5M |

</details>

<details>
<summary><b>⚽ FIFA 19</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **L. Messi** | FC Barcelona | CF, RW, ST | 94 | €110.5M |
| **Cristiano Ronaldo** | Juventus FC | ST, LW | 94 | €77.0M |
| **Neymar Jr** | Paris Saint-Germain | LW, CAM | 92 | €108.0M |
| **J. Oblak** | Atlético Madrid | GK | 91 | €75.5M |
| **K. De Bruyne** | Manchester City | CAM, CM | 91 | €93.0M |
| **E. Hazard** | Chelsea FC | LW, CF | 91 | €93.0M |
| **L. Modrić** | Real Madrid | CM | 91 | €67.0M |
| **L. Suárez** | FC Barcelona | ST | 91 | €80.0M |
| **H. Kane** | Tottenham Hotspur | ST | 90 | €96.5M |
| **De Gea** | Manchester United | GK | 90 | €62.5M |

</details>

<details>
<summary><b>⚽ FIFA 18</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **L. Messi** | FC Barcelona | CF, ST, RW | 94 | €118.5M |
| **Cristiano Ronaldo** | Real Madrid | LW, ST | 94 | €95.5M |
| **Neymar** | Paris Saint-Germain | LW | 92 | €119.5M |
| **L. Suárez** | FC Barcelona | ST | 92 | €97.0M |
| **M. Neuer** | Bayern München | GK | 92 | €61.0M |
| **De Gea** | Manchester United | GK | 91 | €74.5M |
| **K. De Bruyne** | Manchester City | CAM, CM | 91 | €104.5M |
| **R. Lewandowski** | Bayern München | ST | 91 | €92.0M |
| **E. Hazard** | Chelsea FC | LW, CF | 91 | €95.5M |
| **T. Kroos** | Real Madrid | CM, CDM | 90 | €79.0M |

</details>

<details>
<summary><b>⚽ FIFA 17</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **Cristiano Ronaldo** | Real Madrid | LW, ST | 94 | €87.0M |
| **L. Messi** | FC Barcelona | RW | 93 | €89.0M |
| **Neymar** | FC Barcelona | LW | 92 | €106.0M |
| **L. Suárez** | FC Barcelona | ST | 92 | €83.0M |
| **M. Neuer** | Bayern München | GK | 92 | €69.5M |
| **De Gea** | Manchester United | GK | 90 | €68.5M |
| **R. Lewandowski** | Bayern München | ST | 90 | €71.0M |
| **G. Bale** | Real Madrid | RW | 90 | €72.0M |
| **Z. Ibrahimović** | Manchester United | ST | 90 | €36.5M |
| **T. Courtois** | Chelsea FC | GK | 89 | €65.5M |

</details>

<details>
<summary><b>⚽ FIFA 16</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **L. Messi** | FC Barcelona | RW, CF | 94 | €101.0M |
| **Cristiano Ronaldo** | Real Madrid | LW, LM, ST | 93 | €85.5M |
| **Neymar** | FC Barcelona | LW | 90 | €89.5M |
| **L. Suárez** | FC Barcelona | ST | 90 | €69.0M |
| **M. Neuer** | Bayern München | GK | 90 | €58.0M |
| **Z. Ibrahimović** | Paris Saint-Germain | ST | 89 | €40.5M |
| **A. Robben** | Bayern München | RM, RW | 89 | €50.0M |
| **E. Hazard** | Chelsea FC | LM | 88 | €64.0M |
| **M. Özil** | Arsenal FC | CAM | 88 | €61.0M |
| **R. Lewandowski** | Bayern München | ST | 88 | €57.0M |

</details>

<details>
<summary><b>⚽ FIFA 15</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **L. Messi** | FC Barcelona | CF, RW | 93 | €100.5M |
| **Cristiano Ronaldo** | Real Madrid | LW, ST | 92 | €79.0M |
| **M. Neuer** | Bayern München | GK | 90 | €63.5M |
| **A. Robben** | Bayern München | RM, LM, RW | 90 | €54.5M |
| **L. Suárez** | FC Barcelona | ST, CF, RW | 89 | €49.5M |
| **Z. Ibrahimović** | Paris Saint-Germain | ST | 89 | €34.5M |
| **Iniesta** | FC Barcelona | CM | 89 | €36.0M |
| **E. Hazard** | Chelsea FC | LM | 88 | €40.5M |
| **F. Ribéry** | Bayern München | LM | 88 | €33.0M |
| **B. Schweinsteiger** | Bayern München | CM, CDM | 88 | €39.0M |

</details>

<details>
<summary><b>⚽ FIFA 14</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **L. Messi** | FC Barcelona | CF | 94 | €78.0M |
| **Cristiano Ronaldo** | Real Madrid | LW, LM | 92 | €56.0M |
| **Z. Ibrahimović** | Paris Saint-Germain | ST | 90 | €38.5M |
| **L. Suárez** | Liverpool FC | ST, CF | 89 | €32.0M |
| **Falcao** | AS Monaco | ST | 89 | €32.0M |
| **F. Ribéry** | Bayern München | LM | 89 | €24.0M |
| **R. van Persie** | Manchester United | ST | 89 | €30.0M |
| **Iniesta** | FC Barcelona | CM, LW | 89 | €25.5M |
| **E. Hazard** | Chelsea FC | LM, RM | 88 | €36.0M |
| **S. Agüero** | Manchester City | ST | 88 | €42.0M |

</details>

<details>
<summary><b>⚽ FIFA 13</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **L. Messi** | FC Barcelona | CF, ST, RW | 94 | €107.5M |
| **Cristiano Ronaldo** | Real Madrid | LW, LM, ST, RM | 92 | €80.5M |
| **Falcao** | Atlético Madrid | ST | 90 | €38.5M |
| **Iniesta** | FC Barcelona | CM, LW, CAM | 90 | €34.0M |
| **F. Ribéry** | Bayern München | LM, RM | 90 | €26.0M |
| **Xavi** | FC Barcelona | CM, CAM | 90 | €18.5M |
| **Z. Ibrahimović** | Paris Saint-Germain | ST | 89 | €23.0M |
| **R. van Persie** | Manchester United | ST, CF | 89 | €26.0M |
| **David Silva** | Manchester City | CAM, RM, LM | 88 | €30.5M |
| **Casillas** | Real Madrid | GK | 88 | €12.5M |

</details>

<details>
<summary><b>⚽ FIFA 12</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **L. Messi** | FC Barcelona | CF, ST, RW | 94 | €92.5M |
| **Cristiano Ronaldo** | Real Madrid | LW, LM, ST, RM | 92 | €68.0M |
| **Iniesta** | FC Barcelona | CAM, CM, RW, LW | 91 | €38.5M |
| **Xavi** | FC Barcelona | CM, CAM, CDM | 91 | €21.5M |
| **W. Rooney** | Manchester United | CF, ST | 90 | €38.5M |
| **Cesc Fàbregas** | FC Barcelona | CAM, CM, CDM | 89 | €35.5M |
| **Casillas** | Real Madrid | GK | 89 | €20.0M |
| **F. Ribéry** | Bayern München | LM, RW, RM | 89 | €27.0M |
| **A. Robben** | Bayern München | RM, LM, RW, LW | 89 | €24.5M |
| **N. Vidić** | Manchester United | CB | 89 | €16.0M |

</details>

<details>
<summary><b>⚽ FIFA 11</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **L. Messi** | FC Barcelona | RW, RF, ST, CAM | 90 | €0 |
| **Cristiano Ronaldo** | Real Madrid | RW, CAM, LW, ST | 89 | €0 |
| **Casillas** | Real Madrid | GK | 88 | €0 |
| **David Villa** | FC Barcelona | ST, CF, LW, CAM | 88 | €0 |
| **W. Rooney** | Manchester United | ST, CF, LW, LF | 87 | €0 |
| **N. Vidić** | Manchester United | CB | 87 | €0 |
| **Xavi** | FC Barcelona | CM, CAM, CDM | 87 | €0 |
| **Iniesta** | FC Barcelona | CAM, CM, RW, LW | 87 | €0 |
| **A. Robben** | Bayern München | RM, LM, RW, LW | 87 | €0 |
| **F. Ribéry** | Bayern München | LM, LW, CAM, RW | 86 | €0 |

</details>

<details>
<summary><b>⚽ FIFA 10</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **L. Messi** | FC Barcelona | RW | 90 | €0 |
| **Casillas** | Real Madrid | GK | 90 | €0 |
| **Cristiano Ronaldo** | Real Madrid | RW | 89 | €0 |
| **W. Rooney** | Manchester United | CF | 89 | €0 |
| **Júlio César** | Inter Milan | GK | 89 | €0 |
| **F. Fabregas** | Arsenal FC | CM | 88 | €0 |
| **G. Buffon** | Juventus FC | GK | 88 | €0 |
| **David Villa** | Valencia CF | ST | 88 | €0 |
| **Fernando Torres** | Liverpool FC | ST | 88 | €0 |
| **S. Gerrard** | Liverpool FC | CAM | 88 | €0 |

</details>

<details>
<summary><b>⚽ FIFA 09</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **Casillas** | Real Madrid | GK | 91 | €0 |
| **L. Messi** | FC Barcelona | RW | 90 | €0 |
| **Cristiano Ronaldo** | Manchester United | RW | 90 | €0 |
| **G. Buffon** | Juventus FC | GK | 90 | €0 |
| **Z. Ibrahimović** | Inter Milan | ST | 89 | €0 |
| **Kaká** | AC Milan | CAM | 89 | €0 |
| **F. Ribéry** | Bayern München | LM | 88 | €0 |
| **Fernando Torres** | Liverpool FC | ST | 88 | €0 |
| **P. Čech** | Chelsea FC | GK | 88 | €0 |
| **A. Nesta** | AC Milan | CB | 88 | €0 |

</details>

<details>
<summary><b>⚽ FIFA 08</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **Cristiano Ronaldo** | Manchester United | RW | 91 | €0 |
| **Ronaldinho** | FC Barcelona | CAM | 91 | €0 |
| **G. Buffon** | Juventus FC | GK | 91 | €0 |
| **A. Nesta** | AC Milan | CB | 91 | €0 |
| **T. Henry** | FC Barcelona | ST | 91 | €0 |
| **Kaká** | AC Milan | CAM | 90 | €0 |
| **W. Rooney** | Manchester United | CF | 90 | €0 |
| **J. Terry** | Chelsea FC | CB | 90 | €0 |
| **H. de Noteboom** | Netherlands | ST | 90 | €0 |
| **David Villa** | Valencia CF | ST | 89 | €0 |

</details>

<details>
<summary><b>⚽ FIFA 07</b></summary>

#### 👤 Top 10 Players

| Player | Club | Position | Overall | Value |
| :--- | :--- | :--- | :--- | :--- |
| **W. Rooney** | Manchester United | ST | 93 | €0 |
| **G. Buffon** | Juventus FC | GK | 93 | €0 |
| **G. Coupet** | Olympique Lyonnais | GK | 92 | €0 |
| **Ronaldinho** | FC Barcelona | CAM | 91 | €0 |
| **T. Henry** | Arsenal FC | ST | 91 | €0 |
| **F. Cannavaro** | Real Madrid | CB | 91 | €0 |
| **A. Nesta** | AC Milan | CB | 91 | €0 |
| **J. Terry** | Chelsea FC | CB | 91 | €0 |
| **D. Trezeguet** | Juventus FC | ST | 90 | €0 |
| **F. Lampard** | Chelsea FC | CM | 90 | €0 |

</details>

<details>
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
