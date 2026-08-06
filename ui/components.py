"""
Reusable UI Components
"""

import streamlit as st


def show_user_message(message):

    with st.chat_message("user"):

        st.markdown(message)


def show_ai_message(message):

    with st.chat_message("assistant"):

        st.markdown(message)


def render_chat_history(messages):

    """
    Display chat history.

    Skip system prompt.
    """

    for msg in messages:

        if msg["role"] == "system":
            continue

        if msg["role"] == "user":

            show_user_message(msg["content"])

        elif msg["role"] == "assistant":

            show_ai_message(msg["content"])


def show_typing():

    return st.spinner("Thinking...")