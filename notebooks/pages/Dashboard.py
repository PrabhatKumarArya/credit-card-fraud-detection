import streamlit as st

import streamlit as st


st.title("📈 Dashboard")

st.divider()

# Navigation Bar

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
    flex:column;
}
</style>
""", unsafe_allow_html=True)

# st.container(border=True)

nav1, nav2, nav3, nav4 = st.columns(4)

nav1.page_link("app.py", label="🏠 Home")
nav2.page_link("pages/Prediction.py", label="🔍 Prediction")
nav3.page_link("pages/data_explorer.py", label="📊 Explorer")
nav4.page_link("pages/model_comparison.py", label="🤖 Compare")

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


st.markdown("### Model Overview")

st.metric("ROC-AUC", "98.2%")
st.metric("Recall", "87%")

st.success("System Ready 🚀")

