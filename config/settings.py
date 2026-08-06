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

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_NAME = "gpt-4.1-mini"

TEMPERATURE = 0.5

MAX_TOKENS = 500

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