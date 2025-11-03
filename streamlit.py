#what is streamlit?
#it is a python library that turns data into sharable web apps easily

import streamlit as st
#Title of the application
st.title("""welcome to MET""")
#simple text
st.write("this is a simple application fo MET")
#take input box
name = st.text_input("enter your name")
#Buttons
if st.button("Greet"):
    st.success(f"Hello,{name}! Welcome to MET")

st.write("visualisations")
import pandas as pd
import numpy as np
data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['A','B','C']

)
st.line_chart(data)

option = st.selectbox("choose a number",[1,2,3])
st.write(f"you selected {option}")
choice = st.radio("pick one",['Apple','Banana','watermelon'])
st.write(f"your choice {choice}")

upload_file = st.file_uploader("upload your csv file")
if upload_file is not None:
    df = pd.read_csv("upload_file")
    st.dataframe(df)

st.sidebar.title("Menu")
select = st.sidebar.radio("Navigation",['Home','About'])
if select == "Home":
    st.write("Welcome Home")
else:
    st.write("About Us")


col1,col2 = st.columns(2)
col1.write("left column")
col2.write("right column")



