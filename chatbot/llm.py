"""
LLM Service
-----------
Handles communication with OpenAI.
"""

from google import genai
from google.genai import types

from config.settings import GEMINI_API_KEY, MODEL_NAME

client = genai.Client(api_key=GEMINI_API_KEY)


class LLMService:

    def generate_response(self, messages):

        try:
            system_instruction = None
            conversation = []

            for msg in messages:
                if msg["role"] == "system":
                    system_instruction = msg["content"]
                else:
                    conversation.append(
                        f'{msg["role"].capitalize()}: {msg["content"]}'
                    )

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents="\n\n".join(conversation),
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction
                ) if system_instruction else None,
            )

            print(response)
            print("--------------------------------")
            print(response.candidates)

            return response.text if response.text else "No text returned."

        except Exception as e:
            return f"Error: {e}"