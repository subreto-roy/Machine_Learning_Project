import streamlit as st
import requests

st.title('Web Data Extractor')

# User inputs
url = st.text_input('URL', 'Enter the URL of the webpage to extract data from')
schema = st.text_area('Schema', 'Enter the schema in JSON format')

if st.button('Extract Data'):
    # Make an API request to the Django server
    response = requests.post('http://localhost:8000/api/extract/', json={'url': url, 'schema': schema})
    if response.status_code == 200:
        st.write('Data extracted successfully!')
        st.json(response.json())
    else:
        st.write('Failed to extract data. Error:', response.text)
