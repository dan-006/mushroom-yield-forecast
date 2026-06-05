import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load cleaned data
df = pd.read_parquet("data/processed/02_cleaned.parquet")

# Create figures folder
Path("reports/figures").mkdir(parents=True, exist_ok=True)

# --------------------------
# Correlation Heatmap
# --------------------------

features = [
    "temperature_c",
    "humidity_pct",
    "co2_ppm",
    "yield_kg"
]

corr = df[features].corr()

fig, ax = plt.subplots(figsize=(6, 5))

im = ax.imshow(
    corr,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

ax.set_xticks(range(len(features)))
ax.set_xticklabels(features, rotation=45, ha="right")

ax.set_yticks(range(len(features)))
ax.set_yticklabels(features)

ax.set_title("Sensor & Yield Correlations")

fig.colorbar(
    im,
    ax=ax,
    label="Pearson Correlation"
)

plt.tight_layout()

plt.savefig(
    "reports/figures/corr_heatmap.png",
    dpi=150
)

plt.close()

# --------------------------
# Humidity vs Yield
# --------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    df["humidity_pct"],
    df["yield_kg"],
    alpha=0.5,
    s=15
)

plt.xlabel("Humidity (%)")
plt.ylabel("Yield (kg)")
plt.title("Humidity vs Yield")

plt.tight_layout()

plt.savefig(
    "reports/figures/humidity_vs_yield.png",
    dpi=150
)

plt.close()

# --------------------------
# Temperature vs Yield
# --------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    df["temperature_c"],
    df["yield_kg"],
    alpha=0.5,
    s=15
)

plt.xlabel("Temperature (°C)")
plt.ylabel("Yield (kg)")
plt.title("Temperature vs Yield")

plt.tight_layout()

plt.savefig(
    "reports/figures/temperature_vs_yield.png",
    dpi=150
)

plt.close()

# --------------------------
# CO2 vs Yield
# --------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    df["co2_ppm"],
    df["yield_kg"],
    alpha=0.5,
    s=15
)

plt.xlabel("CO₂ (ppm)")
plt.ylabel("Yield (kg)")
plt.title("CO₂ vs Yield")

plt.tight_layout()

plt.savefig(
    "reports/figures/co2_vs_yield.png",
    dpi=150
)

plt.close()

print("EDA figures saved to reports/figures/")