"""Base provider interface for AI providers."""

from abc import ABC, abstractmethod
from typing import List, Dict, Any


class AIProvider(ABC):
    """Abstract base class for AI providers."""
    
    def __init__(self, api_key: str, model: str = None):
        self.api_key = api_key
        self.model = model
    
    @abstractmethod
    def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Generate a response from the AI model.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            **kwargs: Additional provider-specific parameters
            
        Returns:
            The generated response text
        """
        pass
    
    @abstractmethod
    def generate_stream(self, messages: List[Dict[str, str]], **kwargs):
        """Generate a streaming response from the AI model.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            **kwargs: Additional provider-specific parameters
            
        Yields:
            Response chunks as they arrive
        """
        pass
