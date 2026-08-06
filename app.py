import streamlit as st

from config.settings import APP_TITLE

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🤖",
    layout="wide",
)

st.title(APP_TITLE)

st.success("Project Setup Completed Successfully ✅")