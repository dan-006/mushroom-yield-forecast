from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import pandas as pd
import numpy as np
import json
import joblib
import time

# -----------------------------
# Load train/test data
# -----------------------------

train = pd.read_parquet(
    "data/processed/train_features.parquet"
)

test = pd.read_parquet(
    "data/processed/test_features.parquet"
)

feature_cols = [
    "temperature_c_scaled",
    "humidity_pct_scaled",
    "co2_ppm_scaled",
    "temp_humid_interaction_scaled"
]

X_train = train[feature_cols]
y_train = train["yield_kg"]

X_test = test[feature_cols]
y_test = test["yield_kg"]

# -----------------------------
# Time Series CV
# -----------------------------

tscv = TimeSeriesSplit(n_splits=3)

# -----------------------------
# Parameter Grid
# -----------------------------

param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 5, 10],
    "min_samples_leaf": [1, 3, 5]
}

rf = RandomForestRegressor(
    random_state=42,
    n_jobs=-1
)

# -----------------------------
# Grid Search
# -----------------------------

search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=tscv,
    scoring="neg_mean_absolute_error",
    n_jobs=-1,
    refit=True,
    verbose=1
)

start_time = time.time()
search.fit(X_train, y_train)
end_time = time.time()

runtime_seconds = end_time - start_time

print(f"Runtime: {runtime_seconds:.2f} seconds")

# -----------------------------
# Best Results
# -----------------------------

print("\nBest Parameters")
print(search.best_params_)

print(
    "\nBest CV MAE:",
    -search.best_score_
)

# -----------------------------
# Evaluate on Test Set
# -----------------------------

best_model = search.best_estimator_

pred = best_model.predict(X_test)

mae = mean_absolute_error(
    y_test,
    pred
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        pred
    )
)

r2 = r2_score(
    y_test,
    pred
)

print("\nTuned RF Results")
print("----------------")
print(f"MAE:  {mae:.3f}")
print(f"RMSE: {rmse:.3f}")
print(f"R²:   {r2:.3f}")

# -----------------------------
# Save model
# -----------------------------

joblib.dump(
    best_model,
    "models/random_forest_tuned.joblib"
)

# -----------------------------
# Save params
# -----------------------------

with open(
    "models/rf_best_params.json",
    "w"
) as f:
    json.dump(
        search.best_params_,
        f,
        indent=2
    )

# -----------------------------
# Save CV results
# -----------------------------

results = pd.DataFrame(
    search.cv_results_
)

results.to_csv(
    "reports/rf_gridsearch_results.csv",
    index=False
)

print("\nSaved:")
print("models/random_forest_tuned.joblib")
print("models/rf_best_params.json")
print("reports/rf_gridsearch_results.csv")