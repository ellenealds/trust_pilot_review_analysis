# this is a streamlit app that takes in a csv file and displays the data in a table, 
# a large language model function is called on each row and generates a new column with the output of the function

import streamlit as st
import pandas as pd
import cohere

# create a function that saves the model
co = cohere.Client('b55ru767vjHE7IuQ0aaqQx9rIO3g7CN0zquVnEZY')

# the user can either upload their own file in the format of a csv containing one column called data or they can use the sample data
# import csv file
df = pd.read_csv('fedex_reviews.csv')

# display the data in a table contained in a 
st.write(df)

# provide an input box for the user to enter a string
user_input = st.text_input("Enter a string")
# provide an input for the new column name
new_column_name = st.text_input("Enter a new column name")

# create a new column in the dataframe with the name of the new column

def add_column(df, new_column_name):
    response = []
    for i in df['data']:
        prompt = f'Review: '+ {i} + user_input
        response1 = co.generate(
        model='xlarge',
        prompt=prompt,
        max_tokens=50,
        temperature=0.3,
        k=5,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE')
        response.append(response1.generations[0].text)
    df['new_column_name'] = response
