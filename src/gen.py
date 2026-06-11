import pandas as pd
import numpy as np

# ----------------------------
# Configuration
# ----------------------------
NUM_ROWS = 1000
START_DATE = "2023-01-01 00:00:00"

np.random.seed(42)

# ----------------------------
# Generate timestamps
# ----------------------------
timestamps = pd.date_range(
    start="2023-01-01",
    periods=NUM_ROWS,
    freq="D"
)

# ----------------------------
# Temperature (°C)
# ----------------------------
day_of_year = timestamps.dayofyear.values

temperature = (
    22
    + 3 * np.sin(2 * np.pi * day_of_year / 365)
    + np.random.normal(0, 0.8, NUM_ROWS)
)

temperature = np.clip(temperature, 15, 28)

# ----------------------------
# Humidity (%)
# ----------------------------
humidity = (
    90
    - 4 * np.sin(2 * np.pi * day_of_year / 365)
    + np.random.normal(0, 1.5, NUM_ROWS)
)
humidity = np.clip(humidity, 82, 98)

# ----------------------------
# CO₂ (ppm)
# ----------------------------
co2 = (
    950
    + 120 * np.sin(2 * np.pi * day_of_year / 365)
    + np.random.normal(0, 60, NUM_ROWS)
)

# Ventilation events
ventilation_idx = np.random.choice(
    NUM_ROWS,
    size=int(NUM_ROWS * 0.03),
    replace=False
)

co2[ventilation_idx] -= 400

co2 = np.clip(co2, 400, 1800)

# ----------------------------
# Yield generation
# ----------------------------
#
# Mushrooms perform best near:
# 22°C
# 90% humidity
# 1000 ppm CO₂
#
# Environmental score
#

temp_score = 1 - (np.abs(temperature - 22) / 10)
hum_score = 1 - (np.abs(humidity - 90) / 15)
co2_score = 1 - (np.abs(co2 - 1000) / 1200)

temp_score = np.clip(temp_score, 0, 1)
hum_score = np.clip(hum_score, 0, 1)
co2_score = np.clip(co2_score, 0, 1)

environment_score = (
    0.40 * temp_score
    + 0.30 * hum_score
    + 0.30 * co2_score
)

# Daily yield (kg)
yield_kg = (
    6
    + 10 * environment_score
    + np.random.normal(0, 0.4, NUM_ROWS)
)

yield_kg = np.clip(yield_kg, 2, 20)

# Occasional growth pauses
pause_idx = np.random.choice(
    NUM_ROWS,
    size=int(NUM_ROWS * 0.02),
    replace=False
)

yield_kg[pause_idx] *= 0.7
# ----------------------------
# Missing values
# ----------------------------

def add_missing(data, percent):
    data = data.copy()
    idx = np.random.choice(
        len(data),
        size=int(len(data) * percent),
        replace=False
    )
    data[idx] = np.nan
    return data

temperature = add_missing(temperature, 0.05)
humidity = add_missing(humidity, 0.04)
co2 = add_missing(co2, 0.03)

# ----------------------------
# Outliers
# ----------------------------

outlier_idx = np.random.choice(
    NUM_ROWS,
    size=int(NUM_ROWS * 0.01),
    replace=False
)

temperature[outlier_idx] += np.random.uniform(10, 15, len(outlier_idx))

# ----------------------------
# Create DataFrame
# ----------------------------

df = pd.DataFrame({
    "timestamp": timestamps,
    "temperature_c": np.round(temperature, 2),
    "humidity_pct": np.round(humidity, 2),
    "co2_ppm": np.round(co2, 0),
    "yield_kg": np.round(yield_kg, 3)
})

duplicate_rows = df.sample(
    n=15,
    random_state=42
)

df = pd.concat(
    [df, duplicate_rows],
    ignore_index=True
)
 
# ----------------------------
# Save CSV
# ----------------------------

df.to_csv(
    "data/raw/mushroom_polyhouse_raw_data.csv",
    index=False
)
print("Dataset created successfully.")
print(f"Rows: {len(df)}")
print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())