# Polyhouse Data Quality Report

Total observations: 994
Date range: 2023-01-01 to 2025-09-26
Typical sampling frequency: every 1.0 day(s)

## Summary Statistics

|               |   count |   mean |    std |    min |    25% |    50% |     75% |     max |    cv |
|:--------------|--------:|-------:|-------:|-------:|-------:|-------:|--------:|--------:|------:|
| temperature_c |     994 |  22.24 |   2.37 |  16.46 |  20.25 |  22.31 |   24.15 |   34.5  | 0.107 |
| humidity_pct  |     994 |  89.86 |   3.18 |  82    |  87.24 |  89.74 |   92.45 |   98    | 0.035 |
| co2_ppm       |     994 | 945.47 | 121.86 | 400    | 872.25 | 959    | 1029    | 1224    | 0.129 |
| yield_kg      |     994 |  14.33 |   1.02 |   9.4  |  13.82 |  14.42 |   15.05 |   16.71 | 0.071 |

## Data Quality

Rows passing validity rules: 100.0%

## Interpretation

- Average yield is 14.33 kg/day while median yield is 14.42 kg/day.
- Mean and median yield are similar, indicating little skew.
- Yield standard deviation is 1.02 kg.
- Average humidity is 89.9%, which falls within the expected polyhouse range.
- Humidity variability is low (CV = 0.035), indicating stable polyhouse environmental conditions.
- CO₂ variability is moderate (CV = 0.129), which may reflect normal ventilation cycles.
- Yield variability is low (CV = 0.071), indicating relatively consistent mushroom production throughout the observation period.