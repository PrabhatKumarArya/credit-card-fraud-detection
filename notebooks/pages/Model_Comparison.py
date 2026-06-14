import streamlit as st
import joblib
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


st.title("🤖 Model Comparison Dashboard")
st.divider()

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
nav2.page_link("pages/Dashboard.py", label="📈 Dashboard")
nav3.page_link("pages/Prediction.py", label="🔍 Prediction")
nav4.page_link("pages/Data_Explorer.py", label="📊 Explorer")

st.divider()

st.markdown("""
<style>

body {
    background: #0e1117;
}
            
/* Sidebar glass */
section[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(15px);
    border-right: 1px solid rgba(255,255,255,0.1);
}

</style>
""", unsafe_allow_html=True)


MODEL_DIR = "notebooks/model"

model_folders = {
    "XGBoost": "xgboost",
    "Random Forest": "random_forest"
}

# -------------------------
# COMPUTE SCORES ONCE
# -------------------------
scores = {}
cms = {}

for name, folder in model_folders.items():

    model = joblib.load(f"{MODEL_DIR}/{folder}/model.pkl")
    X_test = joblib.load(f"{MODEL_DIR}/{folder}/X_test.pkl")
    y_test = joblib.load(f"{MODEL_DIR}/{folder}/y_test.pkl")

    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)

    cms[name] = cm

    tn, fp, fn, tp = cm.ravel()
    recall = tp / (tp + fn + 1e-9)

    scores[name] = recall

# -------------------------
# BEST MODEL
# -------------------------
best_model = max(scores, key=scores.get)

st.subheader("📊 Recall Scores") 
st.dataframe(scores)

st.success(f"🏆 Best Model: {best_model}")

# -------------------------
# CONFUSION MATRICES (SIDE BY SIDE)
# -------------------------
cols = st.columns(len(cms))

for i, (name, cm) in enumerate(cms.items()):

    fig, ax = plt.subplots(figsize=(5,4))

    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)

    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")

    title = f"{name}"
    if name == best_model:
        ax.set_title(f"{name} (BEST)", color="green")
    else:
        ax.set_title(name)

    # ax.set_title(title)

    cols[i].pyplot(fig)