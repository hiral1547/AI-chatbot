# AI-chatbot
AI-powered chatbot tailored for business-specific customer support and assistance.

# Phase 1: AI Chatbot Build Guide

## 1. Project Overview

Phase 1 objective was to build an AI chatbot with:

- Streamlit-based conversational UI
- Modular chatbot architecture
- LLM API integration
- Conversation memory handling
- Secure API key management

---

## 2. Tech Stack

- Python
- Streamlit
- LLM API
- Python modular architecture

---

## 3. Project Structure

```text
AI-chatbot/
│
├── app.py                  # Streamlit application entry point
├── list_model.py           # Model utility/testing
├── test.py                 # Testing file
├── requirements.txt        # Project dependencies
│
├── chatbot/
│   ├── chat.py             # Chatbot logic and API interaction
│   └── memory.py           # Conversation memory handling
│
├── config/
│   └── settings.py         # Configuration management
│
└── ui/
    ├── sidebar.py          # Sidebar UI components
    └── components.py       # Reusable Streamlit components
```

---

# 4. Environment Setup

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

# 5. Install Dependencies

Install all required libraries:

```bash
pip install -r requirements.txt
```

---

# 6. API Key Setup

## Why API Key is Required

The chatbot connects with an external AI model API.

The API key is required for:

- Authentication
- Accessing AI models
- Tracking API usage

## Never Hardcode API Keys

❌ Avoid:

```python
api_key = "my_secret_key"
```

Problems:

- Exposes secrets
- Risk of pushing keys to GitHub
- Difficult to manage across environments


✅ Recommended:

Use:

- Environment variables
- Streamlit Secrets

---

# 7. Streamlit Secrets Setup

## Why Streamlit Secrets are Required?

When running the chatbot locally, environment variables from a `.env` file can be used. However, **Streamlit Community Cloud does not reliably use `.env` files during deployment**.

The reason is:

- `os.getenv()` reads values from system environment variables.
- Streamlit Cloud manages secrets separately through `st.secrets`.
- Secrets stored in Streamlit Cloud are not automatically loaded from a local `.env` file.

Therefore, local development and cloud deployment use different secret management approaches.

---

## Local Machine Setup (.env)

For local development, create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_key_here
```

Example:

```text
AI-chatbot/
│
├── .env
├── app.py
└── requirements.txt
```

Load the key using environment variables:

```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
```

---

## Streamlit Cloud Setup (st.secrets)

For Streamlit Community Cloud deployment, use **Streamlit Secrets** instead of `.env`.

Secrets are stored securely in the Streamlit Cloud dashboard.

Add:

```toml
GEMINI_API_KEY = "your_key_here"
```

Access the key in the application:

```python
import streamlit as st

api_key = st.secrets["GEMINI_API_KEY"]
```

---

# Adding Secrets in Streamlit Community Cloud

Follow these steps:

1. Open **Streamlit Community Cloud**:
   - Sign in using the GitHub account connected to your deployment.

2. Open your deployed chatbot application.

3. Locate the application settings:
   - Click the **⋮ (three dots)** menu near the top-right of the app page  
   - Or open the menu next to the app name inside your workspace

4. Select:

```text
Settings
```

5. Navigate to:

```text
App settings → Secrets
```

6. Add your secret:

```toml
GEMINI_API_KEY = "your_key_here"
```

7. Save the changes and restart/redeploy the application.

---

# Environment Difference Summary

| Environment | Secret Storage | Access Method |
|-------------|---------------|---------------|
| Local Machine | `.env` file | `os.getenv()` |
| Streamlit Cloud | Streamlit Secrets | `st.secrets` |

---

## Best Practice

Never commit sensitive keys into GitHub.

Do not add:

```text
.env
secrets.toml
API keys
```

to your repository.

Add them to `.gitignore`:

```text
.env
.streamlit/secrets.toml
```

This keeps API credentials secure while allowing the application to run safely in both local and cloud environments.

# 8. Streamlit Application Flow

```text
User
 |
 |
Streamlit UI
 |
 |
User Input
 |
 |
Chatbot Logic
 |
 |
LLM API Request
 |
 |
AI Generated Response
 |
 |
Display Response in Streamlit
```

---

# 9. Streamlit Implementation

Main application file:

```text
app.py
```

Responsibilities:

- Configure Streamlit page
- Initialize chatbot
- Load configuration
- Maintain session state
- Display chat messages
- Accept user input
- Show AI responses


Basic flow:

```python
user_input = st.chat_input()

response = chatbot.ask(user_input)

st.write(response)
```

---

# 10. Chat Memory

Conversation memory helps maintain context between messages.

Purpose:

- Store previous conversations
- Provide better AI responses
- Display chat history


Flow:

```text
User Message
      |
      |
Memory Storage
      |
      |
LLM Context
      |
      |
AI Response
```

---

# 11. Running the Application

Start Streamlit application:

```bash
streamlit run app.py
```

Application runs at:

```text
http://localhost:8501
```

---

# 12. Phase 1 Outcome

Completed:

✅ Streamlit chatbot interface  
✅ Modular project structure  
✅ LLM API integration  
✅ Conversation memory  
✅ Secure API key management  
✅ Local and cloud deployment readiness  


## Future Enhancements

- Retrieval Augmented Generation (RAG)
- Document-based chatbot
- Database integration
- User authentication
- Advanced memory management
- Production deployment
