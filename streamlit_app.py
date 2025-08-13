import streamlit as st
import json

# Get query parameters
query_params = st.query_params

# API endpoint simulation
if query_params.get("api") == "data":
    # Your API logic here
    response_data = {
        "message": "Hello from API", 
        "status": "success",
        "timestamp": "2024-01-01T00:00:00Z"
    }
    
    # Display as JSON (this is what the user will see)
    st.json(response_data)
    st.stop()

elif query_params.get("api") == "users":
    # Another endpoint example
    users_data = {
        "users": [
            {"id": 1, "name": "John"},
            {"id": 2, "name": "Jane"}
        ]
    }
    st.json(users_data)
    st.stop()

# Regular Streamlit UI
st.title("My App with API")
st.write("Available endpoints:")
st.write("- `?api=data` - Get sample data")
st.write("- `?api=users` - Get users list")
