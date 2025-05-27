import streamlit as st
import joblib
import numpy as np

# Load the model once
model = joblib.load("models/price_predictor.pkl")

def predict_price(rating, reviews):
    features = np.array([[rating, reviews]])
    pred = model.predict(features)[0]
    return pred

st.title("📱 Smartphone Price Predictor")

# Logo or header image (optional)
# st.image("path_to_logo.png", width=150)  # Uncomment if you have a logo

st.write("Enter smartphone features to predict its price.")

# Input fields with validation
rating = st.number_input("Enter product rating (0-5):", min_value=0.0, max_value=5.0, step=0.1)
reviews = st.number_input("Enter number of reviews (0 or more):", min_value=0, step=1)

if st.button("Predict Price"):
    if reviews < 0 or rating < 0 or rating > 5:
        st.error("Please enter valid rating (0-5) and reviews (≥0).")
    else:
        price = predict_price(rating, reviews)
        low = price * 0.9
        high = price * 1.1
        st.success(f"Predicted price: ₹{price:,.2f}")
        st.info(f"Estimated price range: ₹{low:,.2f} - ₹{high:,.2f}")

# Add some styling
st.markdown("""
<style>
body {
    background-image: url('https://images.unsplash.com/photo-1511707171634-5f897ff02aa9');
    background-size: cover;
    color: white;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)