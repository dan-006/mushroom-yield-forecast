# Random Forest Results



## Model Performance



Random Forest Regressor was trained using the same chronological train/test split used for Linear Regression. This ensured a fair comparison between models while preserving temporal order.



## Test Metrics



| Metric | Linear Regression | Random Forest |
|----------|------------------:|--------------:|
| MAE | 0.412 kg | 0.447 kg |
| RMSE | 0.508 kg | 0.544 kg |
| R² | 0.525 | 0.453 |



The Random Forest model produced slightly worse results than the Linear Regression baseline across all evaluation metrics.



## Feature Importance



### Feature Importance Ranking



1. Temperature

2. Humidity

3. CO₂

4. Temperature-Humidity Interaction



Temperature was identified as the most influential predictor of mushroom yield, which is consistent with findings from exploratory data analysis. Humidity also contributed substantially to model predictions, while CO₂ provided a smaller contribution. The engineered temperature-humidity interaction feature had the lowest importance among the available predictors.



## Interpretation



Random Forest is capable of capturing nonlinear relationships and complex feature interactions. However, it did not outperform the simpler Linear Regression model on this dataset.



This suggests that the relationship between environmental conditions and mushroom yield is largely linear and can be modeled effectively without additional algorithmic complexity. The Random Forest model may have introduced unnecessary variance without uncovering additional predictive patterns.



## Recommendation



For the current dataset, Linear Regression remains the preferred model because:



- It achieved better test performance.

- It achieved a higher R² score.

- It is easier to interpret.

- It requires fewer computational resources.

- Environmental effects can be communicated more clearly to stakeholders.



Future improvements should focus on collecting additional predictive features, such as lag variables, operational records, or environmental control actions, rather than increasing model complexity alone.



## Conclusion



Although Random Forest produced reasonable predictions, it did not improve upon the Linear Regression baseline. Therefore, Linear Regression was selected as the final model for mushroom yield prediction in this project.

