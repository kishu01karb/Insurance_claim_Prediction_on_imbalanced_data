import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ---------------- LOAD MODEL ----------------
model = joblib.load("xgb_claim_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")
feature_columns = joblib.load("feature_columns.pkl")

st.set_page_config(page_title="Insurance Claim Risk Predictor", layout="centered")

st.title("🛡 Insurance Claim Risk Predictor")
st.write("Answer simple questions. If you're unsure, just choose an approximate option.")

# ---------------- USER INPUTS ----------------
st.header("📋 Customer Details")

age = st.slider("Customer Age", 18, 80, 35,
                 help="Approximate age is fine")

vehicle_age = st.slider("Vehicle Age (years)", 0, 20, 5,
                         help="How old is the vehicle?")

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG", "Electric", "Not sure"],
    help="Select 'Not sure' if unknown"
)

max_power = st.slider(
    "Engine Power (approx)",
    50, 300, 100,
    help="You can estimate — exact value not required"
)

airbags = st.selectbox(
    "Number of Airbags",
    [0, 2, 4, 6, "Not sure"]
)

is_esc = st.radio(
    "Does the vehicle have ESC (Electronic Stability Control)?",
    ["Yes", "No", "Not sure"]
)

# ---------------- HANDLE UNKNOWN VALUES ----------------
if fuel_type == "Not sure":
    fuel_type = "Petrol"

if airbags == "Not sure":
    airbags = 2

if is_esc == "Yes":
    is_esc = 1
elif is_esc == "No":
    is_esc = 0
else:
    is_esc = 0

# ---------------- CREATE INPUT DATAFRAME ----------------
input_data = {
    "age": age,
    "vehicle_age": vehicle_age,
    "fuel_type": fuel_type,
    "max_power": max_power,
    "airbags": airbags,
    "is_esc": is_esc
}

df = pd.DataFrame([input_data])

# ---------------- ENCODE CATEGORICAL ----------------
for col, encoder in label_encoders.items():
    if col in df.columns:
        try:
            df[col] = encoder.transform(df[col].astype(str))
        except:
            df[col] = 0

# ---------------- ALIGN FEATURES ----------------
for col in feature_columns:
    if col not in df.columns:
        df[col] = 0

df = df[feature_columns]

# ---------------- PREDICTION ----------------
if st.button("🔮 Predict Claim Risk"):
    probability = model.predict_proba(df)[0][1]
    prediction = "HIGH RISK" if probability >= 0.4 else "LOW RISK"

    st.subheader("📊 Prediction Result")

    if prediction == "HIGH RISK":
        st.error(f"⚠ High chance of claim\n\nProbability: {probability:.2%}")
    else:
        st.success(f"✅ Low chance of claim\n\nProbability: {probability:.2%}")

    st.write("### ℹ What this means")
    st.write(
        "This prediction is based on patterns learned from historical insurance data. "
        "It is meant to **assist decision-making**, not replace human judgment."
    )
