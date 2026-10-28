import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

scaler = joblib.load("D:\\after grad training\\Customer Churn Prediction\\scaler.pkl")
model = joblib.load("D:\\after grad training\\Customer Churn Prediction\\best_model.pkl")

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predict whether a customer will churn.",
    version="1.0.0",
)


class CustomerFeatures(BaseModel):
    age: float = Field(ge=18, le=100)
    tenure: float = Field(ge=0, le=72)
    monthly_charges: float = Field(ge=30, le=200)
    gender: str

@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running",
        "docs": "/docs",
    }



@app.post("/predict")
def predict(customer: CustomerFeatures):
    # Match the encoding used in the original Streamlit app
    gender = customer.gender.strip().lower()

    if gender not in {"male", "female"}:
        raise HTTPException(
            status_code=422,
            detail="Gender must be Male or Female",
        )

    gender_encoded = 1 if gender == "male" else 0

    # Preserve the training feature order
    features = np.array([[
        customer.age,
        customer.tenure,
        customer.monthly_charges,
        gender_encoded,
    ]])

    scaled_features = scaler.transform(features)
    prediction = model.predict(scaled_features)[0]

    predicted_class = (
        "Churn" if prediction == 1 else "Not Churn"
    )

    return {
        "prediction": predicted_class,
        "customer": {
            "age": customer.age,
            "tenure": customer.tenure,
            "monthly_charges": customer.monthly_charges,
            "gender": gender.capitalize(),
        },
    }


