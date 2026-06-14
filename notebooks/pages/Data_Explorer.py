import streamlit as st
import pandas as pd

import streamlit as st

# Navigation Bar
st.title("📂 Data Explorer")

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
nav3.page_link("pages/Model_Comparison.py", label="🤖 Compare")
nav4.page_link("pages/Prediction.py", label="🔍 Prediction")

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

uploaded_file = st.file_uploader(
    "Upload dataset",
    type=["csv"],
    accept_multiple_files=False   # IMPORTANT FIX
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # FORCE SINGLE DATASET VIEW (clear old state issue)
    st.session_state["df"] = df

    st.subheader("Shape")
    st.write(df.shape)

    st.subheader("Preview")
    st.dataframe(df.head(), use_container_width=True)

    st.subheader("Summary")
    st.write(df.describe())

else:
    st.info("Upload a file to view data")