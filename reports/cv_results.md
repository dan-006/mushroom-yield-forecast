Time Series Cross-Validation Results



Methodology



TimeSeriesSplit with 5 folds was applied to the training dataset. This approach preserves chronological order by ensuring that earlier observations are always used to predict later observations.



Only the training dataset was used during cross-validation. The held-out test set remained completely untouched until final model evaluation.



Mean Absolute Error (MAE) was selected as the evaluation metric because it provides a direct interpretation of prediction error in kilograms of mushroom yield.



Cross-Validation Results



| Model             | Mean CV MAE (kg) | Std Dev (kg) |

| ----------------- | ---------------- | ------------ |

| Linear Regression | 0.410            | 0.024        |

| Random Forest     | 0.447            | 0.025        |



Fold-Level Results



Linear Regression



MAE values across folds:



\* 0.432

\* 0.368

\* 0.430

\* 0.419

\* 0.402



Random Forest



MAE values across folds:



\* 0.482

\* 0.415

\* 0.458

\* 0.455

\* 0.423



Comparison with Final Test Results



| Model             | CV MAE (kg) | Test MAE (kg) |

| ----------------- | ----------- | ------------- |

| Linear Regression | 0.410       | 0.412         |

| Random Forest     | 0.447       | 0.447         |



The close agreement between cross-validation and test results indicates that both models generalized well to unseen observations.



Interpretation



Linear Regression achieved the lowest average cross-validation error and slightly lower variability across folds.



Random Forest showed consistent performance across folds but produced higher average prediction errors than Linear Regression.



The similarity between cross-validation and final test results suggests that neither model suffered from substantial overfitting.



Overfitting Analysis



For the Linear Regression model:



\* Mean Absolute Train Residual = 0.400 kg

\* Mean Absolute Test Residual = 0.412 kg



The small difference between training and testing errors indicates strong generalization and little evidence of overfitting.



Random Forest also demonstrated similar cross-validation and test performance, suggesting stable predictive behavior across different time periods.



Recommendation



Both models generalized reasonably well. However, Linear Regression consistently achieved better prediction accuracy during both cross-validation and final testing.



Given its superior performance, lower complexity, and greater interpretability, Linear Regression remains the preferred model for mushroom yield prediction on this dataset.



Conclusion



Linear Regression achieved the strongest overall performance with a Mean CV MAE of 0.410 kg and a Test MAE of 0.412 kg. Random Forest did not provide a meaningful improvement despite its additional complexity. Therefore, Linear Regression was selected as the final model for deployment and future analysis.



