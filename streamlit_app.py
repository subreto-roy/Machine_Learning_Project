import streamlit as st
import requests
import json

st.title('Data Extractor')

url = st.text_input('Enter the URL:', '')
schema_str = st.text_area('Enter the schema in JSON format:', '')

if st.button('Extract Data'):
    try:
        schema = json.loads(schema_str)
        response = requests.post('http://localhost:8501/extract/', json={'url': url, 'schema': schema})
        if response.status_code == 200:
            st.success('Data extracted successfully!')
            st.json(response.json())
        else:
            st.error(f'Failed to extract data: {response.text}')
    except json.JSONDecodeError:
        st.error("The schema format is incorrect. Please enter valid JSON.")
