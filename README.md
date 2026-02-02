Here’s a **clean, professional, and beginner-friendly `README.md`** for your project.
You can **directly copy–paste** this into your GitHub repo 👇

---

# 🛡 Insurance Claim Risk Prediction App

An **end-to-end Machine Learning web application** that predicts the **risk of an insurance claim** using **XGBoost**, and presents results through a **user-friendly Streamlit interface** designed for **non-technical users**.

---
🚀 **Project is live:** [Insurance Claim Risk Prediction App](https://insuranceclaimpredictiononimbalanceddata-9pipjuf7dpwtklpwephqb.streamlit.app/)

## 📌 Project Overview

Insurance companies face significant losses due to **fraudulent and high-risk claims**.
This project uses **machine learning** to predict whether a customer is likely to file an insurance claim, helping businesses:

* Reduce financial risk
* Prioritize investigations
* Make data-driven decisions

The app allows users to enter **approximate values** (even if they are unsure) and still get reliable predictions.

---

## 🚀 Features

* 🔮 Claim risk prediction using **XGBoost**
* ⚖ Handles **imbalanced data** using **SMOTE**
* 🧠 Feature engineering & categorical encoding
* 📊 Model evaluation (Precision, Recall, Confusion Matrix)
* 💼 Business impact analysis
* 🌐 **Streamlit web app** with beginner-friendly UI
* ❓ “Not sure” options for unknown inputs
* 📦 Saved model & encoders for reuse

---

## 🧠 Machine Learning Pipeline

1. Data loading & inspection
2. Data cleaning and preprocessing
3. Feature encoding using `LabelEncoder`
4. Handling class imbalance using **SMOTE**
5. Model training:

   * Random Forest (baseline)
   * **XGBoost (final model)**
6. Model evaluation & comparison
7. Feature importance analysis
8. Business impact calculation
9. Model deployment with Streamlit

---

## 🖥 Tech Stack

* **Python**
* **XGBoost**
* **Scikit-learn**
* **Imbalanced-learn (SMOTE)**
* **Pandas & NumPy**
* **Matplotlib & Seaborn**
* **Streamlit**
* **Joblib**

---

## 📁 Project Structure

```
├── app.py                     # Streamlit application
├── Insurance claims data.csv  # Dataset
├── xgb_claim_model.pkl        # Trained XGBoost model
├── label_encoders.pkl         # Saved encoders
├── feature_columns.pkl        # Feature order
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/insurance-claim-prediction.git
cd insurance-claim-prediction
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🧪 How to Use the App

1. Open the app in your browser
2. Enter basic customer and vehicle details
3. Use **sliders and dropdowns** (exact values not required)
4. Click **“Predict Claim Risk”**
5. View:

   * Claim probability
   * Risk level (High / Low)
   * Clear, human-readable explanation

---

## 📊 Output Example

* **Prediction:** High Risk
* **Claim Probability:** 68%
* **Meaning:** Customer has a higher likelihood of filing a claim

---

## 💼 Business Impact

The model helps:

* Catch high-risk claims early
* Reduce financial losses
* Optimize investigation costs

It demonstrates how **machine learning creates real business value**, not just predictions.

---

## 📈 Model Performance (XGBoost)

* **High Recall:** Captures most genuine claims
* **Balanced Precision:** Reduces false alarms
* Optimized using **custom probability threshold**

---

## 🔐 Disclaimer

This project is for **educational and demonstration purposes**.
Predictions should **support**, not replace, professional judgment.

---

## 👤 Author

**Krishna Gangeya Karbhari**
Fresher BE Computer Science Engineering
Focus: AI/ML • Data Science • Data Analysis

---


