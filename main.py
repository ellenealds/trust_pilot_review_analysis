# this is a streamlit app that takes in a csv file and displays the data in a table, 
# a large language model function is called on each row and generates a new column with the output of the function

import streamlit as st
import pandas as pd
import cohere

# create a function that saves the model
co = cohere.Client('x')

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
    # add a counter that will be used to display the progress of the function
    counter = 0
    # count the number of rows in the dataframe
    total_rows = len(df.index)
    for i in df['data']:
        
        temp = 'Review: ' + i
        prompt = temp + user_input
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
        counter += 1
        st.write(counter, 'of', total_rows, 'rows completed')
    df['new'] = response
    # rename the new column
    df.rename(columns={'new': new_column_name}, inplace=True)
    return df

# display the new dataframe
st.write(add_column(df, new_column_name))

# save the new dataframe as a csv file
df.to_csv('new.csv')
# import libraries to get the file
import base64
def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(
        csv.encode()
    ).decode()  # some strings <-> bytes conversions necessary here
    return f'<a href="data:file/csv;base64,{b64}" download="myfilename.csv">Download csv file</a>'
# download the new csv file
st.markdown(get_table_download_link(df), unsafe_allow_html=True)

