import streamlit as st
import pandas as pd
import time
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# Storing timestamp and date of attendance
ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M %p")

# Streamlit auto refresh for application after 1 second
count = st_autorefresh(interval=1000, limit=100, key="fizzbuzzcounter")

# Display logic during refresh (can be customized)
if count == 0:
    st.write("Welcome to the Attendance Tracker!")
elif count % 3 == 0 and count % 5 == 0:
    st.write("Refresh in progress...")
else:
    st.write("Real-time updates enabled.")

# Load attendance data
try:
    df = pd.read_csv(f"attendance/Attendance_{date}.csv")
    # Display attendance DataFrame
    st.dataframe(df.style.highlight_max(
        axis=0, props="background-color: #FFF9BB; color: #31333F;"))
except FileNotFoundError:
    st.write(f"No attendance file found for {date}.")
