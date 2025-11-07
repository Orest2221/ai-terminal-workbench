"""OpenAI provider implementation."""

from typing import List, Dict
from openai import OpenAI
from ai_workbench.providers import AIProvider


class OpenAIProvider(AIProvider):
    """OpenAI API provider."""
    
    def __init__(self, api_key: str, model: str = "gpt-4"):
        super().__init__(api_key, model)
        self.client = OpenAI(api_key=api_key)
    
    def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Generate a response using OpenAI API."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            **kwargs
        )
        return response.choices[0].message.content
    
    def generate_stream(self, messages: List[Dict[str, str]], **kwargs):
        """Generate a streaming response using OpenAI API."""
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=True,
            **kwargs
        )
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content
