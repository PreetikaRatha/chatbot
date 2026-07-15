import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["API_KEY"])

st.write("Available models:")

try:
    for model in client.models.list():
        st.write(model.name)
except Exception as e:
    st.error(e)
