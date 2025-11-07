"""Configuration management for AI Terminal Workbench."""

import os
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv


class Config:
    """Configuration manager for the application."""
    
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # API Keys
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        
        # Default settings
        self.default_provider = os.getenv("DEFAULT_PROVIDER", "openai")
        self.default_model = os.getenv("DEFAULT_MODEL", "gpt-4")
        
        # Provider-specific default models
        self.provider_models = {
            "openai": "gpt-4",
            "anthropic": "claude-3-5-sonnet-20241022",
            "google": "gemini-2.0-flash-exp"
        }
    
    def get_api_key(self, provider: str) -> Optional[str]:
        """Get API key for a specific provider."""
        keys = {
            "openai": self.openai_api_key,
            "anthropic": self.anthropic_api_key,
            "google": self.google_api_key
        }
        return keys.get(provider)
    
    def get_default_model(self, provider: str) -> str:
        """Get default model for a provider."""
        return self.provider_models.get(provider, self.default_model)
    
    def is_configured(self, provider: str) -> bool:
        """Check if a provider is configured with an API key."""
        return self.get_api_key(provider) is not None


# Global config instance
config = Config()
