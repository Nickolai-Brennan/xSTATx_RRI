# xSTATx RRI Scoring System

Welcome to the official repository for the **xSTATx Reliever Reliability Index (RRI)**. This repo powers a modern evaluation framework for MLB bullpen arms using advanced stats, real-time usage data, and fantasy value modeling.

---

## 📂 Repository Structure

```bash
xSTATx-RRI-Scoring/
├── README.md                  ← Overview and getting started
├── data/                      ← Raw and processed data files
├── notebooks/                 ← Jupyter + Databricks notebooks
├── scripts/                   ← Python scripts for scoring, syncing, modeling
├── sql/                       ← Databricks-ready SQL queries
├── models/                    ← ML models for RRI projections
├── dashboards/                ← Streamlit and HTML leaderboards
├── docs/                      ← Technical references, icon maps, glossary
└── .github/workflows/         ← GitHub Actions for automation
```

---

## 🧠 Key Components

### 🔢 `calculate_rri.py`
- Contains the core scoring logic for RRI, including xFIP, K/BB, CSW%, leverage index, role type, and stuff grades.

### 📄 `sync_google_sheets.py`
- Authenticates and downloads Sheets-based overrides or scouting notes for custom projections.

### 📊 `streamlit_app.py`
- Launch a full leaderboard UI with interactive uploads, filters, and sortable RRI rankings.

---

## 📚 Docs Summary

### `docs/RRI_Formula.md`
Explains the complete formula and each scoring factor:
- Role Base Score
- xFIP / K/BB / CSW% Tiers
- Stuff+ and Spin Rate Boosts
- Team Standings Bonus
- Prospect / Injury / Trade Penalties

### `docs/Glossary.md`
Defines each stat used in the model:
- wOBAA, xERA, pLI, SIERA, SVH3, QA4, etc.

### `docs/Emoji_Stat_Icon_Map.md`
Icon legend used in visual dashboards:
- 🎯 = Command
- 🧊 = Clutch
- 💨 = Velocity
- 🧱 = Elite Inherited Runner Stopper

### `docs/Version_History.md`
RRI formula changes and updates across 2024–2025.

---

## 🔄 Unified Toolchain: How It All Works

| Tool           | Purpose                                                                 |
|----------------|-------------------------------------------------------------------------|
| **Google Sheets** | Manual overrides, scouting notes, and prospect tracking               |
| **RowZero**        | Front-end analytics for Top 5% metrics, dynamic dashboards            |
| **Google Drive**   | Central storage for exported CSVs and data versioning                |
| **Databricks**     | Core compute engine for scoring, cleaning, modeling                  |
| **OpenAI**         | Player blurbs, tier analysis, fantasy insight generation             |
| **GitHub**         | Version control, workflows, documentation, community contributions   |
| **Python**         | All backend logic for calculation, syncing, dashboard generation     |
| **SQL**            | Delta table creation, joins, and real-time RRI scoring in Databricks |

### 🌐 Workflow Sequence

1. **Manual Input** → `Google Sheets`
2. **Auto-Pulled to GitHub** → via Apps Script or Zapier
3. **Loaded into `data/raw/`** for GitHub tracking
4. **Databricks Notebooks** transform and apply `calculate_rri()`
5. **Python Scripts** enhance scoring with AI (e.g., OpenAI insights)
6. **Dashboards** (Streamlit/RowZero) update with new RRI + icons
7. **Finals saved in `data/processed/`** and pushed back to Sheets or WordPress

---

## 🚀 Getting Started

```bash
# Clone the repo
$ git clone https://github.com/yourname/xSTATx-RRI-Scoring.git
$ cd xSTATx-RRI-Scoring

# Install requirements
$ pip install -r requirements.txt

# Run Streamlit dashboard
$ streamlit run dashboards/streamlit_app.py
```

---

## 🛠️ GitHub Workflows
- `nightly_update.yml` → Automate daily RRI recalculation
- `sync_gsheets_to_git.yml` → Sync latest data from Google Sheets

---

## 🧩 WordPress + Hostinger Deployment

If you're hosting your RRI leaderboard or dashboards on a **WordPress.org** site via **Hostinger**, follow this setup:

1. **Upload HTML Leaderboards** to your WordPress `uploads` or use a plugin like "Insert HTML Snippet".
2. **Use `<iframe>` embeds** to load `rri_leaderboard.html` directly onto blog pages or landing sections.
3. **Deploy Streamlit to a public web app** (or use local hosting via ngrok) and link in WP.
4. **Sync leaderboard data** via Google Sheets live embed or CSV-to-HTML conversion plugin.
5. **Optimize SEO** with metadata for player names, RRI tags, fantasy values.

🔗 Bonus: Connect **Mailchimp** or **ConvertKit** forms on WP to allow subscriber-only access to Top 25 Rankings.

---

## 📬 Contact / Contribute

Interested in contributing, building fantasy dashboards, or API integrations?
- DM @xSTATx on Twitter or GitHub
- Fork this repo and submit PRs

---

🧪 Powered by Databricks, OpenAI, Python, RowZero, and the ⚾️ community of nerds.
🌐 Distributed via GitHub, Sheets, Streamlit, and WordPress.org on Hostinger.
