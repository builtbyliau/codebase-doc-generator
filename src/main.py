"""CLI interface for codebase documentation generator."""

import shutil

import click

from .analyzer import analyze_structure, clone_repo, get_sample_files
from .generator import generate_readme


@click.group()
def cli():
    """Codebase Documentation Generator - AI-powered README creation."""
    pass


@cli.command()
@click.argument("repo_url")
@click.option("--output", "-o", default="generated_README.md", help="Output file path")
def generate(repo_url: str, output: str):
    """
    Generate README for a GitHub repository.
    Example: python main.py generate https://github.com/user/repo
    """
    repo_path = None
    try:
        # step 1: clone repository
        repo_path = clone_repo(repo_url)
        click.echo("✅ Cloned to temporary location")

        # step 2: analyze structure
        click.echo("🔍 Analyzing codebase...")
        structure = analyze_structure(repo_path)
        click.echo(f"   Found {structure['total_files']} supported files")

        # step 3: extract samples
        click.echo("📄 Reading sample files...")
        samples = get_sample_files(repo_path, max_files=5)

        # step 4: generate documentation
        readme_content = generate_readme(structure, samples, repo_url)

        # step 5: save output
        with open(output, "w", encoding="utf-8") as f:
            f.write(readme_content)

        click.echo(f"✨ Success! README generated at: {output}")

    except Exception as e:
        click.echo(f"❌ Error: {str(e)}", err=True)

    finally:
        # cleanup
        if repo_path and repo_path.exists():
            click.echo("🧹 Cleaning up...")
            shutil.rmtree(repo_path)


if __name__ == "__main__":
    cli()
