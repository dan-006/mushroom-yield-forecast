import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib
from pathlib import Path

# Load cleaned data
df = pd.read_parquet(
    "data/processed/02_cleaned.parquet"
)

# Sort chronologically
df = df.sort_values("timestamp")

# Feature engineering
df["temp_humid_interaction"] = (
    df["temperature_c"] * df["humidity_pct"] / 100
)

feature_cols = [
    "temperature_c",
    "humidity_pct",
    "co2_ppm",
    "temp_humid_interaction"
]

# -------------------------------
# Chronological Split
# -------------------------------

split_idx = int(len(df) * 0.8)

train = df.iloc[:split_idx]
test = df.iloc[split_idx:]

print("\nTrain period:")
print(train["timestamp"].min(), "->",
      train["timestamp"].max())

print("\nTest period:")
print(test["timestamp"].min(), "->",
      test["timestamp"].max())

# -------------------------------
# X and y
# -------------------------------

X_train = train[feature_cols]
X_test = test[feature_cols]

y_train = train["yield_kg"]
y_test = test["yield_kg"]

# -------------------------------
# Leak-free scaling
# -------------------------------

scaler = MinMaxScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

# Save scaler
Path("models").mkdir(exist_ok=True)

joblib.dump(
    scaler,
    "models/minmax_scaler_train.joblib"
)

# -------------------------------
# Save processed splits
# -------------------------------

train_df = pd.DataFrame(
    X_train_scaled,
    columns=[c + "_scaled" for c in feature_cols]
)

train_df["yield_kg"] = y_train.values

test_df = pd.DataFrame(
    X_test_scaled,
    columns=[c + "_scaled" for c in feature_cols]
)

test_df["yield_kg"] = y_test.values

Path("data/processed").mkdir(
    parents=True,
    exist_ok=True
)

train_df.to_parquet(
    "data/processed/train_features.parquet",
    index=False
)

test_df.to_parquet(
    "data/processed/test_features.parquet",
    index=False
)

# -------------------------------
# Summary
# -------------------------------

print("\nTrain size:", len(train_df))
print("Test size:", len(test_df))

print("\nNo missing values for trained dataset:")
print(train_df.isna().sum())
print("\nNo missing values for test dataset:")
print(test_df.isna().sum())

print("\nSaved:")
print("models/minmax_scaler_train.joblib")
print("data/processed/train_features.parquet")
print("data/processed/test_features.parquet")