# this is a streamlit app that takes in a csv file and displays the data in a table, 
# a large language model function is called on each row and generates a new column with the output of the function

import streamlit as st
import pandas as pd

# the user can either upload their own file in the format of a csv containing one column called data or they can use the sample data
# import csv file
df = pd.read_csv('fedex_reviews.csv')
# upload the csv file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else :
    df = uploaded_file
    
    st.write(df)

