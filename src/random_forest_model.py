import pandas as pd
import numpy as np
import json
import joblib
import matplotlib.pyplot as plt

from pathlib import Path

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# -------------------------------
# Load datasets
# -------------------------------

train_df = pd.read_parquet(
    "data/processed/train_features.parquet"
)

test_df = pd.read_parquet(
    "data/processed/test_features.parquet"
)

X_train = train_df.drop(
    columns=["yield_kg"]
)

y_train = train_df["yield_kg"]

X_test = test_df.drop(
    columns=["yield_kg"]
)

y_test = test_df["yield_kg"]

# -------------------------------
# Train model
# -------------------------------

rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

rf.fit(
    X_train,
    y_train
)

# -------------------------------
# Predictions
# -------------------------------

pred_test = rf.predict(X_test)

# -------------------------------
# Metrics
# -------------------------------

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

print("\nRandom Forest Results")
print("---------------------")

print(
    f"Test MAE:  {mae:.3f} kg"
)

print(
    f"Test RMSE: {rmse:.3f} kg"
)

print(
    f"Test R²:   {r2:.3f}"
)

metrics = {
    "mae": float(mae),
    "rmse": float(rmse),
    "r2": float(r2)
}

Path("reports").mkdir(
    exist_ok=True
)

with open(
    "reports/metrics_random_forest.json",
    "w"
) as f:
    json.dump(
        metrics,
        f,
        indent=4
    )

Path("models").mkdir(
    exist_ok=True
)

joblib.dump(
    rf,
    "models/random_forest.joblib"
)

# -------------------------------
# Feature Importances
# -------------------------------

importances = rf.feature_importances_

feature_names = X_train.columns

importance_df = pd.DataFrame({
    "feature": feature_names,
    "importance": importances
})

importance_df = importance_df.sort_values(
    "importance"
)

Path(
    "reports/figures"
).mkdir(
    parents=True,
    exist_ok=True
)

plt.figure(figsize=(8, 5))

plt.barh(
    importance_df["feature"],
    importance_df["importance"]
)

plt.xlabel("Importance")
plt.title(
    "Random Forest Feature Importance"
)

plt.tight_layout()

plt.savefig(
    "reports/figures/rf_feature_importance.png",
    dpi=150
)

plt.close()

with open(
    "reports/metrics_linear.json"
) as f:
    linear_metrics = json.load(f)

print("\nComparison")
print("----------")

print(
    f"Linear R²: {linear_metrics['r2']:.3f}"
)

print(
    f"RF R²:     {r2:.3f}"
)