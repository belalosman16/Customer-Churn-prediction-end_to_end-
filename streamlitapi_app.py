import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Customer Churn Prediction", page_icon="📊")
st.title("Customer Churn Prediction")
st.write("Enter the customer details below. Streamlit sends them to the FastAPI backend.")

with st.form("customer_form"):
    age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1)
    tenure = st.number_input("Tenure (in months)", min_value=0, max_value=72, value=12)
    monthly_charges = st.number_input(
        "Monthly Charges", min_value=30.0, max_value=200.0, value=50.0, step=1.0
    )
    gender = st.selectbox("Gender", ["Male", "Female"])
    submitted = st.form_submit_button("Predict")

if submitted:
    payload = {
        "age": age,
        "tenure": tenure,
        "monthly_charges": monthly_charges,
        "gender": gender,
    }

    try:
        with st.spinner("Requesting prediction from the API..."):
            response = requests.post(API_URL, json=payload, timeout=30)

        if response.ok:
            result = response.json()
            predicted_class = result["prediction"]

            if predicted_class == "Churn":
                st.warning(f"Predicted class: {predicted_class}")
            else:
                st.success(f"Predicted class: {predicted_class}")

            with st.expander("API response"):
                st.json(result)
        else:
            st.error(f"API returned HTTP {response.status_code}: {response.text}")

    except requests.exceptions.ConnectionError:
        st.error(
            "Cannot connect to FastAPI. Start the API first with:\n\n"
            "uvicorn main:app --reload"
        )
    except requests.exceptions.RequestException as error:
        st.error(f"Request failed: {error}")




        # uvicorn main:app --reload    terminal 1
        # streamlit run  streamlitapi_app.py   terminal 2
