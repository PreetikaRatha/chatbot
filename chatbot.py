import streamlit as st
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.title("🤖 Gemini Chatbot")

prompt = st.chat_input("Type your message...")

if prompt:
    st.chat_message("user").write(prompt)

    response = st.session_state.chat.send_message(prompt)

    st.chat_message("assistant").write(response.text)
