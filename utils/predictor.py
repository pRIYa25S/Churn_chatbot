import torch
import torch.nn as nn
import joblib
import numpy as np


# ==========================
# Load Scaler
# ==========================
scaler = joblib.load("scaler.pkl")


# ==========================
# ANN Architecture
# (Must match training code)
# ==========================
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
        x = self.fc3(x)
        return x


# ==========================
# Load Model
# ==========================
model = ChurnANN()

model.load_state_dict(
    torch.load(
        "churn_model.pth",
        map_location=torch.device("cpu")
    )
)

model.eval()


# ==========================
# Prediction Function
# ==========================
def predict_churn(features):

    # features must contain exactly:
    # [
    # gender,
    # SeniorCitizen,
    # tenure,
    # InternetService,
    # Contract,
    # PaymentMethod,
    # MonthlyCharges,
    # TotalCharges
    # ]

    gender_map = {
        "Male": 1,
        "Female": 0
    }

    internet_map = {
        "DSL": 0,
        "Fiber optic": 1
    }

    contract_map = {
        "Month-to-month": 0,
        "One year": 1,
        "Two year": 2
    }

    payment_map = {
        "Electronic check": 0,
        "Mailed check": 1,
        "Bank transfer (automatic)": 2,
        "Credit card (automatic)": 3
    }

    data = [
        gender_map[features["gender"]],
        features["SeniorCitizen"],
        features["tenure"],
        internet_map[features["InternetService"]],
        contract_map[features["Contract"]],
        payment_map[features["PaymentMethod"]],
        features["MonthlyCharges"],
        features["TotalCharges"]
    ]

    data = np.array(data).reshape(1, -1)

    data = scaler.transform(data)

    data_tensor = torch.tensor(
        data,
        dtype=torch.float32
    )

    with torch.no_grad():
        output = model(data_tensor)
        probability = torch.sigmoid(output).item()

    return probability