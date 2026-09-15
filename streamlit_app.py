import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="SportsPropLab", layout="wide")

st.title("🏀 SportsPropLab")
st.subtitle("NBA Prop Research prototype (Streamlit + ETL + model)")

st.markdown("""
Welcome to SportsPropLab! This is your NBA prop research application.

### Features
- 📊 Data Analysis
- 🤖 ML Model Predictions
- 📈 Player Statistics
- 💡 Prop Recommendations

---
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Props", "0", delta="Coming Soon")
with col2:
    st.metric("Accuracy", "0%", delta="Coming Soon")
with col3:
    st.metric("ROI", "0%", delta="Coming Soon")

st.info("🚀 More features coming soon! Configure your data pipeline and models in the sidebar.")
