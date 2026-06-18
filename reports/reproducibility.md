# Reproducibility Notes

## Training Configuration

- Random seed: 42
- Train/test split: Chronological 80/20 split
- Training cutoff date: 2025-03-12
- Test period: 2025-03-13 to 2025-09-26

## Champion Model

**Linear Regression**

## Saved Artifacts

- `models/linear_regression.joblib`
- `models/minmax_scaler_train.joblib`
- `models/feature_cols.json`

## Key Libraries

- Python 3.x
- pandas
- numpy
- scikit-learn
- joblib
- matplotlib

## Reproduction Steps

1. Create a virtual environment.
2. Install dependencies using `requirements.txt`.
3. Run the preprocessing pipeline.
4. Train the model.
5. Execute:

```bash
python src/predict.py
```

to generate predictions.

## Notes

All experiments were conducted using a fixed random seed to ensure reproducibility. Model artifacts, feature definitions, and preprocessing steps were saved separately to enable consistent inference and future retraining. The chronological train/test split preserves temporal order and prevents data leakage from future observations into the training process.