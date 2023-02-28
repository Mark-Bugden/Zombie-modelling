import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


st.title('Zombie Modelling')

st.markdown("""
This app shows the results of mathematical modelling of a fictional Zombie Outbreak in various countries around the world. 
* **Python libraries:** 
* **Data source:** 
""")

st.sidebar.header('Choose your country')



# -- Create sidebar for plot controls
st.sidebar.markdown('## Choose your country')
selected_country = st.selectbox(
        "Which country would you like to view?",
        ("Czechia", "Germany", "Other"),
        label_visibility="visible"
    )







st.header('Display Companies in Selected Sector')
st.write('Testing')






num_zombies = st.sidebar.slider('Number of Zombies', 1, 5)


