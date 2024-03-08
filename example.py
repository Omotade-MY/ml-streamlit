import streamlit as st
st.write("This is a Streamlit APP!!!")
st.header("This is a header")

# load the  ML model

# Predict 

# display result
name = st.text_input("Enter your name")
height = st.number_input("Enter your height")
if name:
    st.write(f"Welcome {name}, What do you want?")

if height:
    st.write(f"Your height is {height}")
