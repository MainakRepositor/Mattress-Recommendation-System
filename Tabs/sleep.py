"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

import streamlit.components.v1 as components



hide_st_style = """
<style>
MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

def app():
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Regression</b> for the Recommendation of Best Type of Mattress for your bed.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    matt = st.number_input('Enter Mattress Score', value=1)
    stress = st.number_input('Enter Stress Level', value=0)

    # Display the entered numbers
    st.write(f'Mattress Score: {matt}')
    st.write(f'Stress Score: {stress}')
    sleep = round ((stress / matt),2)*100
    st.info(f'Your sleeping score is: {sleep}')

    if (sleep < 7): st.error("Time to change mattress")
    else: st.success("Good sleep")
