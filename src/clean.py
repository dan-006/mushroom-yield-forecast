import pandas as pd
from pathlib import Path

df = pd.read_parquet("data/interim/01_loaded.parquet")
initial_rows = len(df)

before_nulls = df.isna().sum()

print("\n=== INITIAL MISSING VALUES ===")
print(before_nulls)

df["is_outlier"] = ~(
    df["humidity_pct"].between(50, 100) &
    df["temperature_c"].between(10, 35) &
    df["co2_ppm"].between(400, 2000)
)

print("\nOutliers detected:", df["is_outlier"].sum())

sensor_cols = ["temperature_c", "humidity_pct", "co2_ppm"]

df[sensor_cols] = df[sensor_cols].ffill(limit=2)

df = df.dropna(subset=["yield_kg"])

df = df.drop_duplicates(subset=["timestamp"], keep="last")

after_nulls = df.isna().sum()

print("\n=== FINAL NULL CHECK ===")
print(after_nulls)

print("\nFinal shape:", df.shape)

audit_path = Path("data/interim/02_with_outliers.parquet")
df.to_parquet(audit_path, index=False)

df_clean = df[~df["is_outlier"]].copy()
final_rows = len(df_clean)

rows_dropped = initial_rows - final_rows
drop_pct = (rows_dropped / initial_rows) * 100

clean_path = Path("data/processed/02_cleaned.parquet")
df_clean.to_parquet(clean_path, index=False)

log_path = Path("docs/cleaning_log.md")
log_path.parent.mkdir(exist_ok=True)

with open(log_path, "w", encoding="utf-8") as f:
    f.write("# Cleaning Log - Task 2\n\n")

    f.write("\n**Missing Values Before Cleaning**\n")
    f.write(before_nulls.to_string())
    f.write("\n\n")

    f.write("\n**Missing Values After Cleaning**\n")
    f.write(after_nulls.to_string())
    f.write("\n\n")

    f.write("\n**Validity Rules Applied**\n")
    f.write("- temperature_c: 10–35°C\n")
    f.write("- humidity_pct: 50–100%\n")
    f.write("- co2_ppm: 400–2000 ppm\n\n")

    f.write("\n**Strategy**\n")
    f.write("- Forward-fill sensor columns (limit=2)\n")
    f.write("- Never impute yield_kg\n")
    f.write("- Remove duplicate timestamps using keep='last'\n")
    f.write("- Flag outliers using is_outlier column\n\n")

    f.write("\n**Output Files**\n")
    f.write(f"- Audit dataset: {audit_path}\n")
    f.write(f"- Clean dataset: {clean_path}\n")
    
    f.write("\n**Row Removal Summary**\n")
    f.write(f"Rows before cleaning: {initial_rows}\n")
    f.write(f"Rows after cleaning: {final_rows}\n")
    f.write(f"Rows dropped: {rows_dropped}\n")
    f.write(f"Percentage dropped: {drop_pct:.2f}%\n")
    print(f"\nRows before cleaning: {initial_rows}")
    print(f"Rows after cleaning: {final_rows}")
    print(f"Rows dropped: {rows_dropped} ({drop_pct:.2f}%)")

if drop_pct > 10:
    print("WARNING: More than 10% of rows were removed. Investigate before modeling.")
print("\nCleaning log saved →", log_path)
print("\nSaved:")
print("Audit dataset →", audit_path)
print("Clean dataset →", clean_path)