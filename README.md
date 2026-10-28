# Customer Churn Prediction

## Project Overview

This project predicts whether a customer is likely to churn using a trained Machine Learning model.

The application uses **Streamlit** for the user interface and **FastAPI** to expose the model through a REST API.

Users can enter customer information and receive a churn prediction.

## Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- Streamlit
- FastAPI
- Uvicorn
- Joblib

## Project Architecture

The project separates the user interface from the prediction service.

1. **Streamlit:** Collects customer information and displays the prediction.
2. **FastAPI:** Receives prediction requests, validates input, and returns results.
3. **Scaler:** Preprocesses the input features.
4. **Machine Learning Model:** Predicts whether the customer will churn.

## Features

- Predict customer churn.
- Accept customer age, tenure, monthly charges, and gender.
- Validate input data through FastAPI.
- Expose predictions through a REST API.
- Test API endpoints using interactive Swagger documentation.

## Input Features

| Feature | Description |
|---|---|
| Age | Customer's age |
| Tenure | Number of months the customer has stayed |
| Monthly Charges | Customer's monthly charges |
| Gender | Male or Female |

## Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure the required model files, `scaler.pkl` and `best_model.pkl`, are available in the location expected by your application.

## Run the Application

### Start the FastAPI Backend

```bash
uvicorn main:app --reload
```

API homepage:

http://127.0.0.1:8000/

Interactive API documentation:

http://127.0.0.1:8000/docs

### Start the Streamlit Frontend

Open a second terminal and run:

```bash
streamlit run streamlit_app.py
```

Open the local URL printed in the terminal, usually:

http://localhost:8501

Keep the FastAPI server running while using Streamlit.

## API Usage

### Endpoint

`POST /predict`

### Example Request

```json
{
  "age": 30,
  "tenure": 12,
  "monthly_charges": 50,
  "gender": "Male"
}
```

### Example Response

```json
{
  "prediction": "Not Churn",
  "customer": {
    "age": 30,
    "tenure": 12,
    "monthly_charges": 50,
    "gender": "Male"
  }
}
```

The example prediction is illustrative. Actual results depend on the trained model.

## Future Improvements

- Add model performance metrics.
- Add automated API tests.
- Containerize the application using Docker.
- Deploy the API and Streamlit application online.
- Add model monitoring and prediction logging.

## Author

**Belal Mostafa **

Computer and Data Science Graduate
