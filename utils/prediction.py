import streamlit as st
from utils.predictor import predict_churn

st.title("🔍 Customer Churn Prediction")

# Inputs

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

senior = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

tenure = st.number_input(
    "Tenure (Months)",
    min_value=0
)

internet = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0
)

# Predict button
if st.button("Predict"):

    features = {
        "gender": gender,
        "SeniorCitizen": senior,
        "tenure": tenure,
        "InternetService": internet,
        "Contract": contract,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }

    result = predict_churn(features)

    st.success(f"Prediction: {result}")