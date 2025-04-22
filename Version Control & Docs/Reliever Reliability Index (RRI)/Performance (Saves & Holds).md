### 💾 SVH3_Score Calculation (15% of RRI)

The **SVH3 Score** reflects a reliever’s consistency and value in securing wins through **saves, holds**, and **game leverage**.
It accounts for efficiency, opportunity, and impact when pitching in high-stakes scenarios.

---

#### 🔐 **Saves Component**
```python
Save_Score = (
    scale(Save_Percentage_Rank) + 
    scale(Save_Opportunities) - 
    0.25 * Blown_Saves
)
```
- **Save Percentage Rank**: Relative efficiency vs league peers
- **Save Opportunities**: Total chances taken into account
- **Blown Saves**: Penalized at 25% weight


#### 🛡️ **Holds Component**
```python
Hold_Score = (
    scale(Hold_Percentage_Rank) + 
    scale(Hold_Opportunities) - 
    0.25 * IR_Scored_Pct
)
```
- **Hold Percentage Rank**: Relative hold efficiency
- **Hold Opportunities**: Volume of games pitched with lead
- **Inherited Runners Scored %**: Penalizes poor strand rate


#### 📈 **Holds Ranking Bonus**
```python
HLD_Impact = Holds_Leader_Tier + 0.25 * scale(Avg_Leverage)
```
- **Holds Leader Tier**: +2 to +5 for Top 10 in league
- **Average Leverage Index**: Additional weight to high-pressure roles


#### 🧮 **Final SVH3 Score**
```python
if current_week >= halfway_point:
    SVH3_Score = min(
        10,
        0.5 * Save_Score + 
        0.4 * Hold_Score + 
        0.1 * HLD_Impact
    )
else:
    SVH3_Score = 0  # No SVH3 contribution before halfway mark
```
- Weighted blend (post All-Star break or Week 13+):
  - Saves: 50%
  - Holds: 40%
  - Hold Tier/Leverage: 10%
- **Score is capped at +10 RRI points**
- **No minimum contribution until halfway through the season**

Use in final equation:
```python
RRI += 0.15 * SVH3_Score
```

---

📌 This component adjusts weekly with updated usage and impact metrics.
📆 SVH3 scoring activates **after the midpoint** of the season to ensure sample size stability.
