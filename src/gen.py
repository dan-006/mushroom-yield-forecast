import numpy as np
import pandas as pd
from pathlib import Path

# ----------------------------
# Configuration
# ----------------------------

rng = np.random.default_rng(42)
n = 1000

# ----------------------------
# Generate timestamps
# ----------------------------

timestamps = pd.date_range(
    start="2023-01-01",
    periods=n,
    freq="D"
)

# ----------------------------
# Sensor Data
# ----------------------------

temp = rng.normal(22, 1.5, n)
hum = np.clip(
    rng.normal(87, 3, n),
    75,
    98
)
co2 = rng.normal(900, 80, n)

# ----------------------------
# Yield Generation
# ----------------------------

yield_kg = (
    8
    + 0.3 * temp
    + 0.05 * hum
    - 0.002 * co2
    + rng.normal(0, 0.5, n)
)

# ----------------------------
# Create DataFrame
# ----------------------------

df = pd.DataFrame({
    "timestamp": timestamps,
    "temperature_c": temp.round(2),
    "humidity_pct": hum.round(1),
    "co2_ppm": co2.round(0),
    "yield_kg": yield_kg.round(2),
})

# ==================================================
# Add Missing Values (~5%)
# ==================================================

for col in [
    "temperature_c",
    "humidity_pct",
    "co2_ppm"
]:
    missing_idx = rng.choice(
        df.index,
        size=50,
        replace=False
    )

    df.loc[missing_idx, col] = np.nan

# ==================================================
# Add Outliers (~2%)
# ==================================================

outlier_idx = rng.choice(
    df.index,
    size=20,
    replace=False
)

df.loc[outlier_idx[:7], "temperature_c"] = (
    df.loc[outlier_idx[:7], "temperature_c"] * 2
)

df.loc[outlier_idx[7:14], "humidity_pct"] = (
    df.loc[outlier_idx[7:14], "humidity_pct"] + 40
)

df.loc[outlier_idx[14:], "co2_ppm"] = (
    df.loc[outlier_idx[14:], "co2_ppm"] * 3
)

# ==================================================
# Add Duplicates (~1%)
# ==================================================

duplicate_rows = df.sample(
    n=10,
    random_state=42
)

df = pd.concat(
    [df, duplicate_rows],
    ignore_index=True
)

# ==================================================
# Save
# ==================================================

Path("data/raw").mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    "data/raw/mushroom_polyhouse_raw_data.csv",
    index=False
)

# ==================================================
# Summary
# ==================================================

print("Dataset created successfully.")
print("\nShape:", df.shape)

print("\nMissing Values:")
print(df.isna().sum())

print("\nDuplicate Rows:",
      df.duplicated().sum())

print("\nSample:")
print(df.head())