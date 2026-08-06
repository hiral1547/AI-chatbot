"""
Sidebar UI
"""

import streamlit as st

from chatbot.memory import ChatMemory
from config.settings import (
    SIDEBAR_TITLE,
    ABOUT_TEXT,
    DEFAULT_MODEL,
)


def render_sidebar():

    with st.sidebar:

        st.title(SIDEBAR_TITLE)

        st.divider()

        st.subheader("Model")

        st.info(DEFAULT_MODEL)

        st.divider()

        st.subheader("Temperature")

        st.write("0.5")

        st.divider()

        if st.button(
            "🗑 Clear Chat",
            use_container_width=True
        ):

            ChatMemory.clear()

            st.success("Chat Cleared")

            st.rerun()

        st.divider()

        with st.expander("About"):

            st.markdown(ABOUT_TEXT)