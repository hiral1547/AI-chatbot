"""
Reusable UI Components
----------------------
Contains reusable Streamlit UI components.
"""

import time
import streamlit as st


def show_user_message(message: str):
    """
    Display user message.
    """
    with st.chat_message("user"):
        st.markdown(message)


def show_ai_message(message: str):
    """
    Display AI message.
    """
    with st.chat_message("assistant"):
        st.markdown(message)


def render_chat_history(messages):
    """
    Render previous conversation.
    Skip system prompt.
    """

    for message in messages:

        if message["role"] == "system":
            continue

        if message["role"] == "user":
            show_user_message(message["content"])

        elif message["role"] == "assistant":
            show_ai_message(message["content"])


def stream_response(response: str, delay: float = 0.01):
    """
    ChatGPT-like typing animation.
    Displays the response character by character.
    """

    placeholder = st.empty()

    full_response = ""

    for char in response:

        full_response += char

        placeholder.markdown(full_response + "▌")

        time.sleep(delay)

    placeholder.markdown(full_response)