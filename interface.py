import streamlit as st
import requests
st.title('5 : GraphQL')
st.title('GraphQL Interface by Fraz')

query = st.text_area('Enter GraphQL Query', 'query { hello }')
submit_button = st.button('Submit')

if submit_button:
    response = requests.post('http://localhost:8000', json={'query': query})
    result = response.json()
    st.write('Response:')
    st.json(result)
