import pandas as pd
from pathlib import Path

# ----------------------------
# Load Data
# ----------------------------

df = pd.read_parquet("data/interim/01_loaded.parquet")

initial_rows = len(df)

# ----------------------------
# Missing Value Report
# ----------------------------

before_nulls = df.isna().sum()
before_null_pct = (before_nulls / len(df)) * 100

print("\n=== INITIAL MISSING VALUES ===")
print(before_nulls)

print("\n=== INITIAL MISSING PERCENTAGES (%) ===")
print(before_null_pct.round(2))

# ----------------------------
# Duplicate Report
# ----------------------------

duplicate_count = df.duplicated(
    subset=["timestamp"]
).sum()

print(f"\nDuplicate timestamps found: {duplicate_count}")

# ----------------------------
# Missing Value Handling
# ----------------------------

sensor_cols = [
    "temperature_c",
    "humidity_pct",
    "co2_ppm"
]

# Forward-fill short sensor gaps
df[sensor_cols] = df[sensor_cols].ffill(limit=2)

# Remove rows still missing sensor values
sensor_missing_before_drop = len(df)

df = df.dropna(subset=sensor_cols)

sensor_rows_removed = (
    sensor_missing_before_drop - len(df)
)

# Never impute target
yield_missing_before_drop = len(df)

df = df.dropna(subset=["yield_kg"])

yield_rows_removed = (
    yield_missing_before_drop - len(df)
)

# ----------------------------
# Outlier Detection
# ----------------------------

df["is_outlier"] = ~(
    df["temperature_c"].between(10, 35) &
    df["humidity_pct"].between(50, 100) &
    df["co2_ppm"].between(400, 2000)
)

outlier_count = df["is_outlier"].sum()

print(f"\nOutliers detected: {outlier_count}")

# ----------------------------
# Duplicate Removal
# ----------------------------

rows_before_duplicates = len(df)

df = df.drop_duplicates(
    subset=["timestamp"],
    keep="last"
)

duplicate_rows_removed = (
    rows_before_duplicates - len(df)
)

# ----------------------------
# Save Audit Dataset
# ----------------------------

audit_path = Path(
    "data/interim/02_with_outliers.parquet"
)

df.to_parquet(
    audit_path,
    index=False
)

# ----------------------------
# Remove Outliers For Modeling
# ----------------------------

df_clean = df[~df["is_outlier"]].copy()

# ----------------------------
# Final Counts
# ----------------------------

final_rows = len(df_clean)

rows_dropped = initial_rows - final_rows

drop_pct = (
    rows_dropped / initial_rows
) * 100

# ----------------------------
# Final Missing Check
# ----------------------------

after_nulls = df_clean.isna().sum()
after_null_pct = (
    after_nulls / len(df_clean)
) * 100

print("\n=== FINAL NULL CHECK ===")
print(after_nulls)

print("\n=== FINAL NULL PERCENTAGES (%) ===")
print(after_null_pct.round(2))

print("\nFinal shape:", df_clean.shape)

print(f"\nRows before cleaning: {initial_rows}")
print(f"Rows after cleaning: {final_rows}")
print(
    f"Rows dropped: {rows_dropped} "
    f"({drop_pct:.2f}%)"
)

if drop_pct > 10:
    print(
        "\nWARNING: More than 10% of rows "
        "were removed. Investigate before modeling."
    )

# ----------------------------
# Save Clean Dataset
# ----------------------------

processed_dir = Path("data/processed")
processed_dir.mkdir(
    parents=True,
    exist_ok=True
)

clean_path = (
    processed_dir / "02_cleaned.parquet"
)

df_clean.to_parquet(
    clean_path,
    index=False
)

# Optional sample file
sample_path = (
    processed_dir /
    "cleaned_sample_50_rows.csv"
)

df_clean.head(50).to_csv(
    sample_path,
    index=False
)

# ----------------------------
# Cleaning Log
# ----------------------------

log_path = Path(
    "docs/cleaning_log.md"
)

log_path.parent.mkdir(
    exist_ok=True
)

with open(
    log_path,
    "w",
    encoding="utf-8"
) as f:

    f.write("# Cleaning Log - Task 2\n\n")

    f.write("## Missing Values Before Cleaning\n")
    f.write(before_nulls.to_string())
    f.write("\n\n")

    f.write(
        "## Missing Value Percentages Before Cleaning (%)\n"
    )
    f.write(before_null_pct.round(2).to_string())
    f.write("\n\n")

    f.write("## Missing Values After Cleaning\n")
    f.write(after_nulls.to_string())
    f.write("\n\n")

    f.write(
        "## Missing Value Percentages After Cleaning (%)\n"
    )
    f.write(after_null_pct.round(2).to_string())
    f.write("\n\n")

    f.write("## Validity Rules Applied\n")
    f.write("- temperature_c: 10–35°C\n")
    f.write("- humidity_pct: 50–100%\n")
    f.write("- co2_ppm: 400–2000 ppm\n\n")

    f.write("## Agritech Cleaning Rationale\n")
    f.write(
        "- Temperature, humidity and CO₂ are "
        "sensor measurements.\n"
    )
    f.write(
        "- Short sensor outages (≤2 readings) "
        "are forward-filled.\n"
    )
    f.write(
        "- Longer outages are removed because "
        "sensor conditions are unknown.\n"
    )
    f.write(
        "- yield_kg is never imputed to avoid "
        "creating artificial labels.\n\n"
    )

    f.write("## Duplicate Handling\n")
    f.write(
        f"- Duplicate timestamps detected: "
        f"{duplicate_count}\n"
    )
    f.write(
        f"- Duplicate rows removed: "
        f"{duplicate_rows_removed}\n\n"
    )

    f.write("## Outlier Review\n")
    f.write(
        f"- Outliers flagged: "
        f"{outlier_count}\n"
    )
    f.write(
        "- Outliers retained in audit dataset "
        "and removed from modeling dataset.\n\n"
    )

    f.write("## Row Removal Summary\n")
    f.write(
        f"- Rows before cleaning: "
        f"{initial_rows}\n"
    )
    f.write(
        f"- Rows after cleaning: "
        f"{final_rows}\n"
    )
    f.write(
        f"- Rows dropped: "
        f"{rows_dropped}\n"
    )
    f.write(
        f"- Percentage dropped: "
        f"{drop_pct:.2f}%\n\n"
    )

    f.write("## Output Files\n")
    f.write(
        f"- Audit dataset: "
        f"{audit_path}\n"
    )
    f.write(
        f"- Clean dataset: "
        f"{clean_path}\n"
    )
    f.write(
        f"- Sample file: "
        f"{sample_path}\n"
    )

print("\nCleaning log saved →", log_path)

print("\nSaved:")
print("Audit dataset →", audit_path)
print("Clean dataset →", clean_path)
print("Sample file →", sample_path)