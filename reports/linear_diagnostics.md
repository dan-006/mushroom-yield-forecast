# Linear Regression Diagnostics



## Residuals vs Predicted Yield



The residuals are generally centered around zero and appear randomly distributed across the range of predicted yield values. No strong systematic pattern is visible, indicating that the model does not consistently overpredict or underpredict mushroom yield.



Most residuals fall within approximately ±1 kg, although a small number of larger positive and negative residuals are present. The spread of residuals appears relatively consistent across predicted values, with only slight variation at higher yield levels. Overall, there is no strong evidence of severe heteroscedasticity.



## Residuals vs Humidity



Residuals remain centered around zero across the full humidity range. No clear trend, curvature, or funnel-shaped pattern is observed, suggesting that the model captures the humidity-related relationship reasonably well.



Most residuals are concentrated within approximately ±1 kg of zero, although a few outlier observations remain. The random distribution of residuals indicates that substantial humidity-related information is not being systematically missed by the model.



## Diagnostic Findings



1. Residuals are generally centered around zero, indicating low overall prediction bias.

2. No strong systematic pattern is visible in the residuals versus predicted yield plot.

3. No clear nonlinear relationship is evident in the residuals versus humidity plot.

4. A small number of outliers remain, indicating occasional prediction errors that are not fully explained by the current feature set.

5. Residual variance appears reasonably consistent across the prediction range, suggesting that the assumptions of linear regression are largely satisfied.



## Modeling Recommendation



The Linear Regression model provides an interpretable baseline with acceptable predictive performance (R² = 0.455, MAE = 0.439 kg).



Residual analysis indicates that the model captures a meaningful portion of the relationship between environmental variables and mushroom yield. However, unexplained variation remains, as evidenced by the presence of residual outliers and moderate predictive accuracy. These findings suggest that some relationships between environmental conditions and yield may be nonlinear or involve more complex interactions.



To investigate whether predictive performance can be improved, a nonlinear model such as Random Forest Regression should be evaluated and compared against the linear baseline.

