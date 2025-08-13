import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """Load CSV data into a DataFrame."""
    return pd.read_csv(filepath)

def filter_data(df: pd.DataFrame, city: str) -> pd.DataFrame:
    """Filter data by city if specified."""
    if city and city != "All":
        return df[df["city"] == city]
    return df
