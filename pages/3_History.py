import streamlit as st
import pandas as pd
from pathlib import Path

st.title("📜 Prediction History")

history_file = Path(__file__).parent.parent / "prediction_history.csv"

st.write("Path:", history_file)

if not history_file.exists():
    st.warning("History file not found.")
else:
    try:
        history_df = pd.read_csv(history_file)
        
        st.dataframe(history_df, use_container_width=True)
        st.write("Rows:", len(history_df))

      
    except pd.errors.EmptyDataError:
        st.warning("History file is empty.")
    except Exception as e:
        st.error(f"Error reading file: {e}")