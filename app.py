import streamlit as st
import torch
import torch.nn as nn
import numpy as np
import joblib

# ===============================
# Model Definition (MUST MATCH TRAINING)
# ===============================
class ChurnANN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(8, 32)
        self.bn1 = nn.BatchNorm1d(32)
        self.fc2 = nn.Linear(32, 16)
        self.bn2 = nn.BatchNorm1d(16)
        self.fc3 = nn.Linear(16, 1)

    def forward(self, x):
        x = torch.relu(self.bn1(self.fc1(x)))
        x = torch.relu(self.bn2(self.fc2(x)))
        return self.fc3(x)


# ===============================
# Load Model & Scaler
# ===============================
scaler = joblib.load("scaler.pkl")

model = ChurnANN()
model.load_state_dict(torch.load("churn_model.pth", map_location="cpu"))
model.eval()


# ===============================
# Streamlit UI
# ===============================
st.title("📊 Customer Churn Prediction")

gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen", ["No", "Yes"])
tenure = st.number_input("Tenure (months)", min_value=0)
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
payment = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer", "Credit card"]
)
monthly = st.number_input("Monthly Charges", min_value=0.0)
total = st.number_input("Total Charges", min_value=0.0)


# ===============================
# Encoding (MUST MATCH TRAINING)
# ===============================
gender_map = {"Female": 0, "Male": 1}
senior_map = {"No": 0, "Yes": 1}
internet_map = {"DSL": 0, "Fiber optic": 1, "No": 2}
contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}
payment_map = {
    "Electronic check": 0,
    "Mailed check": 1,
    "Bank transfer": 2,
    "Credit card": 3
}


# ===============================
# Prediction
# ===============================
if st.button("Predict Churn"):

    input_data = np.array([[
        gender_map[gender],
        senior_map[senior],
        tenure,
        internet_map[internet],
        contract_map[contract],
        payment_map[payment],
        monthly,
        total
    ]])

    input_scaled = scaler.transform(input_data)
    input_tensor = torch.tensor(input_scaled, dtype=torch.float32)

    with torch.no_grad():
        prob = torch.sigmoid(model(input_tensor)).item()

    st.subheader("Prediction Result")
    st.write(f"### 🔢 Churn Probability: **{prob*100:.2f}%**")

    if prob >= 0.5:
        st.error("🚨 High Risk: Customer is likely to churn")
    else:
        st.success("✅ Low Risk: Customer is likely to stay")
