# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 17:14:46 2022

@author: mohan
"""

import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading in the model to predict on the data
pickle_in = open('Best_Model.pkl', 'rb')
model = pickle.load(pickle_in)

def welcome():
    return 'welcome all'

# defining the function which will make the prediction using
# the data which the user inputs
def prediction(carat,cut,color,clarity,depth,table,x,y,z):

    prediction = model.predict(
        [[carat,cut,color,clarity,depth,table,x,y,z]])
    print(prediction)
    return prediction
    

# this is the main function in which we define our webpage
def main():    
    # giving the webpage a title
    st.title("Gemstone Price Prediction")
    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    #html_temp = """
    #<div style ="background-color:yellow;padding:13px">
    #<h1 style ="color:black;text-align:center;">Streamlit Iris Flower Classifier ML App </h1>
    #</div>
    #"""
    
    # this line allows us to display the front end aspects we have
    # defined in the above code
    #st.markdown(html_temp, unsafe_allow_html = True)
    
    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    carat = st.number_input("Carat",min_value=0.01,max_value=1.00,step=0.01)
    cut = st.selectbox("Cut",["Good","Very Good","Ideal","Premium"])
    color = st.selectbox("Color", ["E","F","G","H","I","J"])
    clarity = st.selectbox("Clarity", ["IF","SI1","SI2","VS1","VS2","VVS1","VVS2"])
    table =  st.number_input("Table",min_value=10.00,max_value=100.00,step=0.01)
    depth = st.number_input("Depth",min_value=0.01,max_value=100.00,step=0.01)
    x = st.number_input("x-dimension",min_value=0.01,max_value=100.00,step=0.01)
    y = st.number_input("y-dimension",min_value=0.01,max_value=100.00,step=0.01)
    z = st.number_input("z-dimension",min_value=0.01,max_value=100.00,step=0.01)
    
    result =""
    
    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(carat,cut,color,clarity,depth,table,x,y,z)
    st.success('The Price is {}'.format(result))
    
if __name__=='__main__':
    main()