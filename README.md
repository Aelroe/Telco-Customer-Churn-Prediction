# Telco Customer Churn Prediction
<img width="200" height="200" alt="UTA-DataScience-Logo " src="https://github.com/user-attachments/assets/6f23af37-1bac-426f-b259-95a5499258b1" />


## Business Problem

Customer churn is one of the biggest challenges for telecom companies. Losing customers directly impacts revenue, and acquiring new customers is significantly more expensive than retaining existing ones.

The goal of this project is to predict which customers are at risk of leaving the company so that the business can take proactive retention actions.

If this problem is ignored:
- High-value customers may leave without warning
- Retention strategies become reactive instead of proactive
- Marketing and retention costs increase significantly

---

## Project Overview

This project builds a machine learning model to predict customer churn using demographic, service usage, and billing data.

The workflow includes:
- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Model training and evaluation
- Model interpretation (SHAP)
- Deployment as an interactive Streamlit application

Final Model:
- Model: XGBoost
- ROC-AUC: ~0.82
- F1 Score (churn): ~0.62
- Recall: ~0.79
- Optimized threshold: 0.43

The model is deployed into a user-friendly application where users can input customer information and receive churn predictions in real time.

---

## Data

Dataset Source:
- Kaggle: Telco Customer Churn Dataset

Key characteristics:
- ~7,000 customers
- Target variable: Churn (Yes/No)
- Features include:
  - Demographics (gender, senior citizen)
  - Account info (tenure, contract type)
  - Services (internet, tech support, streaming)
  - Billing (monthly charges, total charges, payment method)

Churn rate:
- ~26.5% (imbalanced dataset)

---
