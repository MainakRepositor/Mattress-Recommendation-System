"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Import necessary functions from web_functions
from web_functions import predict

hide_st_style = """
<style>
MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

def app(df, X, y):
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

    # Take input of features from the user.
    Stiffness = st.slider("Stiffness", int(df['Stiffness'].min()),int(df['Stiffness'].max()))
    Angle = st.slider("Angle", int(df["Angle"].min()), int(df["Angle"].max()))
    Rigidness = st.slider("Rigidness", int(df["Rigidness"].min()), int(df["Rigidness"].max()))
    Fluid = st.slider("Sinovial Fluid", int(df["Fluid"].min()), int(df["Fluid"].max()))
    Height = st.slider("Height", 70, 200)
    Peak = st.slider("Peak", int(df["Peak"].min()), int(df["Peak"].max()))
    Density = st.slider("Density", float(df["Density"].min()), float(df["Density"].max()))
    Comfort = st.slider("Comfort", float(df["Comfort"].min()), float(df["Comfort"].max()))
    Friction = st.slider("Friction", int(df["Friction"].min()), int(df["Friction"].max()))
    Muscle_turgidity = st.slider("Muscle_turgidity", float(df["Muscle_turgidity"].min()), float(df["Muscle_turgidity"].max()))
    Recoil = st.slider("Recoil", float(df["Recoil"].min()), float(df["Recoil"].max()))
   
      # Create a list to store all the features
    features = [Stiffness,Angle,Rigidness,Fluid,Height,Peak,Comfort,Friction,Density,Muscle_turgidity,Recoil]

    
    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score + 0.15 #correction factor
        x = round(prediction[0],2)
        st.write("Your predicted mattress score is:",x)

        if x < 10 or Stiffness > 100:
            st.error("You must change your mattress. Switch to a softer one.")
            st.markdown(
    f'<a href="https://www.amazon.in/s?k=soft+mattress&ref=nb_sb_noss" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: orange; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Buy Mattress</a>',
    unsafe_allow_html=True
)
        
        elif x > 10 and x < 20 or Stiffness > 50 and Stiffness < 100:
            st.success("You are in the Goldilocks Zone. We recommend heated mattress for you!")
            st.markdown(
    f'<a href="https://www.amazon.in/s?k=heating+mattress&ref=nb_sb_noss_2" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: orange; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Buy Mattress</a>',
    unsafe_allow_html=True
)
            
        elif Angle > 45:
            st.info("Recommended for you : Bi-curve / craddle mattress")
            st.markdown(
    f'<a href="https://www.amazon.in/s?k=adjustable+mattress&ref=nb_sb_ss_ts-doa-p_2_15" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: orange; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Buy Mattress</a>',
    unsafe_allow_html=True
)

        elif Friction > 25:
            st.info("Recommended for you : Linen-touch silken mattress")
            st.markdown(
    f'<a href="https://www.amazon.in/s?k=silken+mattress&ref=nb_sb_noss" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: orange; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Buy Mattress</a>',
    unsafe_allow_html=True
)

        elif Comfort > 0.80:
            st.info("Recommended for you: Maharaja Mattress, with extra soft finish and body shape auto-curvature with heating")
            st.markdown(
    f'<a href="https://www.amazon.in/s?k=smart+heating+mattress&ref=nb_sb_noss" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: orange; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Buy Mattress</a>',
    unsafe_allow_html=True
)

        else:
            st.warning("You must change to a harder one.")
            
        



        # Print teh score of the model 
        st.sidebar.write("The model used is trusted by doctor and has an accuracy of ", round((score*100),2),"%")
