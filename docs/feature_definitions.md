# Feature Definitions



## temperature_c

Daily polyhouse air temperature in °C.



## humidity_pct

Daily relative humidity percentage.



## co2_ppm

Daily carbon dioxide concentration in ppm.



## temp_humid_interaction



### Formula

`temperature_c × humidity_pct / 100`



### Rationale

Mushroom growth depends on both temperature and humidity. This interaction feature captures the combined environmental effects that may influence yield more strongly than either variable alone.



# Scaling



`MinMaxScaler` was applied to all feature columns.



**Current implementation:**  

The scaler is fitted on the full cleaned dataset for learning purposes. In a production pipeline, the scaler should be fitted only on the training data and then applied to validation and test data to prevent data leakage.

