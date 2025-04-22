## 🧮 Full RRI Formula Breakdown

```python
RRI = (
    0.25 * RRI_Previous +
    0.50 * RRI_Current_Season +
    0.25 * RRI_NonPlaying_Score
)
```

---

### 🔷 RRI_Current_Season (50%)
```python
RRI_Current_Season = (
    0.30 * Performance_Metrics +
    0.20 * Leverage_Usage_Score +
    0.15 * SVH3_Score +
    0.15 * Stuff_Quality_Score +
    0.10 * Batted_Ball_Score +
    0.10 * Clutch_IR_Score
)
```

### 🧪 Performance_Metrics (30%)
```python
Performance_Metrics = (
    0.10 * scale(ERA) +
    0.10 * scale(xFIP) +
    0.05 * scale(WHIP) +
    0.05 * scale(K_9) +
    0.05 * scale_inverse(BB_9) +
    0.10 * scale(K_BB_Pct) +
    0.05 * scale(SIERA) +
    0.05 * scale(CSW_Pct) +
    0.05 * scale(SwStr_Pct) +
    0.05 * scale_inverse(Hard_Pct)
)

)
```

### ⚡ Leverage & Usage Score (20%)
```python
Leverage_Usage_Score = (
    0.50 * scale(pLI) +
    0.25 * scale(gmLI) +
    0.25 * scale(Avg_LI)
)
```

### 🛡️ SVH3 Score (15%)
```python
SVH3 Score = (
      Saves (Save Percentage Rank + Save Oppurtunities - Saves Blown 25%) 
      Save Ranking (Save Leader 25%)
      HLD (Holds): a measure of a reliever's holds.
      Holds (Hold Percentage Rank + Hold Oppurtunities -  Inherited Runners Scored % 25%)
      Holds Ranking (Holds Leader + Average Leverage Rating 25%)
      )
SVH3_Score
          ** 0.5 * Save_Score +  0.4 * Hold_Score + 0.1 * HLD_Impact **

```
    
```

### **💨 **Stuff + Quality Score** (15%)**
```python
Stuff_Quality_Score = (
    0.075 * scale(StuffPlus_PitchingPlus_LocationPlus) +
    0.0375 * scale(CSW_Pct) +  
    0.0375 * scale(Weighted_Pitch_Value)
)
```
---

### 🟤 Batted Ball Score (10%)
```python
Batted_Ball_Score = (
    0.80 * scale(CSW_Pct) +
    0.10 * scale(Soft_Pct) +
    0.10 * scale_inverse(Hard_Pct)
)
```

### 🧊 Clutch & Inherited Runners Score (10%)
```python
Clutch_IR_Score = (
    0.50 * scale(Clutch) +
    0.50 * scale(IR_Success_Pct)
)
```

---

### 🟡 RRI_NonPlaying_Score (25%)
```python
RRI_NonPlaying_Score = (
    0.05 * Prospect_Boost +
    0.05 * Injury_Adjustment +
    0.05 * Team_Contender_Bonus +
    0.01 * Trade_Risk_Penalty +
    0.05 * Role_Classification_Bonus +
    0.04 * Age_Adjustment
)
```

---

### 🔁 Additive Modifiers (Stacked After Core RRI)
```python
# Additive Modifiers
+ Versatility_Bonus            # up to +5 for multi-role usage
+ Division_Rank_Bonus          # +5 for top team

# Tiered Emoji Badges
+2 for 🎯, 🧱, 💨, 🧊 icons (max +8 total)

# Cap Removal Logic
# No upper cap on RRI. Scores above 125 are permitted
# for historically elite profiles (e.g., Devin Williams peak).

