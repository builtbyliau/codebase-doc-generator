"""CLI interface for codebase documentation generator."""

import shutil
from pathlib import Path

import click

from .analyzer import analyze_structure, clone_repo, get_sample_files
from .generator import generate_readme


# helper function for safe filenames
def get_unique_filename(filename: str) -> str:
    path = Path(filename)
    if not path.exists():
        return filename

    counter = 1
    while True:
        # create new filename: generated_README_1.md, generated_README_2.md
        new_path = path.with_name(f"{path.stem}_{counter}{path.suffix}")
        if not new_path.exists():
            return str(new_path)
        counter += 1


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
        safe_output_path = get_unique_filename(output)

        with open(safe_output_path, "w", encoding="utf-8") as f:
            f.write(readme_content)

        click.echo(f"✨ Success! README generated at: {safe_output_path}")

    except Exception as e:
        click.echo(f"❌ Error: {str(e)}", err=True)

    finally:
        # cleanup
        if repo_path and repo_path.exists():
            click.echo("🧹 Cleaning up...")
            shutil.rmtree(repo_path)


@cli.command()
@click.argument("repo_url")
def compare(repo_url: str):
    """Compare existing README vs AI-generated README."""

    repo_path = None
    try:
        # 1. clone
        repo_path = clone_repo(repo_url)

        # 2. find existing README (case insensitive search)
        existing_content = ""
        existing_file_name = "N/A"

        for file in repo_path.iterdir():
            if file.name.lower().startswith("readme"):
                existing_file_name = file.name
                try:
                    with open(file, "r", encoding="utf-8", errors="replace") as f:
                        existing_content = f.read()
                except Exception:
                    existing_content = "(Could not read file encoding)"
                break

        if existing_content:
            click.echo(f"📄 Found existing: {existing_file_name}")
        else:
            click.echo("❌ No existing README found.")

        # 3. generate new
        click.echo("🔄 Generating AI version...")
        structure = analyze_structure(repo_path)
        samples = get_sample_files(repo_path)
        new_content = generate_readme(structure, samples, repo_url)

        # 4. display comparison (terminal summary)
        click.echo("\n" + "=" * 50)
        click.echo("📊 COMPARISON SUMMARY")
        click.echo("=" * 50)

        click.echo("\n--- [ORIGINAL START] ---")
        click.echo(existing_content[:300] + "..." if existing_content else "(None)")

        click.echo("\n--- [AI GENERATED START] ---")
        click.echo(new_content[:300] + "...")

        # 5. save files for deep dive
        click.echo("\n" + "=" * 50)
        click.echo("💾 SAVING FULL FILES FOR REVIEW")
        with open("compare_original.md", "w", encoding="utf-8") as f:
            f.write(existing_content if existing_content else "No original README.")
        with open("compare_ai.md", "w", encoding="utf-8") as f:
            f.write(new_content)

        click.echo("✅ Saved: 'compare_original.md' & 'compare_ai.md'")
        click.echo("💡 Tip: Use VS Code 'Select for Compare' to see the diff!")

    except Exception as e:
        click.echo(f"❌ Error: {str(e)}", err=True)
    finally:
        if repo_path and repo_path.exists():
            shutil.rmtree(repo_path)


if __name__ == "__main__":
    cli()
