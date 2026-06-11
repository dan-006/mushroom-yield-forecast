Linear Regression Diagnostics



Residuals vs Predicted Yield



Residuals are generally centered around zero and appear randomly distributed across predicted yield values. No strong systematic bias is visible, indicating that the model does not consistently overpredict or underpredict mushroom yield.



A small number of large negative residuals are present, suggesting occasional observations where yield is substantially overestimated by the model. Mild heteroscedasticity is visible at higher predicted yield values, although the effect is not severe.



Residuals vs Humidity



Residuals remain centered around zero across the full humidity range. No clear curvature or U-shaped pattern is observed, suggesting that the current model captures the humidity-related signal reasonably well.



Several outlier observations remain, but most residuals fall within approximately ±1 kg of zero.



Diagnostic Findings



1\. Residuals are generally centered around zero, indicating low overall prediction bias.

2\. No strong nonlinear pattern is visible in the humidity residual plot.

3\. A small number of large negative residuals indicate occasional prediction errors that are not explained by the current feature set.

4\. Mild heteroscedasticity is present at higher predicted yield levels.

5\. Train and test residual magnitudes are similar, suggesting the model generalizes reasonably well and does not show clear signs of overfitting.



Modeling Recommendation



The Linear Regression model provides an interpretable baseline with acceptable predictive performance (R² = 0.455, MAE = 0.439 kg).



Residual analysis suggests that the model captures a meaningful portion of the relationship between environmental variables and mushroom yield, but unexplained variation remains. Because some residual structure and outliers persist, evaluating a nonlinear model such as Random Forest Regression is recommended to determine whether predictive performance can be improved.



