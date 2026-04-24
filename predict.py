import pickle
import pandas as pd

def load_model():
    with open("models/model.pkl", "rb") as f:
        return pickle.load(f)

def predict_consumption(hour, day=1, month=1):
    model = load_model()
    input_data = pd.DataFrame([[hour, day, month]], columns=["hour", "day", "month"])
    prediction = model.predict(input_data)
    return float(prediction[0])
