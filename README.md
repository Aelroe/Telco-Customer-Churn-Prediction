# Telco Customer Churn Prediction
<img width="200" height="200" alt="UTA-DataScience-Logo " src="https://github.com/user-attachments/assets/6f23af37-1bac-426f-b259-95a5499258b1" />


## Business Problem / Motivation

Customer churn is a major challenge in the telecom industry because it directly impacts long-term revenue. Companies rely on recurring payments, so when customers leave, it creates a continuous loss that is more expensive to recover from than preventing in the first place.

The goal of this project is to predict which customers are at risk of churning so that the company can take proactive action, such as targeted retention offers or improved customer support.

From a business perspective, solving this problem allows companies to shift from reactive strategies to data-driven decision-making, helping reduce costs and improve customer retention.

From a data science perspective, this project demonstrates how machine learning can be used to turn historical customer data into actionable insights. Instead of simply analyzing past behavior, the model provides forward-looking predictions that can support real-world decisions.

Overall, this project connects technical modeling with real business impact by transforming customer data into a practical tool for predicting and reducing churn.

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
## Data Preprocessing

To prepare the dataset for modeling, several cleaning and transformation steps were applied.

### Cleaning
- Converted `TotalCharges` to numeric, revealing 11 missing values  
- These corresponded to customers with zero tenure, so they were removed (~0.16% of data)  
- Dropped `customerID` as it has no predictive value  

### Missing Values
- Removed rows with missing `TotalCharges`  
- No additional imputation was needed  

### Encoding
- Simplified categories like `'No internet service'` → `'No'`  
- Binary variables encoded as 0/1  
- Multi-class features one-hot encoded  
- Target (`Churn`) converted to binary (1/0)  

### Scaling
- Applied StandardScaler (fit on training data only to avoid leakage)  

### Class Imbalance
- Dataset is imbalanced (~26.5% churn)  
- Used SMOTEENN on training data only  

### Train-Test Split
- 80/20 split with stratification to preserve churn distribution

---
## Exploratory Data Analysis (EDA)

Exploratory data analysis was conducted to identify patterns and key factors influencing customer churn.

### Churn Distribution
![Churn Distribution](image1.png)

- The dataset is imbalanced, with about 26.5% of customers churning  
- This confirms the need for imbalance handling techniques during modeling  

### Churn Rate by Key Features
![Churn by Features](image2.png)

- Certain features, such as contract type, internet service, and payment method, show clear differences in churn rates  
- Customers with month-to-month contracts and electronic payments tend to churn more  
- This highlights the importance of service and billing-related features  

### Tenure Group vs Churn
![Tenure vs Churn](image3.png)

- Customers with shorter tenure are much more likely to churn  
- Longer-tenure customers are more stable and less likely to leave  
- This suggests customer loyalty increases over time  

### Key Insights
- Short-term customers are at the highest risk of churn  
- Contract type and payment behavior strongly influence churn  
- Class imbalance must be handled carefully for accurate predictions

---
## Modeling Approach

To predict customer churn, a baseline model and an advanced model were compared.

### Baseline Model
- Logistic Regression was used as a simple starting point  
- Provides a clear benchmark for performance  

### Advanced Model
- XGBoost was selected as the final model  
- Captures more complex patterns in the data  

### Why XGBoost
- Handles non-linear relationships better  
- More effective with feature interactions  
- Performed better across key metrics (ROC-AUC, F1, recall)  

### Model Selection
- XGBoost outperformed the baseline model  
- Chosen for deployment due to stronger overall performance

---
## Model Training

### Tools Used
- Python (pandas, NumPy)
- scikit-learn
- XGBoost

### Training Process
- Data was split into training and testing sets (80/20, stratified)
- Preprocessing steps (encoding, scaling) were applied
- SMOTEENN was used on the training data to handle class imbalance
- Models were trained and evaluated on the test set

### Hyperparameters
- XGBoost hyperparameters were tuned to improve performance
- Focus was on optimizing recall and overall model stability


---
## Results

### Evaluation Metrics
- ROC-AUC: ~0.82  
- F1 Score (churn): ~0.62  
- Recall: ~0.79  
- Decision Threshold: ~0.43  

### Why These Metrics
- ROC-AUC measures overall model performance  
- Recall is important to capture as many churn cases as possible  
- F1 score balances precision and recall  

### Model Performance
- XGBoost outperformed the baseline model across all key metrics  
- Higher recall ensures fewer high-risk customers are missed  

### Key Takeaway
- The model is effective at identifying customers at risk of churn  
- It is better suited for business use where missing churn cases is costly


---
## Key Insights

- Contract type is the strongest predictor — month-to-month customers churn the most  
- Tenure is critical — newer customers are much more likely to leave  
- Service features matter — lack of tech support and online security increases churn  
- Billing behavior also plays a role — higher charges and paperless billing link to higher churn  

### Business Impact
- The model helps identify high-risk customers early  
- Enables targeted retention strategies (offers, support, incentives)  
- Reduces revenue loss by focusing on customers most likely to churn


---
## Conclusion

This project successfully developed a machine learning model to predict customer churn.

The XGBoost model achieved strong performance and was deployed into an interactive Streamlit app, making it usable in real-world scenarios.

Overall, the project demonstrates how data can be used to support proactive decision-making and reduce customer loss.

---
## Future Work

- Improve model performance with additional features or external data  
- Explore deep learning or ensemble methods  
- Incorporate real-time data for live predictions  
- Enhance deployment with user tracking or dashboards

---
## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run the Streamlit app:
   streamlit run app.py

3. Open the app in your browser and input customer data to get predictions

---
## Repository Structure

- `README.md` — project overview and documentation
- `app.py` — Streamlit deployment app
- `Telco_Churn_CapstoneFinal.ipynb` — full analysis, modeling, and evaluation notebook
- `churn_model_deployment.pkl` — saved trained model and preprocessing objects
- `images/` — visualizations used in the README
- `requirements.txt` — required Python libraries

---

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
