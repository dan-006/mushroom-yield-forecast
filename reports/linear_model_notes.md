Linear Regression Coefficient Interpretation



The temperature-humidity interaction feature received the largest positive coefficient in the model. This indicates that the combined effect of temperature and humidity contributes substantially to mushroom yield prediction. Favorable temperature conditions appear to be most effective when accompanied by suitable humidity levels.



CO₂ concentration received a relatively small coefficient compared with the interaction feature, suggesting that its individual contribution to yield prediction is modest when the other environmental variables are considered simultaneously.



Temperature and humidity individually received negative coefficients. These signs should be interpreted cautiously because the temperature-humidity interaction feature is highly correlated with its component variables. This multicollinearity can distort individual coefficient values while still allowing the model to make accurate predictions.



The overall model achieved a test MAE of approximately 0.41 kg and a test R² of 0.53, indicating that the environmental variables explain a meaningful portion of yield variability. Therefore, model performance metrics are more reliable for interpretation than the signs of individual correlated coefficients.



From an agritech perspective, the results suggest that environmental conditions act together rather than independently. Maintaining an appropriate balance between temperature and humidity may be more important for yield optimization than adjusting any single environmental factor in isolation.



