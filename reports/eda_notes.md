\# EDA Notes



\## Overview



Exploratory Data Analysis (EDA) was performed on 980 cleaned polyhouse observations collected between January 2023 and September 2025. Correlation analysis and scatter plots were used to examine relationships between environmental variables and mushroom yield and to identify potential predictors for machine learning models.



\## Correlation Analysis



\### Yield Correlations



\* Temperature exhibits the strongest positive correlation with mushroom yield.

\* Humidity shows a weak positive correlation with yield.

\* CO₂ concentration shows a weak negative correlation with yield.

\* None of the environmental variables individually demonstrate an extremely strong correlation with yield, indicating that multiple factors likely contribute to production outcomes.



\### Relationships Among Environmental Variables



\* Temperature and humidity display only a weak relationship.

\* Temperature and CO₂ concentration also appear to have little correlation.

\* Humidity and CO₂ show minimal association.

\* Overall, the environmental variables are not strongly correlated with one another, reducing concerns about severe multicollinearity.



\## Scatter Plot Findings



\### Temperature vs Yield



\* A clear positive trend is visible.

\* Higher temperatures are generally associated with higher mushroom yield.

\* The relationship appears approximately linear and is the strongest pattern observed among the predictor variables.



\### Humidity vs Yield



\* A weak positive relationship is present.

\* Yield tends to increase slightly as humidity increases.

\* Considerable variation remains at all humidity levels, suggesting that humidity alone is not a strong predictor of yield.



\### CO₂ vs Yield



\* A weak negative relationship is observed.

\* Yield decreases slightly as CO₂ concentration increases.

\* The scatter plot shows substantial dispersion, indicating that CO₂ alone explains little of the variation in yield.



\## Data Quality Observations



\* No major outlier clusters are visible after data cleaning.

\* Environmental measurements fall within realistic operating ranges.

\* Scatter plots show continuous distributions without obvious data-entry errors.

\* The dataset appears suitable for predictive modeling and feature engineering.



\## Modeling Implications



\* Temperature should be retained as a primary predictor because it demonstrates the strongest relationship with yield.

\* Humidity should remain in the feature set because it contributes additional information despite its weaker correlation.

\* CO₂ should also be retained because weak individual correlations do not necessarily imply low predictive value when combined with other variables.

\* The relatively low correlations among predictor variables suggest that linear regression coefficients should remain reasonably stable and interpretable.

\* Linear Regression is an appropriate baseline model due to the approximately linear relationship between temperature and yield.



\## Caveats



\* Correlation does not imply causation.

\* Relationships observed in EDA represent statistical associations rather than direct biological effects.

\* Additional interactions between environmental variables may exist that are not captured by pairwise correlations.

\* This is a synthetic dataset created for educational purposes and does not fully represent commercial mushroom cultivation systems.



