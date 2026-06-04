# Cleaning Log - Task 2


**Missing Values Before Cleaning**
timestamp        0
temperature_c    0
humidity_pct     0
co2_ppm          0
yield_kg         0


**Missing Values After Cleaning**
timestamp        0
temperature_c    0
humidity_pct     0
co2_ppm          0
yield_kg         0
is_outlier       0


**Validity Rules Applied**
- temperature_c: 10–35°C
- humidity_pct: 50–100%
- co2_ppm: 400–2000 ppm


**Strategy**
- Forward-fill sensor columns (limit=2)
- Never impute yield_kg
- Remove duplicate timestamps using keep='last'
- Flag outliers using is_outlier column


**Output Files**
- Audit dataset: data\interim\02_with_outliers.parquet
- Clean dataset: data\processed\02_cleaned.parquet

**Row Removal Summary**
Rows before cleaning: 365
Rows after cleaning: 365
Rows dropped: 0
Percentage dropped: 0.00%
