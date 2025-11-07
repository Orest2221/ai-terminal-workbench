"""Main CLI interface for AI Terminal Workbench."""

import sys
import click
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory

from ai_workbench.config import config
from ai_workbench.conversation import Conversation
from ai_workbench.providers.openai_provider import OpenAIProvider
from ai_workbench.providers.anthropic_provider import AnthropicProvider
from ai_workbench.providers.google_provider import GoogleProvider


console = Console()


def get_provider(provider_name: str, model: str = None):
    """Get an AI provider instance."""
    api_key = config.get_api_key(provider_name)
    
    if not api_key:
        console.print(f"[red]Error: API key for {provider_name} not found.[/red]")
        console.print(f"[yellow]Please set the API key in your .env file or environment variables.[/yellow]")
        sys.exit(1)
    
    if model is None:
        model = config.get_default_model(provider_name)
    
    providers = {
        "openai": OpenAIProvider,
        "anthropic": AnthropicProvider,
        "google": GoogleProvider
    }
    
    provider_class = providers.get(provider_name)
    if not provider_class:
        console.print(f"[red]Error: Unknown provider '{provider_name}'[/red]")
        console.print("[yellow]Available providers: openai, anthropic, google[/yellow]")
        sys.exit(1)
    
    return provider_class(api_key, model)


def display_welcome():
    """Display welcome message."""
    welcome_text = """
# 🤖 AI Terminal Workbench

Welcome to your AI-powered coding assistant!

**Available commands:**
- `/help` - Show this help message
- `/clear` - Clear conversation history
- `/exit` or `/quit` - Exit the application
- `/provider <name>` - Switch AI provider (openai, anthropic, google)
- `/model <name>` - Switch model
- Any other input - Chat with the AI assistant

Type your question or command to get started!
    """
    console.print(Panel(Markdown(welcome_text), border_style="blue"))


@click.command()
@click.option("--provider", "-p", default=None, help="AI provider (openai, anthropic, google)")
@click.option("--model", "-m", default=None, help="Model to use")
@click.option("--no-stream", is_flag=True, help="Disable streaming responses")
def main(provider, model, no_stream):
    """AI Terminal Workbench - Your AI coding assistant in the terminal."""
    
    # Use default provider if not specified
    if provider is None:
        provider = config.default_provider
    
    # Check if provider is configured
    if not config.is_configured(provider):
        console.print(f"[red]Error: {provider} is not configured.[/red]")
        console.print("[yellow]Please set up your API keys in .env file.[/yellow]")
        console.print(f"[yellow]Copy .env.example to .env and add your API keys.[/yellow]")
        sys.exit(1)
    
    # Initialize provider
    current_provider = get_provider(provider, model)
    conversation = Conversation()
    
    # Display welcome message
    display_welcome()
    console.print(f"[green]Using provider: {provider}[/green]")
    console.print(f"[green]Using model: {current_provider.model}[/green]")
    console.print()
    
    # Create prompt session with history
    session = PromptSession(history=InMemoryHistory())
    
    # Main loop
    while True:
        try:
            # Get user input
            user_input = session.prompt("You: ", multiline=False)
            
            if not user_input.strip():
                continue
            
            # Handle commands
            if user_input.startswith("/"):
                command = user_input.split()[0].lower()
                
                if command in ["/exit", "/quit"]:
                    console.print("[yellow]Goodbye! 👋[/yellow]")
                    break
                
                elif command == "/help":
                    display_welcome()
                    continue
                
                elif command == "/clear":
                    conversation.clear()
                    console.print("[green]Conversation history cleared.[/green]")
                    continue
                
                elif command == "/provider":
                    parts = user_input.split()
                    if len(parts) < 2:
                        console.print("[red]Usage: /provider <name>[/red]")
                        continue
                    new_provider = parts[1].lower()
                    if not config.is_configured(new_provider):
                        console.print(f"[red]Provider '{new_provider}' is not configured.[/red]")
                        continue
                    current_provider = get_provider(new_provider, model)
                    provider = new_provider
                    console.print(f"[green]Switched to provider: {provider}[/green]")
                    console.print(f"[green]Using model: {current_provider.model}[/green]")
                    continue
                
                elif command == "/model":
                    parts = user_input.split()
                    if len(parts) < 2:
                        console.print("[red]Usage: /model <name>[/red]")
                        continue
                    new_model = parts[1]
                    current_provider = get_provider(provider, new_model)
                    console.print(f"[green]Switched to model: {new_model}[/green]")
                    continue
                
                else:
                    console.print(f"[red]Unknown command: {command}[/red]")
                    console.print("[yellow]Type /help for available commands.[/yellow]")
                    continue
            
            # Add user message to conversation
            conversation.add_user_message(user_input)
            
            # Generate response
            console.print("\n[bold cyan]Assistant:[/bold cyan] ", end="")
            
            try:
                if no_stream:
                    # Non-streaming response
                    response = current_provider.generate_response(conversation.get_messages())
                    console.print(Markdown(response))
                    conversation.add_assistant_message(response)
                else:
                    # Streaming response
                    response_text = ""
                    for chunk in current_provider.generate_stream(conversation.get_messages()):
                        console.print(chunk, end="")
                        response_text += chunk
                    console.print()  # New line after streaming
                    conversation.add_assistant_message(response_text)
            
            except Exception as e:
                console.print(f"[red]Error: {str(e)}[/red]")
                # Remove the user message that caused the error
                conversation.messages.pop()
            
            console.print()
        
        except KeyboardInterrupt:
            console.print("\n[yellow]Use /exit or /quit to exit.[/yellow]")
            continue
        except EOFError:
            console.print("\n[yellow]Goodbye! 👋[/yellow]")
            break


if __name__ == "__main__":
    main()
