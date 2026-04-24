import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

# Create models folder if not exists
os.makedirs("models", exist_ok=True)

# Load dataset
data = pd.read_csv("data/energy.csv")

# Convert datetime
data["datetime"] = pd.to_datetime(data["datetime"])

# Feature engineering
data["hour"] = data["datetime"].dt.hour
data["day"] = data["datetime"].dt.day
data["month"] = data["datetime"].dt.month

X = data[["hour", "day", "month"]]
y = data["consumption"]

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved in models/model.pkl")
