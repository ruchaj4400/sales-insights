import sys

import streamlit as st
import pandas as pd
from pathlib import Path

# Add src folder to Python path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from sales_insights.data_load import load_csv
from sales_insights.cleaning import basic_cleaning
from sales_insights import viz

st.set_page_config(page_title="Sales Insights Dashboard", layout="wide")
st.title("Sales Insights Dashboard")

# --- Load dataset ---
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    try:
        df = load_csv("../data/processed/sales_clean.csv")
    except FileNotFoundError:
        st.warning("No uploaded file or processed CSV found. Please upload a CSV.")
        st.stop()

# --- Clean data ---
df = basic_cleaning(df)

# --- Show dataframe ---
st.subheader("Data Preview")
st.dataframe(df.head())

# --- Summary stats ---
st.subheader("Summary Statistics")
st.write(df.describe(include="all"))

# --- Visualizations ---
st.subheader("Missing Values")
viz.plot_missing_values(df)

st.subheader("Correlation Heatmap")
viz.plot_correlation(df)
