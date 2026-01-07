"""Generate documentation using Gemini API."""

import os
from typing import Dict

import google.generativeai as genai
from dotenv import load_dotenv

# load environment variables
load_dotenv()


def generate_readme(
    repo_structure: Dict, sample_files: Dict[str, str], repo_url: str
) -> str:
    """Generate README using Gemini API."""

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "❌ GEMINI_API_KEY not found in .env file. Please check your configuration."
        )

    # configure Gemini
    genai.configure(api_key=api_key)
    # hardcoded to flash model as per MVP specs (Jan 2026)
    model = genai.GenerativeModel("gemini-3-flash-preview")

    # build the prompt
    prompt = f"""You are a technical documentation expert. Analyze this codebase and generate a comprehensive README.md.

Repository URL: {repo_url}

Repository Structure:
- Total Files: {repo_structure["total_files"]}
- File Types: {repo_structure["file_types"]}
- Directory Structure (truncated):
{chr(10).join(f"  - {path}" for path in repo_structure["directory_tree"][:50])}

Sample Code Files:
{_format_sample_files(sample_files)}

Generate a README with these sections:
1. # Project Title (extract from repo URL or code)
2. ## Description (what does this project do?)
3. ## Features (bullet points)
4. ## Installation (how to set up)
5. ## Usage (how to run/use)
6. ## Project Structure (overview of directories)
7. ## Contributing (standard contribution guidelines)

Use clear, concise language. Include code examples where relevant.
Write in Markdown format.
"""

    print("🤖 Generating documentation with Gemini...")
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise Exception(f"Gemini API Error: {str(e)}")


def _format_sample_files(samples: Dict[str, str]) -> str:
    """Format sample files for the prompt."""
    formatted = []
    for path, content in samples.items():
        formatted.append(f"\nFile: {path}\n```\n{content}\n```")
    return "\n".join(formatted)
