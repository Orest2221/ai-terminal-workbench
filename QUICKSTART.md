# 🚀 Quick Start Guide

Get started with AI Terminal Workbench in 5 minutes!

## Step 1: Install

```bash
# Clone the repository
git clone https://github.com/Orest2221/ai-terminal-workbench.git
cd ai-terminal-workbench

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install
pip install -e .
```

## Step 2: Configure API Keys

```bash
# Copy the example env file
cp .env.example .env

# Edit .env and add at least one API key
nano .env  # or use your favorite editor
```

Add your API key(s):
```env
OPENAI_API_KEY=sk-...
# or
ANTHROPIC_API_KEY=sk-ant-...
# or
GOOGLE_API_KEY=AIza...
```

## Step 3: Run!

```bash
ai-workbench
# or use the short alias
awb
```

## Step 4: Start Chatting

Try these example prompts:

```
You: Write a Python function to reverse a string

You: Explain how list comprehension works in Python

You: Debug this error: TypeError: 'str' object does not support item assignment

You: Create a REST API endpoint using Flask
```

## Command Reference

- `/help` - Show available commands
- `/clear` - Start a new conversation
- `/provider openai` - Switch to OpenAI
- `/provider anthropic` - Switch to Claude
- `/provider google` - Switch to Gemini
- `/model gpt-4` - Change model
- `/exit` - Quit the application

## Tips

1. **Be specific**: The more context you provide, the better the responses
2. **Use streaming**: Streaming is enabled by default for faster feedback
3. **Try different providers**: Each AI has different strengths
4. **Maintain context**: The conversation history helps AI understand your project

## Troubleshooting

**"API key not found"**
- Make sure your `.env` file exists and has valid API keys
- Check that you're in the project directory

**"Provider not configured"**
- You need at least one API key configured
- Use `--provider` flag to specify which one to use

**"Command not found: ai-workbench"**
- Make sure you installed with `pip install -e .`
- Activate your virtual environment first

## Need Help?

- Check the [README](README.md) for detailed documentation
- View [Examples](examples/EXAMPLES.md) for usage patterns
- Open an issue on GitHub for bugs or questions

Happy coding with AI! 🎉
