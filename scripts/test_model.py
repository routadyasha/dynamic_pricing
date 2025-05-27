import pandas as pd
import joblib

# Load the model
model = joblib.load("models/price_predictor.pkl")

# Get input from user
try:
    rating = float(input("Enter product rating (e.g., 4.3): "))
    reviews = float(input("Enter number of reviews (e.g., 1500): "))
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()

# Make prediction
predicted_price = model.predict([[rating, reviews]])
print(f"Predicted price: ₹{predicted_price[0]:,.2f}")