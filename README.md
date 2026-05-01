# Telco Customer Churn Prediction
<img width="200" height="200" alt="UTA-DataScience-Logo " src="https://github.com/user-attachments/assets/6f23af37-1bac-426f-b259-95a5499258b1" />


## Business Problem

Customer churn is a major challenge in the telecom industry. When customers leave, companies lose recurring revenue and must spend significantly more to acquire new customers than to retain existing ones.

The goal of this project is to identify customers who are at high risk of churning so the business can take proactive retention actions.

If this problem is not addressed:
- High-value customers may leave without warning  
- Retention efforts become reactive instead of targeted  
- Marketing and operational costs increase  

---

## Project Overview

This project develops a machine learning solution to predict customer churn using demographic, service usage, and billing data.

The workflow includes:
- Data cleaning and preprocessing  
- Exploratory data analysis (EDA)  
- Model training and evaluation  
- Model interpretation using SHAP  
- Deployment as an interactive Streamlit application  

Final Model Performance:
- Model: XGBoost  
- ROC-AUC: ~0.82  
- F1 Score (churn): ~0.62  
- Recall: ~0.79  
- Optimized threshold: 0.43  

The final model is deployed into an interactive application that allows users to input customer information and receive real-time churn predictions. This demonstrates not just model accuracy, but real-world usability.

---

## Data

Dataset Source:
- Kaggle: Telco Customer Churn Dataset  
  https://www.kaggle.com/datasets/blastchar/telco-customer-churn  

This dataset was originally provided by IBM and is widely used for churn prediction tasks.

Key Characteristics:
- ~7,000 customer records  
- 21 features + 1 target variable (Churn)  
- Binary classification problem (Yes/No)  
- Imbalanced dataset (~26.5% churn rate)  

Feature Categories:
- Demographics: gender, senior citizen, partner, dependents  
- Account information: tenure, contract type, payment method  
- Services: phone, internet, tech support, streaming  
- Billing: monthly charges, total charges  

Each row represents a customer, and the target variable indicates whether the customer left the company within the last month. :contentReference[oaicite:0]{index=0}

---
