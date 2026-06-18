# Monitoring Plan



## Prediction Logging



All inference requests are logged with the following information:



- Timestamp

- Temperature (°C)

- Humidity (%)

- CO₂ (ppm)

- Predicted Yield (kg)



No personally identifiable information (PII) is stored.



## Monitoring Metrics



The following metrics will be monitored:



- Daily prediction volume

- Average predicted yield

- Maximum predicted yield

- Minimum predicted yield

- Frequency of out-of-range sensor inputs



## Data Drift Risks



Potential sources of data drift include:



1. Sensor recalibration or replacement

2. Seasonal environmental changes

3. New mushroom substrate batches

4. Polyhouse operational changes

5. CO₂ control system modifications



## Retraining Trigger



Model retraining should be considered when:



- Test MAE increases by more than 20%

- Input feature distributions shift significantly

- New seasonal data becomes available

- At least six months of new production data have been collected



## Business Impact Monitoring



The following business impacts should be monitored:



- Yield overestimation causing buyer shortfalls

- Yield underestimation causing inefficient harvest planning

- Prediction failures or missing forecasts



## Iteration Roadmap



### Planned Improvements



1. Add additional environmental features such as light intensity and substrate moisture.

2. Create an automated retraining pipeline using fresh harvest logs.

3. Implement automated drift detection and alerting mechanisms.

