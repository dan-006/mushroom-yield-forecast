\# EDA Notes



\## Overview



Exploratory Data Analysis was performed on 365 daily mushroom polyhouse observations containing temperature, humidity, CO₂ concentration, and yield measurements. Correlation analysis and scatter plots were used to identify relationships between environmental conditions and mushroom yield.



\## Correlation Analysis



\### Strongest Positive Correlation



\* Temperature shows the strongest positive correlation with yield among the available features.

\* The heatmap indicates that higher temperatures within the observed operating range are generally associated with higher yields.



\### Moderate Positive Correlation



\* Humidity exhibits a moderate positive relationship with yield.

\* Yield tends to increase slightly as humidity increases, although the relationship is weaker than temperature.



\### Strongest Negative Correlation



\* CO₂ concentration shows the strongest negative correlation with yield.

\* However, the magnitude of this negative relationship appears relatively weak and should be interpreted cautiously.



\## Scatter Plot Findings



\### Temperature vs Yield



\* The clearest trend among all scatter plots.

\* Data points form an upward pattern, indicating that yield generally increases as temperature rises.

\* The relationship appears approximately linear within the observed temperature range (18–26°C).

\* Temperature is likely to be an important predictive feature for modeling.



\### Humidity vs Yield



\* A mild positive trend is visible.

\* Higher humidity levels are associated with slightly higher yields.

\* The scatter remains broad, suggesting humidity alone does not fully explain yield variation.



\### CO₂ vs Yield



\* No strong visual trend is apparent.

\* Data points form a relatively dispersed cloud around the average yield.

\* While the heatmap suggests a weak negative correlation, the scatter plot indicates that CO₂ alone is not a strong predictor of yield in this dataset.



\## Data Quality Observations



\* No significant outlier clusters are visible after cleaning.

\* Environmental variables remain within realistic polyhouse operating ranges.

\* Yield values are concentrated between approximately 16 kg and 18.5 kg, indicating stable production conditions.



\## Modeling Implications



\* Temperature should be prioritized as a candidate feature due to its strongest observed relationship with yield.

\* Humidity should also be retained because it shows a moderate positive association with production.

\* CO₂ may contribute useful information when combined with other variables, even though its standalone relationship appears weak.

\* The relationships appear largely linear, making linear regression a reasonable baseline model.

\* More complex models can later be evaluated if nonlinear effects emerge.



\## Caveats



\* Correlation does not imply causation.

\* Environmental variables may interact with each other, and observed relationships may be influenced by overall polyhouse management practices.

\* This is a synthetic dataset with relatively stable operating conditions, so real-world farms may exhibit stronger variability and more complex patterns.



