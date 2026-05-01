import streamlit as st
import joblib
import pandas as pd

# Load saved deployment objects
deployment = joblib.load("churn_model_deployment.pkl")
model = deployment["model"]
scaler = deployment["scaler"]
feature_cols = deployment["feature_cols"]
threshold = deployment["optimal_threshold"]

st.title("Telco Customer Churn Predictor")
st.write("Enter customer information below to predict churn risk.")

# User inputs
gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
phone_service = st.selectbox("Phone Service", ["No", "Yes"])
multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes"])
online_security = st.selectbox("Online Security", ["No", "Yes"])
online_backup = st.selectbox("Online Backup", ["No", "Yes"])
device_protection = st.selectbox("Device Protection", ["No", "Yes"])
tech_support = st.selectbox("Tech Support", ["No", "Yes"])
streaming_tv = st.selectbox("Streaming TV", ["No", "Yes"])
streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes"])
paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"])
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=70.0, step=1.0)
total_charges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=1000.0, step=10.0)

internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
payment_method = st.selectbox(
    "Payment Method",
    [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check"
    ]
)

# Build one input row with all required features
input_data = {
    "gender": 1 if gender == "Male" else 0,
    "SeniorCitizen": 1 if senior == "Yes" else 0,
    "Partner": 1 if partner == "Yes" else 0,
    "Dependents": 1 if dependents == "Yes" else 0,
    "tenure": tenure,
    "PhoneService": 1 if phone_service == "Yes" else 0,
    "MultipleLines": 1 if multiple_lines == "Yes" else 0,
    "OnlineSecurity": 1 if online_security == "Yes" else 0,
    "OnlineBackup": 1 if online_backup == "Yes" else 0,
    "DeviceProtection": 1 if device_protection == "Yes" else 0,
    "TechSupport": 1 if tech_support == "Yes" else 0,
    "StreamingTV": 1 if streaming_tv == "Yes" else 0,
    "StreamingMovies": 1 if streaming_movies == "Yes" else 0,
    "PaperlessBilling": 1 if paperless_billing == "Yes" else 0,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
    "InternetService_DSL": 1 if internet_service == "DSL" else 0,
    "InternetService_Fiber optic": 1 if internet_service == "Fiber optic" else 0,
    "InternetService_No": 1 if internet_service == "No" else 0,
    "Contract_Month-to-month": 1 if contract == "Month-to-month" else 0,
    "Contract_One year": 1 if contract == "One year" else 0,
    "Contract_Two year": 1 if contract == "Two year" else 0,
    "PaymentMethod_Bank transfer (automatic)": 1 if payment_method == "Bank transfer (automatic)" else 0,
    "PaymentMethod_Credit card (automatic)": 1 if payment_method == "Credit card (automatic)" else 0,
    "PaymentMethod_Electronic check": 1 if payment_method == "Electronic check" else 0,
    "PaymentMethod_Mailed check": 1 if payment_method == "Mailed check" else 0,
}

input_df = pd.DataFrame([input_data])
input_df = input_df[feature_cols]

if st.button("Predict Churn"):
    scaled_input = scaler.transform(input_df)
    churn_probability = model.predict_proba(scaled_input)[0][1]
    prediction = "CHURN" if churn_probability >= threshold else "STAY"

    st.subheader(f"Prediction: {prediction}")
    st.write(f"Churn Probability: {churn_probability:.2%}")
    st.write(f"Decision Threshold: {threshold:.2f}")