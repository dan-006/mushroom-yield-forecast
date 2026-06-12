# Polyhouse Data Quality Report

Total observations: 980
Date range: 2023-01-01 to 2025-09-26
Typical sampling frequency: every 1.0 day(s)

## Summary Statistics

|               |   count |   mean |   std |    min |    25% |    50% |    75% |     max |    cv |
|:--------------|--------:|-------:|------:|-------:|-------:|-------:|-------:|--------:|------:|
| temperature_c |     980 |  21.96 |  1.49 |  16.53 |  20.98 |  21.98 |  22.92 |   26.77 | 0.068 |
| humidity_pct  |     980 |  86.78 |  3.06 |  77.9  |  84.8  |  86.9  |  88.8  |   95.7  | 0.035 |
| co2_ppm       |     980 | 903.35 | 81.34 | 655    | 847.75 | 902.5  | 959    | 1145    | 0.09  |
| yield_kg      |     980 |  17.12 |  0.69 |  14.64 |  16.68 |  17.13 |  17.57 |   19.25 | 0.04  |

## Data Quality

Rows passing validity rules: 100.0%

## Interpretation

- Average yield is 17.12 kg/day while median yield is 17.13 kg/day.
- Mean and median yield are similar, indicating little skew.
- Yield standard deviation is 0.69 kg.
- Average humidity is 86.8%, which falls within the expected polyhouse operating range.
- Humidity variability is low (CV = 0.035), indicating stable polyhouse environmental conditions.
- CO₂ variability is low (CV = 0.09), which may reflect normal ventilation cycles.
- Yield variability is low (CV = 0.04), indicating relatively consistent mushroom production throughout the observation period.