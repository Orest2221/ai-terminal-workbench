"""Conversation history management."""

from typing import List, Dict
import json
from pathlib import Path


class Conversation:
    """Manages conversation history."""
    
    def __init__(self):
        self.messages: List[Dict[str, str]] = []
        self.system_message = "You are an expert coding assistant helping developers with terminal-based tasks. Provide clear, concise, and accurate code solutions."
    
    def add_system_message(self, content: str):
        """Add or update the system message."""
        self.system_message = content
    
    def add_user_message(self, content: str):
        """Add a user message to the conversation."""
        self.messages.append({"role": "user", "content": content})
    
    def add_assistant_message(self, content: str):
        """Add an assistant message to the conversation."""
        self.messages.append({"role": "assistant", "content": content})
    
    def get_messages(self) -> List[Dict[str, str]]:
        """Get all messages including system message."""
        return [{"role": "system", "content": self.system_message}] + self.messages
    
    def clear(self):
        """Clear conversation history."""
        self.messages = []
    
    def save(self, filepath: Path):
        """Save conversation to a file."""
        data = {
            "system_message": self.system_message,
            "messages": self.messages
        }
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
    
    def load(self, filepath: Path):
        """Load conversation from a file."""
        with open(filepath, "r") as f:
            data = json.load(f)
        self.system_message = data.get("system_message", self.system_message)
        self.messages = data.get("messages", [])
