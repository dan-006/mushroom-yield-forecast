Test Scenarios



| Scenario           | Temperature (°C) | Humidity (%) | CO₂ (ppm) | Expected Behaviour                                    |

| ------------------ | ---------------- | ------------ | --------- | ----------------------------------------------------- |

| Optimal Conditions | 22               | 88           | 920       | Yield should be within normal operating range         |

| Dry Conditions     | 22               | 70           | 920       | Yield should differ from optimal conditions           |

| Heat Spike         | 32               | 88           | 920       | Yield should remain reasonable and not crash          |

| Low CO₂            | 22               | 88           | 500       | Prediction should still be generated                  |

| High CO₂           | 22               | 88           | 1500      | Prediction should still be generated                  |

| Extreme Inputs     | 35               | 50           | 2000      | Warning should appear and prediction should still run |



Parity Check



For each scenario:



1\. Run `predict\_yield()` in Python.

2\. Enter identical values in Streamlit.

3\. Verify both predictions match exactly.



Result: PASS



