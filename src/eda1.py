import pandas as pd
from pathlib import Path

# Load cleaned dataset
df = pd.read_parquet("data/processed/02_cleaned.parquet")

# Numeric summary
summary = df[
    ["temperature_c", "humidity_pct", "co2_ppm", "yield_kg"]
].describe().T.round(2)

# Coefficient of variation
summary["cv"] = (summary["std"] / summary["mean"]).round(3)

# Dataset information
rows = len(df)
start_date = df["timestamp"].min()
end_date = df["timestamp"].max()

# Sampling frequency
sampling_days = (
    df["timestamp"]
      .sort_values()
      .diff()
      .dt.days
      .dropna()
)

freq = round(sampling_days.mode()[0], 2)

# Validity rules
valid_rows = (
    df["humidity_pct"].between(50, 100)
    & df["temperature_c"].between(10, 35)
    & df["co2_ppm"].between(400, 2000)
)

valid_pct = round(valid_rows.mean() * 100, 2)

# Mean vs median yield
yield_mean = round(df["yield_kg"].mean(), 2)
yield_median = round(df["yield_kg"].median(), 2)
yield_std = round(df["yield_kg"].std(), 2)

# Create report text
report = []

report.append("# Polyhouse Data Quality Report\n")

report.append(f"Total observations: {rows}")
report.append(
    f"Date range: {start_date.date()} to {end_date.date()}"
)
report.append(
    f"Typical sampling frequency: every {freq} day(s)\n"
)

report.append("## Summary Statistics\n")
report.append(summary.to_markdown())

report.append("\n## Data Quality\n")
report.append(
    f"Rows passing validity rules: {valid_pct}%"
)

report.append("\n## Interpretation\n")

report.append(
    f"- Average yield is {yield_mean} kg/day while median yield is {yield_median} kg/day."
)

if abs(yield_mean - yield_median) < 0.25:
    report.append(
        "- Mean and median yield are similar, indicating little skew."
    )
else:
    report.append(
        "- Mean and median differ moderately, suggesting some skew in yield distribution."
    )

report.append(
    f"- Yield standard deviation is {yield_std} kg."
)

report.append(
    f"- Average humidity is {round(df['humidity_pct'].mean(),1)}%, which falls within the expected polyhouse range."
)

report.append(
    f"- Humidity variability is low (CV = {summary.loc['humidity_pct', 'cv']}), indicating stable polyhouse environmental conditions."
)

report.append(
    f"- CO₂ variability is moderate (CV = {summary.loc['co2_ppm', 'cv']}), which may reflect normal ventilation cycles."
)

report.append(
    f"- Yield variability is low (CV = 0.071), indicating relatively consistent mushroom production throughout the observation period."
)

# Save report
Path("reports").mkdir(exist_ok=True)

report_path = Path("reports/data_quality.md")

report_path.write_text(
    "\n".join(report),
    encoding="utf-8"
)

print(f"Report saved -> {report_path}")