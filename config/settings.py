"""
Project Settings
----------------
Loads environment variables and project configuration.
"""

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# ==============================
# OpenAI Configuration
# ==============================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-3.6-flash"

# ==============================
# App Configuration
# ==============================

APP_TITLE = "🏢 Business AI Assistant"

WELCOME_MESSAGE = """
👋 Welcome!

I'm your Business AI Assistant.

I can answer general questions
and assist you throughout our conversation.

How can I help you today?
"""

PAGE_ICON = "🤖"

PAGE_LAYOUT = "wide"

# ==============================
# Sidebar
# ==============================

SIDEBAR_TITLE = "Business AI"

ABOUT_TEXT = """
### Business AI Assistant

Phase 1 Demo

Built with:

- Python
- Streamlit
- OpenAI

Version: 1.0
"""

DEFAULT_MODEL = MODEL_NAME