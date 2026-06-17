import csv
from datetime import datetime, timezone
from pathlib import Path

LOG_PATH = Path("logs/predictions.csv")


def log_prediction(temp, humidity, co2, predicted_kg):
    LOG_PATH.parent.mkdir(exist_ok=True)

    write_header = not LOG_PATH.exists()

    with LOG_PATH.open("a", newline="") as f:
        writer = csv.writer(f)

        if write_header:
            writer.writerow([
                "timestamp_utc",
                "temperature_c",
                "humidity_pct",
                "co2_ppm",
                "predicted_kg"
            ])

        writer.writerow([
            datetime.now(timezone.utc).isoformat(),
            temp,
            humidity,
            co2,
            round(predicted_kg, 3)
        ])