import streamlit as st

import streamlit as st

st.set_page_config(
    page_title="Fraud Detection System",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("💳 Credit Card Fraud Detection System")
st.divider()

st.markdown("## 🚀 Quick Navigation")

col1, col2 = st.columns(2)

with col1:
    st.page_link(
        "pages//Dashboard.py",
        label="Dashboard",
        icon="📈"
    )

    st.page_link(
        "pages/Prediction.py",
        label="Prediction",
        icon="🔍"
    )

with col2:
    st.page_link(
        "pages/Data_Explorer.py",
        label="Data Explorer",
        icon="📊"
    )

    st.page_link(
        "pages/Model_Comparison.py",
        label="Model Comparison",
        icon="🤖"
    )

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
            
# import pandas as pd
# import joblib
# import matplotlib.pyplot as plt 
# import zipfile

# # Page Config
# st.set_page_config(
#     page_title="Fraud Detection Dashboard",
#     page_icon="💳",
#     layout="wide"
# )

# st.markdown("""
# <style>

# .metric-card {
#     background: rgba(255,255,255,0.08);
#     backdrop-filter: blur(12px);
#     border: 1px solid rgba(255,255,255,0.15);
#     border-radius: 18px;
#     padding: 25px;
#     text-align: center;
#     box-shadow: 0 8px 20px rgba(0,0,0,0.2);
#     margin-bottom: 20px;
#     min-height: 140px;

#     display: flex;
#     flex-direction: column;
#     justify-content: center;
#     align-items: center;
#     flex-wrap: wrap;
# }

# .metric-value {
#     font-size: 2rem;
#     font-weight: bold;
#     color: #00c6ff;
# }

# .metric-label {
#     font-size: 1rem;
#     color: #cccccc;
# }
            
# section[data-testid="stSidebar"] {
#     background: linear-gradient(
#         180deg,
#         rgba(0,198,255,0.12),
#         rgba(0,114,255,0.08)
#     );
#     backdrop-filter: blur(12px);
#     border-right: 1px solid rgba(255,255,255,0.1);
# }

# .sidebar-card {
#     background: rgba(255,255,255,0.08);
#     border: 1px solid rgba(255,255,255,0.15);
#     border-radius: 16px;
#     padding: 15px;
#     margin-bottom: 15px;
#     text-align: center;
# }

# .sidebar-title {
#     color: #00c6ff;
#     font-size: 1.2rem;
#     font-weight: bold;
# }

# .sidebar-value {
#     color: white;
#     font-size: 1rem;
# }

# .risk-card {
#     border-radius: 20px;
#     padding: 25px;
#     background: linear-gradient(
#         135deg,
#         rgba(0,198,255,0.15),
#         rgba(0,114,255,0.15)
#     );
#     border: 1px solid rgba(0,198,255,0.3);
#     margin-bottom: 20px;
# }

# .summary-card {
#     background: linear-gradient(
#         135deg,
#         rgba(0,198,255,0.15),
#         rgba(0,114,255,0.15)
#     );
#     border: 1px solid rgba(0,198,255,0.3);
#     border-radius: 20px;
#     padding: 25px;
#     text-align: center;
#     margin-bottom: 20px;
# }

# .summary-title {
#     font-size: 1rem;
#     color: #cccccc;
# }

# .summary-value {
#     font-size: 2rem;
#     font-weight: bold;
#     color: #00c6ff;
# }

# </style>
# """, unsafe_allow_html=True)

# model_files = {
#     "XGBoost": "xgboost_detection_model.pkl",
#     "Random Forest": "random_forest_classifier_model.pkl",
# }

# # Load Model
# import os
# import joblib

# models = {}
# MODEL_DIR = "notebooks/model"

# import joblib

# X_test = joblib.load(os.path.join(MODEL_DIR,"X_test.pkl"))
# y_test = joblib.load(os.path.join(MODEL_DIR,"y_test.pkl"))

# for name, file in model_files.items():
#     path = os.path.join(MODEL_DIR, file)
#     models[name] = joblib.load(path)

# from sklearn.metrics import confusion_matrix

# cms = {}
# scores = {}

# for name, model in models.items():
#     y_pred = model.predict(X_test)
#     cm = confusion_matrix(y_test, y_pred)
    
#     cms[name] = cm
    
#     # simple score = recall of fraud class (better metric for fraud)
#     tn, fp, fn, tp = cm.ravel()
#     recall = tp / (tp + fn + 1e-9)
    
#     scores[name] = recall

# best_model = max(scores, key=scores.get)

# import matplotlib.pyplot as plt
# import seaborn as sns

# st.subheader("📊 Model Comparison - Confusion Matrices")

# cols = st.columns(len(models))

# for i, (name, cm) in enumerate(cms.items()):
#     fig, ax = plt.subplots()

#     sns.heatmap(
#         cm,
#         annot=True,
#         fmt="d",
#         cmap="Blues",
#         ax=ax
#     )

#     ax.set_title(name)

#     # highlight best model
#     if name == best_model:
#         ax.set_title(f"🏆 {name} (BEST)", color="green")

#     cols[i].pyplot(fig)



# selected_model = st.sidebar.selectbox(
#     "🤖 Choose Model",
#     list(model_files.keys())
# )



# model_path = os.path.join(MODEL_DIR, model_files[selected_model])
# model = joblib.load(model_path)

# # Header
# st.markdown(f"""
# <div style="
# padding:30px;
# border-radius:20px;
# background:linear-gradient(135deg,#00c6ff22,#0072ff22);
# border:1px solid rgba(0,198,255,0.3);
# margin-bottom:20px;
# ">
# <h1>💳 Credit Card Fraud Detection System</h1>
# <p>{selected_model} | SMOTE Applied | ROC-AUC: 98.2% | Recall: 87%</p>
# </div>
# """, unsafe_allow_html=True)

# # Metrics
# col1, col2, col3 = st.columns(3)

# st.markdown(f"""
# <div style="
# padding:15px;
# border-radius:12px;
# background:rgba(0,255,100,0.1);
# border:1px solid rgba(0,255,100,0.3);
# text-align:center;
# margin-top:10px;
# margin-bottom:10px;
# ">
# <h3>🏆 Best Model: {best_model}</h3>
# <p>Based on Fraud Recall Score</p>
# </div>
# """, unsafe_allow_html=True)

# with col1:
#     st.markdown("""
#         <div class="metric-card">
#             <h1 style="color:#00c6ff;">98.2%</h1>
#             <p>ROC-AUC</p>
#         </div>
#     """, unsafe_allow_html=True)
    



# with col2:
#     st.markdown("""
#     <div class="metric-card">
#         <h1 style="color:#00c6ff;">87%</h1>
#         <p>Fraud Recall</p>
#     </div>
#     """, unsafe_allow_html=True)

# with col3:
#     st.markdown(f"""
#     <div class="metric-card">
#         <h1 style="color:#00c6ff;">{selected_model}</h1>
#         <p>Model</p>
#     </div>
#     """, unsafe_allow_html=True)

# # Sidebar
# with st.sidebar:

#     st.markdown(f"""
#     <div class="sidebar-card">
#         <div class="sidebar-title">{selected_model}</div>
#         <div class="sidebar-value">SELECTED MODEL</div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#     <div class="sidebar-card">
#         <div class="sidebar-title">🎯 ROC-AUC</div>
#         <div class="sidebar-value">98.2%</div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#     <div class="sidebar-card">
#         <div class="sidebar-title">📈 Recall</div>
#         <div class="sidebar-value">87%</div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#     <div class="sidebar-card">
#         <div class="sidebar-title">⚡ SMOTE</div>
#         <div class="sidebar-value">Applied</div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#         <div class="sidebar-card">
#             <div class="sidebar-title">🚀 Status</div>
#             <div class="sidebar-value">Production Ready</div>
#         </div>
#     """, unsafe_allow_html=True)

# # File Upload
# uploaded_file = st.file_uploader(
#     "📂 Upload Transaction CSV",
#     type=["csv"]
# )

# if uploaded_file is not None:

#     df = pd.read_csv(uploaded_file)

#     c1, c2, c3 = st.columns(3)

#     with c1:
#         st.metric("Transactions", f"{len(df):,}")

#     with c2:
#         st.metric("Features", len(df.columns))

#     with c3:
#         if "Class" in df.columns:
#             st.metric(
#                 "Fraud Cases",
#                 int(df["Class"].sum())
#             )

#     st.subheader("Dataset Preview")
#     st.dataframe(df.head())

#     row = st.slider(
#         "Select Transaction",
#         min_value=0,
#         max_value=len(df) - 1,
#         value=0
#     )

#     sample = df.iloc[[row]]

#     if st.button("🔍 Analyze Transaction"):

#         input_data = sample.copy()

#         if "Class" in input_data.columns:
#             input_data = input_data.drop("Class", axis=1)

#         prediction = model.predict(input_data)[0]
#         probability = model.predict_proba(input_data)[0][1]

#         st.markdown(f"""
#             <div class="summary-card">
#                 <div class="summary-title">Prediction Summary</div>
#                 <div class="summary-value">
#                         {"🚨 FRAUD DETECTED" if prediction == 1 else "✅ LEGITIMATE"}
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)

