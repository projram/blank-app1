import streamlit as st
import pandas as pd
import json
from utils import load_data, filter_data

st.set_page_config(page_title="Basic Data to JSON", layout="centered")

df = load_data("data.csv")

# Read URL query parameters
params = st.query_params

# If API mode is triggered via ?api=1
if params.get("api") == "1":
    # Get 'city' parameter; default to "All" if absent
    city = params.get("city", "All")
    filtered_df = filter_data(df, city)
    # Output raw JSON
    st.write(filtered_df.to_dict(orient="records"))
    st.stop()

# Otherwise, render the Streamlit UI
st.title("📊 Basic Data to JSON")
cities = ["All"] + sorted(df["city"].unique())
selected_city = st.sidebar.selectbox("City", cities)
filtered_df = filter_data(df, selected_city)

st.subheader("Filtered Data")
st.dataframe(filtered_df)

st.subheader("JSON Output")
json_str = filtered_df.to_json(orient="records", indent=2)
st.code(json_str, language="json")

st.download_button(
    label="Download JSON",
    data=json_str,
    file_name="data.json",
    mime="application/json"
)
