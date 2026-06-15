Reproducibility Notes



Training Configuration



\* Random seed: 42

\* Train/test split: chronological 80/20 split

\* Training cutoff date: 2025-03-12

\* Test period: 2025-03-13 to 2025-09-26



Champion Model



Linear Regression



Saved Artifacts



\* models/linear\_regression.joblib

\* models/minmax\_scaler\_train.joblib

\* models/feature\_cols.json



Key Libraries



\* Python 3.x

\* pandas

\* numpy

\* scikit-learn

\* joblib

\* matplotlib



Reproduction Steps



1\. Create virtual environment.

2\. Install dependencies using requirements.txt.

3\. Run preprocessing pipeline.

4\. Train model.

5\. Execute:



```bash

python src/predict.py

```



to generate predictions.



