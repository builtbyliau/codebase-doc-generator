import os

import click
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


@click.command()
@click.argument("repo_url")
def main(repo_url):
    """
    Codebase Documentation Generator

    Analyzes a GitHub repository and generates a README.md file.
    """
    click.echo(f"➡️  Input Repository: {repo_url}")

    # simple check to see if env vars are loading
    gemini_key = os.getenv("GEMINI_API_KEY")
    if gemini_key:
        click.echo("✅ Gemini API Key detected.")
    else:
        click.echo("⚠️ Warning: GEMINI_API_KEY not found in .env")

    click.echo("🔄 Starting analysis... (Logic coming soon)")


if __name__ == "__main__":
    main()
