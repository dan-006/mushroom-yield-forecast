Feature Definitions



temperature\_c

Daily polyhouse air temperature in °C.



humidity\_pct

Daily relative humidity percentage.



co2\_ppm

Daily carbon dioxide concentration in ppm.

temp\_humid\_interaction



Formula:

temperature\_c × humidity\_pct / 100



Rationale:

Mushroom growth depends on both temperature and humidity. This interaction feature captures combined environmental effects that may influence yield more strongly than either variable alone.



Scaling

MinMaxScaler was applied to all feature columns.



Current implementation fits on the full cleaned dataset for learning purposes.

