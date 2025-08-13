import streamlit as st
import pandas as pd
import json
from utils import load_data, filter_data

st.set_page_config(page_title="Basic Data App", layout="centered")

st.title("📊 Basic Data to JSON")

# Load data
df = load_data("data.csv")

# Sidebar filters
st.sidebar.header("Filter Options")
cities = ["All"] + sorted(df["city"].unique())
selected_city = st.sidebar.selectbox("City", cities)

# Filtered data
filtered_df = filter_data(df, selected_city)

# Display table
st.subheader("Filtered Data")
st.dataframe(filtered_df)

# Convert to JSON
st.subheader("JSON Output")
json_str = filtered_df.to_json(orient="records", indent=2)
st.code(json_str, language="json")

# Option to download JSON
st.download_button(
    label="Download JSON",
    data=json_str,
    file_name="data.json",
    mime="application/json"
)
