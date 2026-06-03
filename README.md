Dan Intern - Mushroom Yield Forecast Project



Problem Statement



Predict daily mushroom yield (kg) in a climate-controlled polyhouse

using temperature, humidity, and CO₂ sensor readings.

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

