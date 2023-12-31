"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st

# Import necessary functions from web_functions
from web_functions import load_data

# Configure the app
st.set_page_config(
    page_title = 'Sleeping Posture Based Mattress Recommendation',
    page_icon ='bed',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# Import pages
from Tabs import home, data, predict, sleep, visualise



# Dictionary for pages
Tabs = {
    "Home": home,
    "Data Info": data,
    "Prediction": predict,
    "Sleep": sleep,
    "Visualisation": visualise
    #"About me": about
}

# Create a sidebar
# Add title to sidear
st.sidebar.title("Navigation")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()

# Real time AQI measure
st.sidebar.markdown(
    f'<a href="https://stress-level-detector.streamlit.app/" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: orange; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Stress Level Analyzer</a>',
    unsafe_allow_html=True
)
