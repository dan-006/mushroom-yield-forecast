import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib
from pathlib import Path

# Load cleaned dataset
df = pd.read_parquet("data/processed/02_cleaned.parquet")

# Sort by timestamp
df = df.sort_values("timestamp").reset_index(drop=True)

# --------------------------------------------------
# Engineered Feature
# --------------------------------------------------
# Interaction between temperature and humidity. Higher humidity at suitable temperatures may support mushroom growth better than either variable alone.

df["temp_humid_interaction"] = (
    df["temperature_c"] * df["humidity_pct"] / 100
)

# --------------------------------------------------
# Feature Matrix (X) and Target (y)
# --------------------------------------------------

feature_cols = [
    "temperature_c",
    "humidity_pct",
    "co2_ppm",
    "temp_humid_interaction"
]

X = df[feature_cols]
y = df["yield_kg"]

print("X shape:", X.shape)
print("y shape:", y.shape)

# --------------------------------------------------
# Scaling
# --------------------------------------------------

scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)

# Save scaler
Path("models").mkdir(exist_ok=True)

joblib.dump(
    scaler,
    "models/minmax_scaler.joblib"
)

# Convert back to DataFrame
scaled_df = pd.DataFrame(
    X_scaled,
    columns=[c + "_scaled" for c in feature_cols]
)

scaled_df["yield_kg"] = y.values

# ----------------------------
# VALIDATION CHECKS
# ----------------------------
assert scaled_df[scaled_df.columns[:-1]].min().min() >= -1e-9
assert scaled_df[scaled_df.columns[:-1]].max().max() <= 1 + 1e-9

# Save processed features
Path("data/processed").mkdir(
    parents=True,
    exist_ok=True
)

scaled_df.to_parquet(
    "data/processed/features.parquet",
    index=False
)

print("\nFeature ranges:")

for col in scaled_df.columns[:-1]:
    print(
        col,
        "min=",
        scaled_df[col].min(),
        "max=",
        scaled_df[col].max()
    )

print("\nNo missing values:")
print(scaled_df.isna().sum())

print("\nSaved:")
print("models/minmax_scaler.joblib")
print("data/processed/features.parquet")