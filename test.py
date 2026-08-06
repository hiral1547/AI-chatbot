import streamlit as st

from chatbot.chat import ChatService
from chatbot.memory import ChatMemory

st.title("Test Chat")

ChatMemory.initialize()

chat = ChatService()

question = st.text_input("Question")

if st.button("Ask") and question:
    answer = chat.ask(question)
    st.write(answer)