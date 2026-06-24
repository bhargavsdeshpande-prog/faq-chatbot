import streamlit as st
import nltk
from nltk.tokenize import word_tokenize

st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖")

st.title("🤖 FAQ Chatbot")

st.write("Ask me anything from the FAQ list!")

# Sample FAQ (replace with your dataset)
faq = {
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is python": "Python is a programming language.",
}

def get_response(user_input):
    user_input = user_input.lower()
    return faq.get(user_input, "Sorry, I don't know the answer.")

user_query = st.text_input("Type your question:")

if user_query:
    response = get_response(user_query)
    st.success(response)
