"""
Memory Manager
--------------
Stores and retrieves conversation history
using Streamlit Session State.
"""

import streamlit as st

from chatbot.prompt import SYSTEM_PROMPT


class ChatMemory:

    @staticmethod
    def initialize():

        if "messages" not in st.session_state:

            st.session_state.messages = [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                }
            ]

    @staticmethod
    def get_messages():

        return st.session_state.messages

    @staticmethod
    def add_user_message(message):

        st.session_state.messages.append(
            {
                "role": "user",
                "content": message
            }
        )

    @staticmethod
    def add_ai_message(message):

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": message
            }
        )

    @staticmethod
    def clear():

        st.session_state.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]