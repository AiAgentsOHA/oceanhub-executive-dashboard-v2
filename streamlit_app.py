"""
OceanHub Africa OH7 Executive Dashboard
4 Tabs: EiR Portfolios | Next Steps | Pipeline Analytics | Data Insights

Features:
- EiR portfolio management with "Move to Adjudication 2" button
- Categorized Next Steps outreach (5 priority levels)
- Pipeline analytics with dual conversion rates
- MEL metrics and portfolio composition analysis
- Email tracking with team member attribution

Run: streamlit run streamlit_executive_dashboard.py
"""
import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="OceanHub OH7 Dashboard",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    #MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {display: none !important; visibility: hidden !important;}
    .stApp > header {display: none !important;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    .stApp {background: #0B1426 !important;}
    iframe {border: none !important;}
</style>
""", unsafe_allow_html=True)

paths = [
    'oceanhub_executive_dashboard.html',
    './oceanhub_executive_dashboard.html',
    '/mnt/user-data/outputs/oceanhub_executive_dashboard.html'
]

for p in paths:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            components.html(f.read(), height=920, scrolling=True)
        break
else:
    st.error("Dashboard not found. Place 'oceanhub_executive_dashboard.html' in the same directory.")
