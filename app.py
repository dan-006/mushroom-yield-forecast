import streamlit as st
from src.predict import predict_yield
@st.cache_resource
def load_predictor():
    return predict_yield
predictor = load_predictor()

st.set_page_config(
    page_title="Mushroom Yield Forecast",
    layout="centered"
)

st.title("Polyhouse Yield Predictor")

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

if st.button("Predict Yield"):
    prediction = predictor(
        temp,
        humidity,
        co2
    )

    st.metric(
        "Estimated Daily Yield",
        f"{prediction:.2f} kg"
    )