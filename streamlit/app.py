import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import base64
from PIL import Image




st.title('Zombie Modelling')

st.markdown("""
This app shows the results of mathematical modelling of a fictional Zombie outbreak in various countries around the world. 
""")

st.sidebar.header('Choose your country')



# -- Create sidebar for plot controls
selected_country = st.sidebar.selectbox(
        "Which country would you like to view?",
        ("Czechia", "Germany", "Other")
    )
st.write('You selected:', selected_country)

#Doesn't accept avif files
#image = Image.open("streamlit/app_imgs/test.png")


file = open(r"movies/movie.gif", 'rb')
contents = file.read()
data_url = base64.b64encode(contents).decode('utf-8-sig')
file.close()
st.markdown(f'<img src="data:image/gif;base64,{data_url}>',unsafe_allow_html = True)


#st.image(image, caption='Test image')










num_zombies = st.sidebar.slider('Number of Zombies', 1, 5)


