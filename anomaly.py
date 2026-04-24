from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(data):
    model = IsolationForest(contamination=0.1, random_state=42)
    data["anomaly"] = model.fit_predict(data[["consumption"]])

    # Convert -1 → anomaly, 1 → normal
    data["anomaly"] = data["anomaly"].map({1: "Normal", -1: "Anomaly"})
    return data
