# 📚 RRI Glossary – xSTATx Reliever Reliability Index

This glossary defines every stat or metric referenced in the RRI scoring system. For advanced fantasy, scouting, and projection use.

---

## 🧠 Performance Metrics (RRI Core)
| Stat         | Definition |
|--------------|------------|
| `G`          | Games Played |
| `IP`         | Innings Pitched |
| `AVG`        | Batting Average Allowed |
| `BABIP`      | Batting Average on Balls in Play |
| `WHIP`       | Walks + Hits per Inning Pitched |
| `ERA`        | Earned Run Average |
| `xERA`       | Expected ERA (Statcast-based) |
| `xFIP`       | Expected FIP – Adjusted for league average HR/FB |
| `SIERA`      | Skill-Interactive ERA (FanGraphs) |
| `K/9`        | Strikeouts per 9 innings |
| `BB/9`       | Walks per 9 innings |
| `K-BB%`      | Strikeout % minus Walk % – elite reliability metric |
| `RAR`        | Runs Above Replacement |
| `WAR`        | Wins Above Replacement |
| `Dollars`    | Fantasy valuation from auction models |
| `HLD`        | Holds – used for SVH3 scoring |
| `SV`         | Saves – used for SVH3 scoring |
| `pLI`        | Leverage Index when pitcher enters game |
| `gmLI`       | Avg leverage across all game states for pitcher |
| `Clutch`     | Measures how performance differs in high/low leverage |
| `Swing%`     | Swing rate on all pitches seen |
| `SwStr%`     | Swinging Strike % (dominance marker) |
| `Zone%`      | % of pitches thrown in the strike zone |
| `CSW%`       | Called Strikes + Whiffs % (plate discipline) |
| `Soft%`      | % of batted balls classified as soft contact |
| `Hard%`      | % of hard-hit balls allowed |
| `Contact%`   | % of contact made on swings (lower = better) |

---

## 🧩 Icons + Stat Tiers Map

| Emoji | Meaning |
|-------|---------|
| 🎯   | Elite Command / Zone Control (CSW%, Zone%) |
| 🧊   | Cold-Blooded Clutch Pitcher (high gmLI, high IR%) |
| 💨   | Velocity Tier (Top 10% fastball, high SwStr%) |
| 🧱   | Wall – Elite inherited runner strand rate |
| 🔮   | Prospect Watch – Future RRI boost expected |
| 🚨   | Trade Risk – RRI penalty active due to rumors |
| 🏆   | Top 5% Metric Holder (spin, CSW%, SIERA, xERA, etc) |

Badges are assigned dynamically via `streamlit_app.py` and RowZero tags.

