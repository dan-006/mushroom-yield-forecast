import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Mushroom Yield Forecast",
    layout="centered"
)

from src.predict import predict_yield
@st.cache_resource
def load_predictor():
    return predict_yield
predictor = load_predictor()

st.title("Polyhouse Yield Predictor")

st.caption(
    "Estimate daily mushroom yield from temperature, humidity and CO₂ readings."
)
st.markdown(
    "See project methodology in `reports/model_comparison.md` and project documentation."
)
with st.sidebar:
    temp = st.slider(
        "Temperature (°C)",
        10.0, 35.0, 22.0, 0.1
    )

    humidity = st.slider(
        "Humidity (%)",
        50.0, 100.0, 88.0, 0.5
    )

    co2 = st.slider(
        "CO₂ (ppm)",
        400, 2000, 900, 10
    )
if not (16.53 <= temp <= 26.77):
    st.warning(
        "Temperature is outside the range observed during model training."
    )

if not (77.9 <= humidity <= 95.7):
    st.warning(
        "Humidity is outside the range observed during model training."
    )

if not (655 <= co2 <= 1145):
    st.warning(
        "CO₂ is outside the range observed during model training."
    )

if st.button("Predict Yield"):

    prediction = predictor(
     temp,
     humidity,
     co2
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Estimated Daily Yield",
            f"{prediction:.2f} kg"
        )

    with col2:
        st.info(
            "Prediction based on current environmental conditions."
        )
    
st.subheader("What-if Analysis: Humidity Impact")

humid_range = np.linspace(70, 98, 29)

preds = [
    predictor(temp, h, co2)
    for h in humid_range
]

chart_df = pd.DataFrame({
    "Humidity (%)": humid_range,
    "Predicted Yield (kg)": preds
})

st.line_chart(
    chart_df,
    x="Humidity (%)",
    y="Predicted Yield (kg)"
)

with st.expander("Model Information"):

    st.markdown("""
    **Champion Model:** Linear Regression
    
    **Model Version:** v0.1-model

    **Test MAE:** 0.439 kg

    **Test RMSE:** 0.713 kg

    **Test R²:** 0.525

    **Training Data Range:**
    January 2023 – September 2025

    **Features Used:**
    - Temperature (°C)
    - Humidity (%)
    - CO₂ (ppm)
    - Temperature-Humidity Interaction
    """)
with st.expander("Forecast Confidence"):

    st.write(
        """
        Typical prediction error is approximately
        ±0.44 kg per day on unseen data.

        Predictions should be used as a decision-support
        tool and not as a guarantee of future yield.
        """
    )