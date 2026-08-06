import streamlit as st

from config.settings import (
    APP_TITLE,
    PAGE_ICON,
    PAGE_LAYOUT,
    WELCOME_MESSAGE,
)

from chatbot.chat import ChatService
from chatbot.memory import ChatMemory
from ui.sidebar import render_sidebar
from ui.components import render_chat_history

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=PAGE_ICON,
    layout=PAGE_LAYOUT,
)

ChatMemory.initialize()

render_sidebar()

st.title(APP_TITLE)

st.info(WELCOME_MESSAGE)

chat = ChatService()

messages = ChatMemory.get_messages()

render_chat_history(messages)

if prompt := st.chat_input("Type your message here..."):
    chat.ask(prompt)
    st.rerun()