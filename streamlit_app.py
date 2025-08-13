import streamlit as st
import uvicorn
from fastapi import FastAPI
import threading

# FastAPI instance
api = FastAPI()

@api.get("/api/data")
def get_data():
    return {"message": "Hello from API", "status": "success"}

# Run FastAPI in a separate thread
def run_api():
    uvicorn.run(api, host="0.0.0.0", port=8001)

# Start API server
threading.Thread(target=run_api, daemon=True).start()

# Streamlit app
st.title("My App with API")
