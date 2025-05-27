import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
import os

# Load the cleaned data
df = pd.read_csv("data/processed/amazon_smartphones_cleaned.csv")

# Fill missing reviews with 0 (or another strategy)
df['reviews'] = df['reviews'].fillna(0)

# Feature selection (we'll use rating and reviews to predict price)
X = df[['rating', 'reviews']]
y = df['price']

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"MAE: ₹{mae:.2f}")
print(f"RMSE: ₹{rmse:.2f}")

# Save the model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/price_predictor.pkl")
print("Saved model to models/price_predictor.pkl")
