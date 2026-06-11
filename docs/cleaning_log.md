# Cleaning Log - Task 2

## Missing Values Before Cleaning
timestamp         0
temperature_c    50
humidity_pct     41
co2_ppm          30
yield_kg          0

## Missing Value Percentages Before Cleaning (%)
timestamp        0.00
temperature_c    4.93
humidity_pct     4.04
co2_ppm          2.96
yield_kg         0.00

## Missing Values After Cleaning
timestamp        0
temperature_c    0
humidity_pct     0
co2_ppm          0
yield_kg         0
is_outlier       0

## Missing Value Percentages After Cleaning (%)
timestamp        0.0
temperature_c    0.0
humidity_pct     0.0
co2_ppm          0.0
yield_kg         0.0
is_outlier       0.0

## Validity Rules Applied
- temperature_c: 10–35°C
- humidity_pct: 50–100%
- co2_ppm: 400–2000 ppm

## Agritech Cleaning Rationale
- Temperature, humidity and CO₂ are sensor measurements.
- Short sensor outages (≤2 readings) are forward-filled.
- Longer outages are removed because sensor conditions are unknown.
- yield_kg is never imputed to avoid creating artificial labels.

## Duplicate Handling
- Duplicate timestamps detected: 15
- Duplicate rows removed: 15

## Outlier Review
- Outliers flagged: 6
- Outliers retained in audit dataset and removed from modeling dataset.

## Row Removal Summary
- Rows before cleaning: 1015
- Rows after cleaning: 994
- Rows dropped: 21
- Percentage dropped: 2.07%

## Output Files
- Audit dataset: data\interim\02_with_outliers.parquet
- Clean dataset: data\processed\02_cleaned.parquet
- Sample file: data\processed\cleaned_sample_50_rows.csv
