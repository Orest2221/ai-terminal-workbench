from setuptools import setup, find_packages

setup(
    name="ai-terminal-workbench",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "openai>=1.0.0",
        "anthropic>=0.18.0",
        "google-generativeai>=0.3.0",
        "click>=8.1.0",
        "rich>=13.0.0",
        "python-dotenv>=1.0.0",
        "colorama>=0.4.6",
        "prompt_toolkit>=3.0.0",
    ],
    entry_points={
        "console_scripts": [
            "ai-workbench=ai_workbench.cli:main",
            "awb=ai_workbench.cli:main",
        ],
    },
    author="AI Terminal Workbench",
    description="An AI-powered terminal assistant for coding tasks",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
)
