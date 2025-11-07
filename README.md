# 🤖 AI Terminal Workbench

An AI-powered terminal assistant for developers, similar to the tools shown in [this YouTube video](https://www.youtube.com/watch?v=MsQACpcuTkU&t=15s). Chat with AI directly from your terminal for coding help, explanations, debugging, and more!

## ✨ Features

- 🚀 **Multiple AI Providers**: Support for OpenAI (GPT-4), Anthropic (Claude), and Google (Gemini)
- 💬 **Interactive Chat**: Natural conversation with AI in your terminal
- 🎨 **Beautiful Output**: Rich markdown rendering and colorful interface
- 📝 **Conversation History**: Maintains context throughout your session
- ⚡ **Streaming Responses**: Real-time streaming for faster feedback
- 🔄 **Easy Provider Switching**: Switch between AI providers on-the-fly
- 🎯 **Command System**: Built-in commands for common tasks

## 🎥 Inspiration

This tool is inspired by the AI terminal assistants demonstrated in the video "You've Been Using AI the Hard Way (Use This Instead)" which showcases how developers can use AI directly in the terminal for 10x productivity.

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/Orest2221/ai-terminal-workbench.git
cd ai-terminal-workbench
```

2. **Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install the package**
```bash
pip install -e .
```

4. **Set up your API keys**
```bash
cp .env.example .env
```

Edit the `.env` file and add your API keys:
```env
# Choose at least one provider
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
GOOGLE_API_KEY=your_google_api_key_here

# Set your preferred default provider
DEFAULT_PROVIDER=openai  # or anthropic, or google
```

### Getting API Keys

- **OpenAI**: Get your API key from [platform.openai.com](https://platform.openai.com/api-keys)
- **Anthropic**: Get your API key from [console.anthropic.com](https://console.anthropic.com/)
- **Google**: Get your API key from [ai.google.dev](https://ai.google.dev/)

## 🚀 Usage

### Basic Usage

Start the AI terminal workbench:
```bash
ai-workbench
# or use the short alias
awb
```

### Command Line Options

```bash
# Use a specific provider
ai-workbench --provider openai
ai-workbench --provider anthropic
ai-workbench --provider google

# Use a specific model
ai-workbench --model gpt-4
ai-workbench --model claude-3-5-sonnet-20241022
ai-workbench --model gemini-2.0-flash-exp

# Disable streaming (get complete response at once)
ai-workbench --no-stream
```

### Interactive Commands

Once inside the AI workbench, you can use these commands:

- `/help` - Show help message
- `/clear` - Clear conversation history
- `/exit` or `/quit` - Exit the application
- `/provider <name>` - Switch AI provider (openai, anthropic, google)
- `/model <name>` - Switch model

### Example Conversations

**Getting code help:**
```
You: How do I read a JSON file in Python?
Assistant: Here's how to read a JSON file in Python:

```python
import json

# Read JSON from file
with open('data.json', 'r') as file:
    data = json.load(file)
    
print(data)
```
```

**Debugging assistance:**
```
You: I'm getting a "list index out of range" error in my Python script
Assistant: This error occurs when you try to access an index that doesn't exist...
```

**Code explanation:**
```
You: Explain what this regex does: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
Assistant: This is an email validation regex pattern. Let me break it down...
```

## 🎯 Use Cases

- **Code Generation**: Ask AI to write functions, classes, or entire scripts
- **Debugging Help**: Get assistance understanding and fixing errors
- **Code Explanation**: Understand complex code snippets
- **Refactoring**: Get suggestions for improving code quality
- **Learning**: Ask questions about programming concepts
- **Quick Scripts**: Generate one-off scripts for automation tasks
- **Documentation**: Get help writing docstrings and comments

## 🛠️ Supported AI Providers

| Provider | Models | Strengths |
|----------|--------|-----------|
| **OpenAI** | gpt-4, gpt-4-turbo, gpt-3.5-turbo | Well-rounded, great for general coding tasks |
| **Anthropic** | claude-3-5-sonnet-20241022, claude-3-opus-20240229 | Excellent reasoning, great for complex problems |
| **Google** | gemini-2.0-flash-exp, gemini-pro | Fast responses, large context window |

## 🔧 Development

### Project Structure

```
ai-terminal-workbench/
├── ai_workbench/
│   ├── __init__.py
│   ├── cli.py              # Main CLI interface
│   ├── config.py           # Configuration management
│   ├── conversation.py     # Conversation history
│   └── providers/
│       ├── __init__.py     # Base provider interface
│       ├── openai_provider.py
│       ├── anthropic_provider.py
│       └── google_provider.py
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py
```

### Running Tests

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

## 📝 Tips & Tricks

1. **Use streaming for longer responses** - Streaming is enabled by default and provides faster feedback
2. **Clear history when changing topics** - Use `/clear` to start fresh conversations
3. **Try different providers** - Each AI has different strengths; experiment to find your favorite
4. **Provide context** - The more context you provide, the better the responses
5. **Use specific questions** - Specific questions get better answers than vague ones

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - feel free to use this project for any purpose.

## 🙏 Acknowledgments

- Inspired by the YouTube video "You've Been Using AI the Hard Way (Use This Instead)"
- Built with amazing libraries: Rich, Click, Prompt Toolkit, and more
- Powered by OpenAI, Anthropic, and Google AI APIs

## 📧 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Happy Coding! 🚀**