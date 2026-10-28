import streamlit as st
import pandas as pd
import joblib
import numpy as np

scaler=joblib.load("scaler.pkl")
model=joblib.load("best_model.pkl")



st.title("Customer Churn Prediction")

st.divider()

st.write("please enter the following details to predict whether a customer will churn or not:")
st.divider()

age=st.number_input("Age", min_value=18.0, max_value=100.0, value=30.0 ,step=1.0)
tenure=st.number_input("Tenure (in months)", min_value=0.0, max_value=72.0, value=12.0)
monthly_charges=st.number_input("Monthly Charges", min_value=30.0, max_value=200.0, value=50.0)
gender=st.selectbox("Gender", ["Male", "Female"])

st.divider()

predict_button=st.button("Predict")

if predict_button:
    gender_encoded=1 if gender=="Male" else 0

    x=[age, tenure, monthly_charges, gender_encoded]

    x1=np.array(x).reshape(1,-1)
    x_array=scaler.transform(x1)

    prediction=model.predict(x_array)

    predicted_class="Churn" if prediction[0]==1 else "Not Churn"

    st.balloons()
    st.write(f"The predicted class is: {predicted_class}")
else:
    st.write("Please enter the details and click on Predict button to see the result.")