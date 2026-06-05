# Polyhouse Data Quality Report

Total observations: 365
Date range: 2024-01-01 to 2024-12-30
Typical sampling frequency: every 1.0 day(s)

## Summary Statistics

|               |   count |   mean |   std |    min |    25% |    50% |    75% |     max |    cv |
|:--------------|--------:|-------:|------:|-------:|-------:|-------:|-------:|--------:|------:|
| temperature_c |     365 |  21.99 |  1.41 |  18.15 |  21.01 |  21.97 |  22.88 |   26.37 | 0.064 |
| humidity_pct  |     365 |  86.74 |  3.07 |  78.1  |  84.6  |  86.7  |  88.7  |   94.8  | 0.035 |
| co2_ppm       |     365 | 901.16 | 78.27 | 608    | 854    | 904    | 949    | 1154    | 0.087 |
| yield_kg      |     365 |  17.14 |  0.68 |  15.31 |  16.7  |  17.13 |  17.63 |   18.85 | 0.04  |

## Data Quality

Rows passing validity rules: 100.0%

## Interpretation

- Average yield is 17.14 kg/day while median yield is 17.13 kg/day.
- Mean and median yield are similar, indicating little skew.
- Yield standard deviation is 0.68 kg.
- Average humidity is 86.7%, which falls within the expected polyhouse range.
- Humidity variability is low (CV = 0.035), indicating stable polyhouse environmental conditions.
- CO₂ variability is moderate (CV = 0.087), which may reflect normal ventilation cycles.
- Yield variability is low (CV = 0.04), suggesting relatively consistent mushroom production throughout the year.