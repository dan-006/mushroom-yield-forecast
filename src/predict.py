import json
import joblib
import pandas as pd
from pathlib import Path
from src.logger import log_prediction

MODEL_DIR = Path("models")

scaler = joblib.load(
    MODEL_DIR / "minmax_scaler_train.joblib"
)

model = joblib.load(
    MODEL_DIR / "linear_regression.joblib"
)

with open(MODEL_DIR / "feature_cols.json") as f:
    feature_cols = json.load(f)


def predict_yield(
    temperature_c: float,
    humidity_pct: float,
    co2_ppm: float
) -> float:

    temp_humid_interaction = (
        temperature_c * humidity_pct / 100
    )

    raw = pd.DataFrame(
        [[
            temperature_c,
            humidity_pct,
            co2_ppm,
            temp_humid_interaction
        ]],
        columns=[
            "temperature_c",
            "humidity_pct",
            "co2_ppm",
            "temp_humid_interaction"
        ]
    )

    scaled = scaler.transform(raw)
    scaled = pd.DataFrame(
    scaled,
    columns=[
        "temperature_c_scaled",
        "humidity_pct_scaled",
        "co2_ppm_scaled",
        "temp_humid_interaction_scaled"
    ]
    )

    prediction = float(model.predict(scaled)[0])

    log_prediction(
        temperature_c,
        humidity_pct,
    	co2_ppm,
    	prediction
	)

    return prediction


if __name__ == "__main__":
    pred = predict_yield(
        22.0,
        88.0,
        920
    )

    print(f"Predicted yield: {pred:.2f} kg")