# Floor Handling
# If RRI < 30 and role ≠ prospect call-up
# → apply Regression Factor to stabilize score
```

📌 Use this full breakdown to calculate and track reliever RRI with seasonally evolving components and contextual weights.

## 🧮 Full RRI Formula Breakdown with Scale Weights and Rating Tiers

```python
RRI = (
    0.25 * RRI_Previous +            # Previous season score
    0.50 * RRI_Current_Season +      # Current year production (detailed below)
    0.25 * RRI_NonPlaying_Score      # Contextual non-performance inputs
)
```

---

### 🔷 RRI_Current_Season (50%)
```python
RRI_Current_Season = (
    0.30 * Performance_Metrics +
    0.20 * Leverage_Usage_Score +
    0.15 * SVH3_Score +
    0.15 * Stuff_Quality_Score +
    0.10 * Batted_Ball_Score +
    0.10 * Clutch_IR_Score
)
```

### 🧪 Performance_Metrics (30%) – Tiered Scale Reference
All stats are **scaled from 0–10** using tiered or percentile logic.

#### ERA Scale
| ERA Range     | RRI Points |
|---------------|------------|
| < 2.50        | +10        |
| 2.50–2.99     | +8         |
| 3.00–3.49     | +6         |
| 3.50–3.99     | +4         |
| 4.00–4.49     | +2         |
| ≥ 4.50        |  0         |

#### xFIP / SIERA Scale (similar to ERA)
- < 3.00 → +10
- 3.00–3.49 → +8
- 3.50–3.99 → +5
- 4.00–4.49 → +2
- ≥ 4.50 → 0

#### WHIP
- < 1.00 → +10
- 1.00–1.10 → +8
- 1.11–1.20 → +6
- 1.21–1.30 → +4
- 1.31–1.40 → +2
- > 1.40 → 0

#### K/9
- > 13.0 → +10
- 11.0–13.0 → +8
- 9.0–11.0 → +6
- 7.0–9.0 → +4
- < 7.0 → +2

#### BB/9 (inverse scale)
- < 1.5 → +10
- 1.5–2.0 → +8
- 2.1–2.5 → +6
- 2.6–3.0 → +4
- > 3.0 → 0

#### K-BB%
- > 30% → +10
- 25–30% → +8
- 20–25% → +6
- 15–20% → +4
- < 15% → 0

#### CSW%, SwStr%, Hard%
- CSW% > 33% → +10, scaled down from there
- SwStr% > 16% → +10, 14–16% → +8, < 11% → 0
- Hard% < 28% → +10, 28–32% → +6, > 38% → 0

```python
Performance_Metrics = (
    0.10 * scale(ERA) +
    0.10 * scale(xFIP) +
    0.05 * scale(WHIP) +
    0.05 * scale(K_9) +
    0.05 * scale_inverse(BB_9) +
    0.10 * scale(K_BB_Pct) +
    0.05 * scale(SIERA) +
    0.05 * scale(CSW_Pct) +
    0.05 * scale(SwStr_Pct) +
    0.05 * scale_inverse(Hard_Pct)
)
```

---

### ⚡ Leverage & Usage Score (20%)
Percentile-based across rolling 30-day samples
```python
Leverage_Usage_Score = (
    0.50 * scale(pLI) +
    0.25 * scale(gmLI) +
    0.25 * scale(Avg_LI)
)
```

---

### 🛡️ SVH3 Score (15%) — Max Bonus = +10 RRI
```python
if current_week >= halfway_point:
    SVH3_Score = min(
        10,
        0.5 * Save_Score + 
        0.4 * Hold_Score + 
        0.1 * HLD_Impact
    )
else:
    SVH3_Score = 0
```

---

### 💨 Stuff + Quality Score (15%)
Tiered scaling of Stuff+, Location+, Pitching+, CSW%, pitch value
```python
Stuff_Quality_Score = (

      #### 🧠 Stuff+ / Pitching+ / Location+ Scale
            | Score Range | RRI Points |
            |-------------|------------|
            | > 140       | +6         |
            | 135–140     | +5         |
            | 130–134     | +4         |
            | 125–129     | +3         |
            | 120–124     | +2         |
            | 115–119     | +1         |
            | 100–114     | +0.25      |
            | < 100       | 0          |

    0.075 * scale(StuffPlus_PitchingPlus_LocationPlus) +
    0.0375 * scale(CSW_Pct) +  
    0.0375 * scale(Weighted_Pitch_Value)
)
```

---

### 🟤 Batted Ball Score (10%)
```python
Batted_Ball_Score = (
    0.80 * scale(CSW_Pct) +
    0.10 * scale(Soft_Pct) +
    0.10 * scale_inverse(Hard_Pct)
)
```

---

### 🧊 Clutch & Inherited Runners Score (10%)
```python
Clutch_IR_Score = (
    0.50 * scale(Clutch) +
    0.50 * scale(IR_Success_Pct)
)
```

---

### 🟡 RRI_NonPlaying_Score (25%)
```python
RRI_NonPlaying_Score = (
    0.05 * Prospect_Boost +
    0.05 * Injury_Adjustment +
    0.05 * Team_Contender_Bonus +
    0.01 * Trade_Risk_Penalty +
    0.05 * Role_Classification_Bonus +
    0.04 * Age_Adjustment
)
```

---

### 🔁 Additive Modifiers (Stacked After Core RRI)
```python
# Additive Modifiers
+ Versatility_Bonus            # +3 to +5 based on usage across roles
+ Division_Rank_Bonus          # +5 for division leader, +1 to -3 scaling

# Tiered Emoji Badges
+2 for 🎯, 🧱, 💨, 🧊 icons (max +8 total)

# Cap Removal Logic
# RRI can exceed 125 for historically elite arms

# Floor Handling
# If RRI < 30 and role ≠ prospect call-up
# → apply Regression Factor to stabilize score
```

📌 Each `scale()` uses:
- **Min-Max**: For traditional rates (ERA, WHIP, K/9)
- **Inverse Min-Max**: For penalty stats (BB/9, Hard%)
- **Tiered Range**: For tiered metrics (ERA tiers, CSW%, Stuff+)
- **Percentile Rank**: For contextual leverage (pLI, IR%)

📆 Rolling 30-day sampling used for usage, clutch, and CSW-related metrics.