#         left, right = st.columns([2, 1])

#         with left:
#             st.subheader("Transaction Details")
#             st.dataframe(sample, width="content")

#         with right:

#             st.markdown(f"""
#                 <div class="risk-card">
#                 <h3>Risk Score</h3>
#                 <h1>{probability*100:.2f}%</h1>
#                 </div>
#             """, unsafe_allow_html=True)

#             st.progress(int(probability * 100))

#             if prediction == 1:
#                 st.error("🚨 Fraud Detected")
#             else:
#                 st.success("✅ Legitimate Transaction")


#         importance_df = pd.DataFrame({
#             "Feature": input_data.columns,
#             "Importance": model.feature_importances_
#         })

#         importance_df = importance_df.sort_values(
#             by="Importance",
#             ascending=False
#         )

#         top10 = importance_df.head(10).sort_values(
#             by="Importance",
#             ascending=True
#         )

#         fig,ax = plt.subplots(figsize=(8, 5))

#         bars = ax.barh(
#             top10["Feature"],
#             top10["Importance"]
#         )

#         for bar in bars: 
#             width = bar.get_width()
#             ax.text(
#                 width,
#                 bar.get_y() + bar.get_height()/2,
#                 f"{width:.3f}",
#                 va="center"
#             )

#         ax.set_title("Top 10 Important Features")
#         ax.set_xlabel("Importance Score")

#         plt.tight_layout()

#         chart_col, table_col = st.columns([2,1])

#         with chart_col:
#             st.subheader("📈 Feature Importance")
#             st.pyplot(fig)

#         with table_col:
#             st.subheader("🏆 Top Features")
#             st.dataframe(
#                 top10.sort_values(
#                     by="Importance",
#                     ascending=False
#                 ),
#                 width="stretch"
#             )
#         report = pd.DataFrame({
#             "Prediction": ["Fraud" if prediction == 1 else "Legitimate"],
#             "Fraud Probability (%)": [round(probability * 100, 2)]
#         })

#         csv = report.to_csv(index=False)

#         st.download_button(
#             label="📥 Download Report",
#             data=csv,
#             file_name="fraud_report.csv",
#             mime="text/csv"
#         )

# else:
#     st.info("📂 Upload a CSV file to begin analysis.")


# st.markdown("---")

# st.markdown(
#     """
#     <center>
#     💳 Credit Card Fraud Detection System | 🧠 Machine Learning Powered
#     </center>
#     """,
#     unsafe_allow_html=True
# )