# Model Comparison Report



## Objective



Three machine learning models were evaluated for mushroom yield prediction using environmental sensor data collected from a polyhouse environment:



- Linear Regression

- Random Forest (Default Parameters)

- Random Forest (Tuned using GridSearchCV)



All models were trained using the same chronological train-test split and evaluated on the same untouched test dataset to ensure a fair comparison.



## Performance Comparison



| Model | CV MAE (kg) | Test MAE (kg) | RMSE (kg) | R² | Training Time |
|---------|---------:|---------:|---------:|---------:|---------|
| Linear Regression | 0.410 | 0.412 | 0.508 | 0.525 | < 1 sec |
| Random Forest (Default) | 0.447 | 0.447 | 0.544 | 0.453 | ~1 sec |
| Random Forest (Tuned) | 0.426 | 0.430 | 0.523 | 0.496 | ~30–60 sec (81 fits) |



## Model Evaluation



Linear Regression achieved the strongest overall performance on the held-out test dataset. It produced the lowest Mean Absolute Error (MAE), the lowest Root Mean Squared Error (RMSE), and the highest coefficient of determination (R²).



The default Random Forest model performed worse than Linear Regression across all evaluation metrics. Although Random Forest can capture nonlinear relationships, the available sensor variables appear to contain a signal that is already modeled effectively by the linear baseline.



GridSearchCV tuning improved Random Forest performance. The tuned model reduced both MAE and RMSE compared with the default configuration and increased R² from 0.453 to 0.496. However, it still did not outperform Linear Regression.



## Champion Model



### Selected Model: Linear Regression



Linear Regression was selected as the champion model for deployment.



### Performance Summary



- Lowest Test MAE (0.412 kg)

- Lowest Test RMSE (0.508 kg)

- Highest Test R² (0.525)



In addition to stronger predictive performance, Linear Regression is fully interpretable. The influence of each environmental variable can be explained directly through model coefficients, making it easier to communicate results to growers and project stakeholders.



The model is also computationally efficient and requires minimal resources for training and prediction.



## Agritech Interpretation



The champion model produces an average prediction error of approximately 0.41 kg of mushrooms per day.



From an operational perspective, this means daily yield forecasts are typically within half a kilogram of actual production. Such accuracy can assist growers in harvest planning, labor allocation, inventory management, and distribution scheduling.



Underestimating yield may result in insufficient labor allocation during harvesting, while overestimating yield may create unrealistic expectations for buyers and distributors. Minimizing prediction error therefore improves planning reliability throughout the production cycle.



## Predicted vs Actual Yield



A predicted-versus-actual yield plot was generated for the champion model and saved as:



```text

reports/figures/pred_vs_actual_linear.png

```



The predicted-versus-actual plot shows a clear positive relationship between observed and predicted mushroom yield values. Most points lie reasonably close to the diagonal reference line, indicating that the model captures the overall yield trend effectively.



Some scatter is visible around the line, which reflects normal prediction error. The model tends to compress predictions toward the average yield range (approximately 16.5–17.8 kg). As a result, very low yields are occasionally overpredicted while very high yields are slightly underpredicted.



Despite these deviations, there is no strong evidence of systematic bias, and the plot supports the quantitative performance metrics obtained during testing (MAE = 0.412 kg, RMSE = 0.508 kg, R² = 0.525).



Overall, the figure indicates that Linear Regression provides reliable yield forecasts and is appropriate as the selected champion model for this dataset.



## Model Stability



Cross-validation results showed that Linear Regression generalized well across multiple temporal splits of the training dataset.



The model achieved a mean cross-validation MAE of 0.410 kg with low variation across folds, indicating stable performance over time.



Train and test residual magnitudes were also similar, suggesting minimal overfitting and good generalization to unseen observations.



## Limitations



Several limitations should be considered when interpreting these results:



- The model was trained on temperature values between approximately 16.5–26.8°C, humidity values between 77.9–95.7%, and CO₂ concentrations between 655–1145 ppm. Predictions outside these ranges may be unreliable.

- The dataset covers January 2023 to September 2025. Longer-term seasonal effects and operational changes may not be fully represented.

- The dataset is synthetic and may not fully represent real-world mushroom production variability.

- Important production factors such as substrate condition, spawn age, irrigation practices, and management interventions are not included.

- Seasonal changes and long-term environmental trends may alter relationships between sensor measurements and yield.

- The model should be treated as a decision-support tool rather than a replacement for grower expertise.



## Conclusion



Three machine learning models were evaluated for mushroom yield prediction using the same train-test split and evaluation framework.



Although hyperparameter tuning improved Random Forest performance, Linear Regression remained the strongest model overall. It achieved the best predictive accuracy while also providing superior interpretability and simplicity.



Based on predictive performance, model stability, and ease of explanation, Linear Regression is recommended as the deployment model for subsequent application development and visualization tasks.

