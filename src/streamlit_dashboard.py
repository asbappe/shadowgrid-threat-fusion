import streamlit as st
import pandas as pd

data = [
    {"Threat": "CVE-2024-1234", "Score": 9.8, "Reasoning": "High severity with active exploit", "Source": "NVD"},
    {"Threat": "MOVEit Vulnerability", "Score": 8.5, "Reasoning": "Exploited in recent campaign", "Source": "BleepingComputer"},
]

df = pd.DataFrame(data)
st.title("ShadowGrid Threat Fusion")
st.dataframe(df, use_container_width=True)
