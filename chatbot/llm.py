"""
LLM Service
-----------
Handles communication with OpenAI.
"""

from openai import OpenAI

from config.settings import (
    OPENAI_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
    MAX_TOKENS,
)

# Create OpenAI Client
client = OpenAI(api_key=OPENAI_API_KEY)


class LLMService:
    """
    Handles all interactions with the language model.
    """

    def generate_response(self, messages):
        """
        Send chat messages to the model
        and return the AI response.
        """

        try:

            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS,
            )

            return response.choices[0].message.content

        except Exception as e:

            return f"Error : {str(e)}"