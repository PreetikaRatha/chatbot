import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["API_KEY"])

st.title("Available Models")

try:
    for m in client.models.list():
        st.write(m.name)
except Exception as e:
    st.error(e)
