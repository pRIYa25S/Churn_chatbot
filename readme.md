# Customer Churn Prediction System

## Overview
The Customer Churn Prediction System is a Machine Learning web application that predicts whether a customer is likely to leave a company's service based on customer subscription and usage information.

The application provides:
- Customer churn prediction
- Prediction history tracking
- Analytics dashboard
- Interactive Streamlit interface

---

## Features

### Prediction Module
- Enter customer details
- Generate churn predictions in real time
- User-friendly interface

### History Module
- Stores prediction results
- Displays all previous predictions
- CSV-based storage

### Analytics Module
- Visualizes prediction trends
- Displays churn distribution charts
- Helps analyze prediction history

### About Module
- Provides project information
- Explains workflow and technologies used

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib / Pickle
- Matplotlib
- Git & GitHub

---

## Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Selection
4. Model Training
5. Model Evaluation
6. Model Saving
7. Prediction Generation
8. Result Storage
9. Analytics Visualization

---

## Dataset Features

The model uses the following customer attributes:

- Gender
- Senior Citizen
- Tenure
- Internet Service
- Contract Type
- Payment Method
- Monthly Charges
- Total Charges

---

## Project Structure

```text
Customer_Churn_Project/
│
├── app.py
├── prediction_history.csv
├── requirements.txt
├── README.md
│
├── model/
│   └── churn_model.pkl
│
├── pages/
│   ├── prediction.py
│   ├── History.py
│   ├── Analytics.py
│   └── About.py
│
└── utils/
    └── predictor.py
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Customer_Churn_Project
```

### Create Virtual Environment

```bash
python -m venv churn_env
```

### Activate Environment

Windows:

```bash
churn_env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

Open in browser:

```text
http://localhost:8501
```

---

## Sample Workflow

1. Open Prediction page
2. Enter customer information
3. Click Predict
4. View prediction result
5. Check History page
6. Analyze trends in Analytics page

---

## Future Enhancements

- Churn probability percentage
- Database integration
- User authentication
- Cloud deployment
- Automated model retraining
- Advanced analytics dashboard

---
## App link
https://churnchatbot-6avqd3ciqj4xmegcfabv2n.streamlit.app/
