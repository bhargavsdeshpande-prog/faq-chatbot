import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="FAQ Chatbot")

st.title("🤖 FAQ Chatbot")

st.write("Ask a question about our services.")

user_question = st.text_input("Your Question")

if st.button("Ask"):
    response = get_response(user_question)

    st.success(response)