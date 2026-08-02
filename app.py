import streamlit as st

st.set_page_config(
    page_title = "House Price Prediction",
    page_icon = "🏡",
    layout = "centered"
)

st.title("🏡 House Price Prediction")
st.write("Predict the price of a house using Machine Learning.")

st.image("image.png", use_container_width=True)

# Loading the model 
import joblib

model = joblib.load("model.pkl")

# User input fields

st.subheader("Enter House Details")
area = st.number_input("Area (sq.ft)", min_value = 500, max_value = 5000, value = 1200)
bedrooms = st.number_input("Bedrooms", min_value = 1, max_value = 6, value = 2)
bathrooms = st.number_input("Bathrooms", min_value = 1, max_value = 6, value = 2)
floors = st.number_input("Floors",min_value = 1, max_value = 3, value = 1)
parking = st.number_input("Parking",min_value = 0, max_value = 3, value = 1)
age = st.number_input("House age", min_value = 0, max_value = 30, value = 5)
location_score = st.slider(
    "Location Score",
    min_value=1,
    max_value=10,
    value=5
)

#Predict Button

import pandas as pd 

if st.button ("Predict Price"):
    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "floors" : [floors],
        "parking": [parking],
        "age" : [age],
        "location_score" : [location_score]
    })

    prediction = model.predict (input_data)
    st.success (f"Predicted House Price: ₹ {prediction[0]:,.2f}")


st.sidebar.title("🏠 House Price Prediction")

st.sidebar.info("""
This application predicts house prices
using a Machine Learning model trained
with Linear Regression.
""")

st.markdown("""
### About this Project

Enter the house details below and click **Predict Price**.
The model estimates the house price based on the provided features.
""")

