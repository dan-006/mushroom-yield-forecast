import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import (
    TimeSeriesSplit,
    cross_val_score
)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

train_df = pd.read_parquet(
    "data/processed/train_features.parquet"
)

X_train = train_df.drop(
    columns=["yield_kg"]
)

y_train = train_df["yield_kg"]

tscv = TimeSeriesSplit(
    n_splits=5
)

lin = LinearRegression()

rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

lin_scores = cross_val_score(
    lin,
    X_train,
    y_train,
    cv=tscv,
    scoring="neg_mean_absolute_error"
)

rf_scores = cross_val_score(
    rf,
    X_train,
    y_train,
    cv=tscv,
    scoring="neg_mean_absolute_error"
)

lin_mae = -lin_scores
rf_mae = -rf_scores

print(
    "\nLinear CV MAE:"
)

print(
    lin_mae
)

print(
    "\nRF CV MAE:"
)

print(
    rf_mae
)

print(
    "\nLinear Mean CV MAE:",
    lin_mae.mean()
)

print(
    "Linear Std CV MAE:",
    lin_mae.std()
)

print(
    "\nRF Mean CV MAE:",
    rf_mae.mean()
)

print(
    "RF Std CV MAE:",
    rf_mae.std()
)
models = ["Linear", "Random Forest"]
mae = [
    (-lin_scores).mean(),
    (-rf_scores).mean()
]

plt.figure(figsize=(6, 4))
plt.bar(models, mae)
plt.ylabel("Mean CV MAE (kg)")
plt.title("Cross-Validation Comparison")
plt.tight_layout()

plt.savefig(
    "reports/figures/cv_mae_comparison.png",
    dpi=150
)

print("Saved: reports/figures/cv_mae_comparison.png")