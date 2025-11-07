#!/usr/bin/env python3
"""Demo script to show AI Terminal Workbench features."""

import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()


def show_demo():
    """Display demo information."""
    
    demo_text = """
# 🎬 AI Terminal Workbench Demo

## What is this?

AI Terminal Workbench brings AI coding assistance directly to your terminal, just like the tools shown in the YouTube video!

## Key Features Demonstrated

### 1. Multiple AI Providers
Switch between OpenAI, Anthropic Claude, and Google Gemini on the fly:
```bash
ai-workbench --provider openai
ai-workbench --provider anthropic  
ai-workbench --provider google
```

### 2. Interactive Chat
Natural conversation with AI for:
- 💻 Code generation
- 🐛 Debugging help
- 📚 Learning programming concepts
- 🔧 Refactoring suggestions
- 📝 Documentation writing

### 3. Real-time Streaming
Get responses as they're generated for faster feedback!

### 4. Session Management
- Conversation history maintained throughout session
- Easy to clear and start fresh with `/clear`
- Context-aware responses

## Example Use Cases

### Code Generation
```
You: Create a Python function to calculate fibonacci numbers
```

### Debugging
```
You: I'm getting a TypeError when trying to concatenate int and str
```

### Learning
```
You: Explain the difference between list and tuple in Python
```

### Refactoring
```
You: How can I make this code more efficient? [paste code]
```

## Getting Started

1. Install the package (already done if you're seeing this!)
2. Set up API keys in `.env` file
3. Run `ai-workbench` or `awb`
4. Start coding with AI assistance!

## Need API Keys?

- **OpenAI**: https://platform.openai.com/api-keys
- **Anthropic**: https://console.anthropic.com/
- **Google**: https://ai.google.dev/

Copy `.env.example` to `.env` and add your keys!
    """
    
    console.print(Panel(Markdown(demo_text), border_style="cyan", title="Demo"))


if __name__ == "__main__":
    show_demo()
