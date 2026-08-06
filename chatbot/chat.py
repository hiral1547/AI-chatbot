"""
Chat Service
------------
Coordinates memory and LLM communication.
"""

from chatbot.llm import LLMService
from chatbot.memory import ChatMemory


class ChatService:

    def __init__(self):

        self.llm = LLMService()

    def ask(self, question):

        # Store user message
        ChatMemory.add_user_message(question)

        # Fetch complete conversation
        messages = ChatMemory.get_messages()

        # Generate AI response
        answer = self.llm.generate_response(messages)

        # Store AI response
        ChatMemory.add_ai_message(answer)

        return answer