# 💳 Credit Card Fraud Detection System

A machine learning-powered web application for detecting fraudulent credit card transactions using multiple classification models.

## 🚀 Features

* Multi-page Streamlit Dashboard
* Credit Card Fraud Prediction
* Data Explorer
* Model Comparison Dashboard
* Confusion Matrix Visualization
* Feature Importance Analysis
* Dynamic Model Switching
* Fraud Probability Score
* Downloadable Prediction Reports
* Glassmorphism UI

## 🧠 Models Used

* XGBoost
* Random Forest

## 📊 Evaluation Metrics

* ROC-AUC Score
* Fraud Recall
* Confusion Matrix
* Feature Importance

## 📂 Project Structure

```text
notebooks/
│
├── app.py
│
├── pages/
│   ├── dashboard.py
│   ├── Prediction.py
│   ├── data_explorer.py
│   └── model_comparison.py
│
└── model/
    ├── xgboost/
    │   ├── model.pkl
    │   ├── X_test.pkl
    │   └── y_test.pkl
    │
    └── random_forest/
        ├── model.pkl
        ├── X_test.pkl
        └── y_test.pkl
```

## ⚙️ Installation

```bash
git clone <your-repo-url>
cd credit-card-fraud-detection

pip install -r requirements.txt

streamlit run notebooks/app.py
```

## 📈 Dashboard Pages

### Dashboard

Model overview, metrics, and system status.

### Prediction

Upload transaction data and predict fraudulent transactions.

### Data Explorer

Explore datasets, view statistics, and inspect features.

### Model Comparison

Compare machine learning models using confusion matrices and fraud recall scores.

## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-Learn
* XGBoost
* Pandas
* Matplotlib
* Seaborn

## 👨‍💻 Author

Prabhat Kumar Arya
