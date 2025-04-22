## 🔢 Performance Metrics Component – 30% Weight

Each reliever’s **RRI Score** draws 30% from performance metrics. These are scaled from best-in-league to replacement-level.

### 🧮 RRI_Performance =  
  (0.10 × Scaled ERA)  
+ (0.10 × Scaled xFIP)  
+ (0.05 × Scaled WHIP)  
+ (0.05 × Scaled K/9)  
+ (0.05 × Scaled BB/9 [inverted])  
+ (0.10 × K-BB%)  
+ (0.05 × SIERA)  
+ (0.05 × CSW%)  
+ (0.05 × SwStr%)  
+ (0.05 × Hard% [inverse])

- **Elite CSW% > 33%** → bonus applied
- **xFIP ≤ 3.00** → strong leverage boost
- **Hard% > 40%** → significant penalty
- **SIERA vs ERA delta** is used to measure true skill

📌 All metrics are smoothed over rolling 30-day or 60-day windows when available.
