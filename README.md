Mushroom Yield Forecast Project


Problem Statement

Predict daily mushroom yield (kg) in a climate-controlled polyhouse using temperature, humidity, and CO₂ sensor readings.
The goal is to build a machine learning pipeline that estimates mushroom yield from sensor readings.


Environment Setup

1\. Create virtual environment
python -m venv venv
2\. Activate virtual environment
Windows CMD
venv\\Scripts\\activate
Windows PowerShell
.\\venv\\Scripts\\Activate.ps1
3\. Install dependencies
pip install -r requirements.txt


Project Structure

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

|   |-- smoke\_test.py

|

|-- requirements.txt

|-- README.md

|-- .gitignore



Smoke Test

Run:
python src\\smoke\_test.py

Expected Output:
Polyhouse sensor snapshot:
...

Environment OK.

Folder Map

data/raw      -> Raw sensor CSV files

notebooks     -> Jupyter notebooks

src           -> Python scripts

models        -> Trained models



Champion Model

Linear Regression was selected as the champion model because it achieved the best performance on the held-out test set while remaining simple and highly interpretable.

Run Inference
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
from src.predict import predict\_yield
prediction = predict\_yield(
&#x20;   temperature\_c=22.0,
&#x20;   humidity\_pct=88.0,
&#x20;   co2\_ppm=920
)
print(prediction)

```

The prediction function automatically:

\* Creates engineered features

\* Applies the saved Min-Max scaler

\* Loads the champion Linear Regression model

\* Returns predicted mushroom yield in kilograms


Run Streamlit App

Streamlit Dashboard
Run:
streamlit run app.py

The dashboard allows users to:

- Enter temperature, humidity and CO₂ readings
- Generate yield forecasts
- View a humidity sensitivity chart
- Review model performance information
- Receive warnings when values fall outside the training range