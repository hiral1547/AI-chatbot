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

from ui.components import (
    render_chat_history,
    show_user_message,
    stream_response,
)

# --------------------------------------------------------
# Page Configuration
# --------------------------------------------------------

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=PAGE_ICON,
    layout=PAGE_LAYOUT,
)

# --------------------------------------------------------
# Initialize Memory
# --------------------------------------------------------

ChatMemory.initialize()

chatbot = ChatService()

# --------------------------------------------------------
# Sidebar
# --------------------------------------------------------

render_sidebar()

# --------------------------------------------------------
# Header
# --------------------------------------------------------

st.title(APP_TITLE)

st.info(WELCOME_MESSAGE)

# --------------------------------------------------------
# Display Previous Messages
# --------------------------------------------------------

render_chat_history(
    ChatMemory.get_messages()
)

# --------------------------------------------------------
# Chat Input
# --------------------------------------------------------

question = st.chat_input("Type your message here...")

if question:

    # Display user message
    show_user_message(question)

    # Get AI response
    answer = chatbot.ask(question)

    # Display AI response with typing animation
    with st.chat_message("assistant"):
        stream_response(answer)