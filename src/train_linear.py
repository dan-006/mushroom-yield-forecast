import pandas as pd
import numpy as np
import joblib
import json
import matplotlib.pyplot as plt
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

pred_test = model.predict(X_test)
pred_train = model.predict(X_train)

residuals = y_test - pred_test

train_residuals = y_train - pred_train
test_residuals = y_test - pred_test

print(
    "\nMean Absolute Train Residual:",
    abs(train_residuals).mean()
)

print(
    "Mean Absolute Test Residual:",
    abs(test_residuals).mean()
)

mae = mean_absolute_error(y_test, pred_test)
rmse = np.sqrt(mean_squared_error(y_test, pred_test))
r2 = r2_score(y_test, pred_test)

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

plt.figure(figsize=(6, 4))

plt.scatter(
    pred_test,
    residuals,
    alpha=0.5
)

plt.axhline(
    y=0,
    color="red",
    linestyle="--"
)

plt.xlabel("Predicted Yield (kg)")
plt.ylabel("Residual (kg)")
plt.title("Residuals vs Predicted Yield")

plt.tight_layout()

plt.savefig(
    "reports/figures/residuals_vs_predicted_linear.png",
    dpi=150
)

plt.close()

humidity_feature = X_test.iloc[:, 1]

plt.figure(figsize=(6, 4))

plt.scatter(
    humidity_feature,
    residuals,
    alpha=0.5
)

plt.axhline(
    y=0,
    color="red",
    linestyle="--"
)

plt.xlabel("Scaled Humidity")
plt.ylabel("Residual (kg)")
plt.title("Residuals vs Humidity")

plt.tight_layout()

plt.savefig(
    "reports/figures/residuals_vs_humidity_linear.png",
    dpi=150
)

plt.close()

print("\nSaved:")
print("models/linear_regression.joblib")
print("reports/metrics_linear.json")