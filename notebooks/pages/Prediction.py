import streamlit as st
import joblib
import os
import pandas as pd

st.set_page_config(page_title="Prediction Page", layout="wide")

st.divider()

st.title("🔍 Fraud Prediction System")

st.markdown("""
<style>
.nav-box{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 15px;
    padding: 15px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# st.container(border=True)

nav1, nav2, nav3, nav4 = st.columns(4)

nav1.page_link("App.py", label="🏠 Home")
nav2.page_link("pages/dashboard.py", label="📈 Dashboard")
nav3.page_link("pages/data_explorer.py", label="📊 Explorer")
nav4.page_link("pages/model_comparison.py", label="🤖 Compare")


st.markdown("---")

st.markdown("""
<style>
section[data-testid="stSidebar"]{
    display:none;
}
            
/* Top-left hamburger/menu button hide */
button[kind="header"]{
    display:none;
}

/* Header hide */
header[data-testid="stHeader"]{
    display:none;
}

[data-testid="collapsedControl"] {
    display: none;
}       

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

body {
    background: #0e1117;
}

/* Glass Card */
.glass-card {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 18px;
    padding: 20px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    transition: 0.3s ease;
}

.glass-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(0,198,255,0.25);
}

/* Big numbers */
.glass-value {
    font-size: 2rem;
    font-weight: bold;
    color: #00c6ff;
    text-align: center;
    margin-bottom:10px;
}

/* Labels */
.glass-label {
    font-size: 1rem;
    color: #ccc;
    text-align: center;
}

/* Sidebar glass */
section[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(15px);
    border-right: 1px solid rgba(255,255,255,0.1);
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# MODEL SELECT
# -------------------------

MODEL_DIR = "notebooks/model"

model_folders = {
    "XGBoost": "xgboost",
    "Random Forest": "random_forest"
}

selected_model = st.selectbox(
    "🤖 Choose Model",
    list(model_folders.keys())
)

folder = model_folders[selected_model]

model_path = os.path.join(MODEL_DIR, folder, "model.pkl")
model = joblib.load(model_path)

st.success(f"Loaded Model: {selected_model}")

# -------------------------
# FILE UPLOAD
# -------------------------
uploaded_file = st.file_uploader("📂 Upload CSV file", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Data Preview")
    st.dataframe(df.head())

    # -------------------------
    # PREDICTION
    # -------------------------
    if st.button("🔍 Predict Now"):

        preds = model.predict(df)
        probs = None
        if hasattr(model, "predict_proba"):
            probs = model.predict_proba(df)[:, 1]
        
        df["Prediction"] = preds
        df["Result"] = df["Prediction"].apply(
            lambda x: "🚨 Fraud" if x == 1 else "✅ Legit"
        )

        if probs is not None:
            df["Fraud Probability (%)"] = probs * 100

        st.subheader("📈 Prediction Results")

        # st.dataframe(df)

        # -------------------------
        # SUMMARY
        # -------------------------
        fraud_count = (df["Prediction"] == 1).sum()
        total = len(df)
        fraud_pct = (fraud_count / total) * 100

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
            <div class="glass-card">
                <div class="glass-value">{total}</div>
                <div class="glass-label">Total Transactions</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="glass-card">
                <div class="glass-value">{fraud_count}</div>
                <div class="glass-label">Fraud Detected</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="glass-card">
                <div class="glass-value">{fraud_pct:.2f}%</div>
                <div class="glass-label">Fraud Rate</div>
            </div>
            """, unsafe_allow_html=True)

else:
    st.info("Upload a CSV file to start prediction")