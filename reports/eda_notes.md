EDA Notes



Overview



Exploratory Data Analysis (EDA) was performed on 994 cleaned polyhouse observations collected between January 2023 and September 2025. Correlation analysis and scatter plots were used to examine relationships between environmental variables and mushroom yield.



Correlation Analysis



Strongest Positive Correlation



\* Temperature and CO₂ concentration show the strongest positive correlation among the environmental variables.

\* This suggests periods of higher temperature are often associated with higher CO₂ levels within the polyhouse environment.



Strongest Negative Correlation



\* Temperature and humidity exhibit a strong negative correlation.

\* As temperature increases, humidity generally decreases, which is consistent with expected greenhouse and polyhouse conditions.



Yield Relationships



\* Yield shows a weak positive correlation with temperature.

\* Yield also shows a weak positive correlation with CO₂ concentration.

\* Humidity displays a weak negative correlation with yield.

\* Overall, no single environmental variable appears to strongly determine yield on its own.



Scatter Plot Findings



Temperature vs Yield



\* A slight upward trend is visible.

\* Higher temperatures are associated with marginally higher yields.

\* The relationship is relatively weak, suggesting other factors also influence production.



Humidity vs Yield



\* The scatter plot shows substantial overlap across humidity levels.

\* No strong visual trend is apparent.

\* Humidity alone does not appear to be a strong predictor of yield in this dataset.



CO₂ vs Yield



\* A mild positive relationship can be observed.

\* Higher CO₂ concentrations are sometimes associated with higher yields, although the effect appears limited.



Data Quality Observations



\* No major outlier clusters are visible after cleaning.

\* Environmental measurements remain within realistic polyhouse operating ranges.

\* Yield values are relatively consistent throughout the observation period.

\* The dataset contains stable environmental conditions with moderate seasonal variation.



Modeling Implications



\* Temperature should be retained as an important predictor due to its positive relationship with yield.

\* CO₂ should also be included because it demonstrates a modest positive association with production.

\* Humidity may provide additional context even though its individual relationship with yield appears weak.

\* Since correlations with yield are relatively small, combining multiple features will likely be more effective than relying on any single variable.

\* Linear regression can serve as a useful baseline model before testing more advanced approaches.



Caveats



\* Correlation does not imply causation.

\* Environmental variables influence one another and may be affected by polyhouse management practices.

\* This is a synthetic dataset and may not fully capture the biological complexity of commercial mushroom cultivation.



