import streamlit as st

# Page config MUST be first
st.set_page_config(
    page_title="SportsPropLab",
    page_icon="🏀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and subtitle
st.title("🏀 SportsPropLab")
st.subheader("NBA Prop Research prototype")

# Main content
st.markdown("""
Welcome to SportsPropLab! Your NBA prop research application.

### Features
- 📊 Data Analysis
- 🤖 ML Model Predictions
- 📈 Player Statistics
- 💡 Prop Recommendations
""")

# Simple metrics display
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Props", "0")
with col2:
    st.metric("Accuracy", "0%")
with col3:
    st.metric("ROI", "0%")

st.divider()
st.info("✨ More features coming soon!")
