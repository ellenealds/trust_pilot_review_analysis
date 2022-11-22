# this is a streamlit app that takes in a csv file and displays the data in a table, 
# a large language model function is called on each row and generates a new column with the output of the function

import streamlit as st
import pandas as pd

# create a class that stores the data and the output of the function
class Data:
    def __init__(self, data):
        self.data = data
        self.output = None
        # the class can create add columns based on a function
        # the function is called on each row of the data
        # the output is stored in the output attribute
    def add_column(self, function):
        self.output = self.data.apply(function, axis=1)
        return self.output

# upload the csv file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    # read the csv file into a pandas dataframe
    df = pd.read_csv(uploaded_file)
    # create an instance of the Data class
    data = Data(df)
    # add a column to the dataframe
    data.add_column(function)

    # display the dataframe into a table with filter and sort options
    st.write(data.output)

# import csv file
df = pd.read_csv('fedex_reviews.csv')

# if no file is uploaded, add a button to use sample data
if uploaded_file is None:
    if st.button('Use sample data'):
        uploaded_file = df

# create an instance of the Data class
data = Data(df)

#display the dataframe into a table with filter and sort options
st.write(data.output)

