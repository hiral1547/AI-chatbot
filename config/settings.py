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
Hello 👋

I'm your AI Assistant.

Ask me anything!
"""

PAGE_ICON = "🤖"

PAGE_LAYOUT = "wide"