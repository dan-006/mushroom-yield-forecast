Grid Search Results – Random Forest Hyperparameter Tuning
Objective

The objective of this task was to improve Random Forest performance by identifying an optimal combination of hyperparameters using GridSearchCV. Hyperparameter tuning was performed after establishing baseline results from the default Random Forest model.

Methodology

GridSearchCV was applied to a RandomForestRegressor using only the training dataset. To preserve temporal order and prevent data leakage, TimeSeriesSplit with 3 folds was used during cross-validation.

Model performance was optimized using Mean Absolute Error (MAE). Since Scikit-learn returns negative values for error-based scoring metrics, the reported cross-validation MAE values were converted back to positive values for interpretation.

The following hyperparameters were evaluated:

n_estimators: [50, 100, 200]
max_depth: [None, 5, 10]
min_samples_leaf: [1, 3, 5]

This resulted in 27 parameter combinations. With 3 cross-validation folds, GridSearchCV performed a total of 81 model fits.

Best Parameters

The best-performing parameter combination was:

{
  "max_depth": 5,
  "min_samples_leaf": 3,
  "n_estimators": 200
}

Best Cross-Validation MAE:

0.426

These parameters indicate that a moderately sized forest with shallow trees and slightly larger leaf nodes generalized better than more complex configurations.

Tuned Random Forest Performance

The best estimator was automatically refit on the full training dataset and evaluated on the held-out test set.

Metric	Tuned Random Forest
MAE	0.430 kg
RMSE	0.523 kg
R²	0.496
Comparison with Default Random Forest
Metric	Default RF	Tuned RF
MAE	0.447 kg	0.430 kg
RMSE	0.544 kg	0.523 kg
R²	0.453		0.496

Hyperparameter tuning improved all evaluation metrics, demonstrating better predictive performance and generalization compared to the default Random Forest model.

Interpretation

The optimal model used a maximum tree depth of 5 and a minimum leaf size of 3 samples. Restricting tree growth reduced model variance and helped prevent overfitting. Increasing the number of trees to 200 improved ensemble stability and slightly reduced prediction error.

The relatively low variation in cross-validation scores suggests that the tuned model performed consistently across different temporal segments of the training data.

Conclusion

GridSearchCV successfully improved Random Forest performance relative to the default configuration. The tuned model achieved lower error and a higher R² score, indicating better generalization to unseen data.

Despite these improvements, Linear Regression remained the strongest model overall, achieving lower prediction error and a higher R² score on the held-out test set. Therefore, Linear Regression remains the preferred model for this dataset due to its superior performance, simplicity, and interpretability.