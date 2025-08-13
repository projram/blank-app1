import streamlit as st
import pandas as pd
import json
import sys
from utils import load_data, filter_data

df = load_data("data.csv")

# Check if query params exist (for API mode)
params = st.experimental_get_query_params()

if "api" in params:
    # API Mode
    city = params.get("city", ["All"])[0]
    filtered_df = filter_data(df, city)
    st.write(filtered_df.to_dict(orient="records"))
    st.stop()

# Normal UI mode
st.title("📊 Basic Data to JSON")
cities = ["All"] + sorted(df["city"].unique())
selected_city = st.sidebar.selectbox("City", cities)
filtered_df = filter_data(df, selected_city)
st.dataframe(filtered_df)
st.subheader("JSON Output")
st.code(filtered_df.to_json(orient="records", indent=2), language="json")
