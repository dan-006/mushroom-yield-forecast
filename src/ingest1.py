import pandas as pd
from pathlib import Path

RAW = Path("data/raw/mushroom_polyhouse_raw_data.csv")
INTERIM = Path("data/interim")
INTERIM.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = INTERIM / "01_loaded.parquet"

df = pd.read_csv(
    RAW,
    parse_dates=["timestamp"],
)

print("\nShape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

print("\nInfo:")
df.info()

print("\nSummary Statistics:")
print(df.describe())

df.to_parquet(OUTPUT_FILE, index=False)

print("\nSnapshot saved:")
print(OUTPUT_FILE)
