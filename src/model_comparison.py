import pandas as pd
import matplotlib.pyplot as plt
import joblib

# Load test data
test_df = pd.read_parquet(
    "data/processed/test_features.parquet"
)

X_test = test_df.drop(
    columns=["yield_kg"]
)
y_test = test_df["yield_kg"]

# Load champion model
model = joblib.load(
    "models/linear_regression.joblib"
)

pred = model.predict(X_test)

plt.figure(figsize=(6,6))

plt.scatter(
    y_test,
    pred,
    alpha=0.6
)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    "r--"
)

plt.xlabel("Actual Yield (kg)")
plt.ylabel("Predicted Yield (kg)")
plt.title("Predicted vs Actual Yield")

plt.tight_layout()

plt.savefig(
    "reports/figures/pred_vs_actual_linear.png",
    dpi=150
)

print("Saved:")
print("reports/figures/pred_vs_actual_linear.png")