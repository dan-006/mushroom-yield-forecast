import pandas as pd
import numpy as np
import joblib
import json
from pathlib import Path

from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ---------------------------------
# Load train/test data
# ---------------------------------

train_df = pd.read_parquet(
    "data/processed/train_features.parquet"
)

test_df = pd.read_parquet(
    "data/processed/test_features.parquet"
)

# ---------------------------------
# Split X and y
# ---------------------------------

X_train = train_df.drop(columns=["yield_kg"])
y_train = train_df["yield_kg"]

X_test = test_df.drop(columns=["yield_kg"])
y_test = test_df["yield_kg"]

# ---------------------------------
# Train model
# ---------------------------------

model = LinearRegression()

model.fit(X_train, y_train)

# ---------------------------------
# Predictions
# ---------------------------------

pred_train = model.predict(X_train)
pred_test = model.predict(X_test)

# ---------------------------------
# Metrics
# ---------------------------------

mae = mean_absolute_error(
    y_test,
    pred_test
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        pred_test
    )
)

r2 = r2_score(
    y_test,
    pred_test
)

# ---------------------------------
# Print metrics
# ---------------------------------

print("\nLinear Regression Results")
print("-------------------------")
print(f"Test MAE:  {mae:.3f} kg")
print(f"Test RMSE: {rmse:.3f} kg")
print(f"Test R²:   {r2:.3f}")

# ---------------------------------
# Coefficients
# ---------------------------------

print("\nFeature Coefficients")

for feature, coef in zip(
    X_train.columns,
    model.coef_
):
    print(f"{feature}: {coef:.4f}")

# ---------------------------------
# Save model
# ---------------------------------

Path("models").mkdir(
    parents=True,
    exist_ok=True
)

joblib.dump(
    model,
    "models/linear_regression.joblib"
)

# ---------------------------------
# Save metrics
# ---------------------------------

metrics = {
    "mae": float(mae),
    "rmse": float(rmse),
    "r2": float(r2)
}

Path("reports").mkdir(
    parents=True,
    exist_ok=True
)

with open(
    "reports/metrics_linear.json",
    "w"
) as f:
    json.dump(
        metrics,
        f,
        indent=4
    )

print("\nSaved:")
print("models/linear_regression.joblib")
print("reports/metrics_linear.json")