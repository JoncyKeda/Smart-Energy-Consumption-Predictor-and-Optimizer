import streamlit as st
import pandas as pd
from predict import predict_consumption
from utils import suggest_optimization
from anomaly import detect_anomalies

st.set_page_config(page_title="Energy Predictor", layout="centered")

st.title("⚡ Smart Energy Consumption Predictor")

# Input
hour = st.slider("Select Hour", 0, 23, 12)
day = st.slider("Select Day", 1, 31, 1)
month = st.slider("Select Month", 1, 12, 1)

if st.button("Predict Consumption"):
    prediction = predict_consumption(hour, day, month)

    st.subheader(f"🔮 Predicted Consumption: {prediction:.2f} units")

    suggestion = suggest_optimization(prediction)
    st.info(suggestion)

# Load dataset
st.subheader("📊 Historical Data + Anomaly Detection")
data = pd.read_csv("data/energy.csv")
data = detect_anomalies(data)

st.dataframe(data)
