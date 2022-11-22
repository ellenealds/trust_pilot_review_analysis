# this is a streamlit app that takes in a csv file and displays the data in a table, 
# a large language model function is called on each row and generates a new column with the output of the function

import streamlit as st
import pandas as pd

# the user can either upload their own file in the format of a csv containing one column called data or they can use the sample data
# import csv file
df = pd.read_csv('fedex_reviews.csv')

# display the data in a table contained in a 
st.write(df)

# add an input box for the user to enter a string, display this as prompt and provide a description
input_string = st.text_input('Enter a string', 'Type Here')