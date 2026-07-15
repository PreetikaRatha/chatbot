from google import genai
import streamlit as st

client = genai.Client(api_key=st.secrets["API_KEY"])

st.title("🤖 Gemini Chatbot")

prompt = st.chat_input("Type your message...")

if prompt:
    st.chat_message("user").write(prompt)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    st.chat_message("assistant").write(response.text)
