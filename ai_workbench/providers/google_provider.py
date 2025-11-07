"""Google Gemini provider implementation."""

from typing import List, Dict
import google.generativeai as genai
from ai_workbench.providers import AIProvider


class GoogleProvider(AIProvider):
    """Google Gemini API provider."""
    
    def __init__(self, api_key: str, model: str = "gemini-2.0-flash-exp"):
        super().__init__(api_key, model)
        genai.configure(api_key=api_key)
        self.model_instance = genai.GenerativeModel(model)
    
    def _format_messages(self, messages: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Format messages for Gemini API."""
        formatted = []
        for msg in messages:
            role = msg["role"]
            # Map roles for Gemini
            if role == "system":
                # Prepend system message to first user message
                continue
            elif role == "assistant":
                role = "model"
            formatted.append({"role": role, "parts": [msg["content"]]})
        return formatted
    
    def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Generate a response using Google Gemini API."""
        # Extract system message if present
        system_message = None
        formatted_messages = []
        
        for msg in messages:
            if msg["role"] == "system":
                system_message = msg["content"]
            else:
                formatted_messages.append(msg)
        
        # Create chat with history
        chat = self.model_instance.start_chat(history=self._format_messages(formatted_messages[:-1]))
        
        # Send the last message
        message_content = formatted_messages[-1]["content"]
        if system_message:
            message_content = f"{system_message}\n\n{message_content}"
        
        response = chat.send_message(message_content)
        return response.text
    
    def generate_stream(self, messages: List[Dict[str, str]], **kwargs):
        """Generate a streaming response using Google Gemini API."""
        # Extract system message if present
        system_message = None
        formatted_messages = []
        
        for msg in messages:
            if msg["role"] == "system":
                system_message = msg["content"]
            else:
                formatted_messages.append(msg)
        
        # Create chat with history
        chat = self.model_instance.start_chat(history=self._format_messages(formatted_messages[:-1]))
        
        # Send the last message with streaming
        message_content = formatted_messages[-1]["content"]
        if system_message:
            message_content = f"{system_message}\n\n{message_content}"
        
        response = chat.send_message(message_content, stream=True)
        for chunk in response:
            if chunk.text:
                yield chunk.text
