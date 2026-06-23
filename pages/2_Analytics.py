import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Churn Analytics Dashboard")

df = pd.read_csv("Telco-Customer-Churn.csv")

# KPIs
total_customers = len(df)
churned = len(df[df["Churn"] == "Yes"])
churn_rate = (churned / total_customers) * 100

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Customers", total_customers)

with col2:
    st.metric("Churned Customers", churned)

with col3:
    st.metric("Churn Rate", f"{churn_rate:.2f}%")

st.divider()

# Pie Chart
fig1 = px.pie(
    df,
    names="Churn",
    title="Customer Churn Distribution"
)

st.plotly_chart(fig1, use_container_width=True)

# Contract Analysis
fig2 = px.histogram(
    df,
    x="Contract",
    color="Churn",
    barmode="group",
    title="Contract Type vs Churn"
)

st.plotly_chart(fig2, use_container_width=True)

# Monthly Charges
fig3 = px.box(
    df,
    x="Churn",
    y="MonthlyCharges",
    title="Monthly Charges vs Churn"
)

st.plotly_chart(fig3, use_container_width=True)