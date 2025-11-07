"""Anthropic Claude provider implementation."""

from typing import List, Dict
from anthropic import Anthropic
from ai_workbench.providers import AIProvider


class AnthropicProvider(AIProvider):
    """Anthropic Claude API provider."""
    
    def __init__(self, api_key: str, model: str = "claude-3-5-sonnet-20241022"):
        super().__init__(api_key, model)
        self.client = Anthropic(api_key=api_key)
    
    def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Generate a response using Anthropic API."""
        # Extract system message if present
        system_message = None
        formatted_messages = []
        
        for msg in messages:
            if msg["role"] == "system":
                system_message = msg["content"]
            else:
                formatted_messages.append(msg)
        
        response = self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            system=system_message if system_message else "You are a helpful coding assistant.",
            messages=formatted_messages,
            **kwargs
        )
        return response.content[0].text
    
    def generate_stream(self, messages: List[Dict[str, str]], **kwargs):
        """Generate a streaming response using Anthropic API."""
        # Extract system message if present
        system_message = None
        formatted_messages = []
        
        for msg in messages:
            if msg["role"] == "system":
                system_message = msg["content"]
            else:
                formatted_messages.append(msg)
        
        with self.client.messages.stream(
            model=self.model,
            max_tokens=4096,
            system=system_message if system_message else "You are a helpful coding assistant.",
            messages=formatted_messages,
            **kwargs
        ) as stream:
            for text in stream.text_stream:
                yield text
