# Mushroom Yield Forecast Project

## Problem Statement

Predict daily mushroom yield (kg) in a climate-controlled polyhouse using temperature, humidity, and CO₂ sensor readings.

The goal is to build a machine learning pipeline that estimates mushroom yield from sensor readings.

## Environment Setup

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate virtual environment

#### Windows CMD

```bash
venv\Scripts\activate
```

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Project Structure

```text
Dan Intern/
|
|-- data/
|   |-- raw/
|
|-- models/
|
|-- notebooks/
|
|-- src/
|   |-- smoke_test.py
|
|-- requirements.txt
|-- README.md
|-- .gitignore
```

## Smoke Test

Run:

```bash
python src\smoke_test.py
```

Expected Output:

```text
Polyhouse sensor snapshot:
...

Environment OK.
```

## Folder Map

```text
data/raw      -> Raw sensor CSV files
notebooks     -> Jupyter notebooks
src           -> Python scripts
models        -> Trained models
```

## Champion Model

Linear Regression was selected as the champion model because it achieved the best performance on the held-out test set while remaining simple and highly interpretable.

## Run Inference

Load the trained model and generate a mushroom yield prediction:

```bash
python src/predict.py
```

Example output:

```text
Predicted yield: 17.24 kg
```

Example usage inside Python:

```python
from src.predict import predict_yield

prediction = predict_yield(
    temperature_c=22.0,
    humidity_pct=88.0,
    co2_ppm=920
)

print(prediction)
```

The prediction function automatically:

- Creates engineered features
- Applies the saved Min-Max scaler
- Loads the champion Linear Regression model
- Returns predicted mushroom yield in kilograms

## Run Streamlit App

### Streamlit Dashboard

Run:

```bash
streamlit run app.py
```

The dashboard allows users to:

- Enter temperature, humidity and CO₂ readings
- Generate yield forecasts
- View a humidity sensitivity chart
- Review model performance information
- Receive warnings when values fall outside the training range

## Deployment URL

https://mushroom-yield-forecast-yuyw8tbwilapps8umkaafac.streamlit.app/