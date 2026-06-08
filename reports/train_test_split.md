Train/Test Split Report



Split Method

Chronological 80/20 split.



Reason

Future sensor readings must never be available when predicting past yield. A random split would introduce unrealistic information leakage.



Train Window

2024-01-01 to 2024-10-18



Test Window

2024-10-19 to 2024-12-30



Train Rows

292



Test Rows

73



Scaling

MinMaxScaler was fitted on the training set only and then applied to the test set.



Leakage Prevention

No test information was used during scaler fitting or feature generation.



