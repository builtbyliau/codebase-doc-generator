"""Generate documentation using Gemini API."""

import os
import time
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
    prompt = f"""You are a senior technical writer analyzing a codebase.

Repository: {repo_url}

Codebase Analysis:
- Total Files: {repo_structure["total_files"]}
- Languages: {repo_structure["file_types"]}
- Key Files Found: {", ".join(repo_structure["directory_tree"][:15])}

Sample Code:
{_format_sample_files(sample_files)}

Generate a README.md with these SPECIFIC requirements:

1. # Project Title
   - Extract from repo name or main file
   - Add a one-line tagline

2. ## Description  
   - 2-3 sentences explaining what this project does
   - Be specific based on actual code, not generic

3. ## Features
   - List 3-5 key features you can see in the code
   - Use bullet points

4. ## Installation
   - Provide actual commands based on language detected
   - If Python: include pip/uv commands
   - If JavaScript: include npm/yarn commands

5. ## Usage
   - Show a realistic example based on the code
   - Include code block with actual syntax

6. ## Project Structure
   - Show directory tree (top-level only)
   - Brief explanation of main folders

7. ## Contributing
   - Standard contribution guidelines

CRITICAL RULES:
- Only mention features you can verify in the code samples
- Don't hallucinate technologies not present
- Be specific, not generic
- Use proper Markdown formatting
- Keep it under 500 words

Output only the Markdown, no preamble.
"""

    print("🤖 Generating documentation with Gemini...")
    # add retry logic for API failures
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            if attempt == max_retries - 1:
                raise RuntimeError(
                    f"❌ Failed to generate README after {max_retries} attempts: {e}"
                )

            wait_time = 2 * (attempt + 1)  # exponential backoff: 2s, 4s...
            print(f"⚠️  Attempt {attempt + 1} failed. Retrying in {wait_time}s...")
            time.sleep(wait_time)


def _format_sample_files(samples: Dict[str, str]) -> str:
    """Format sample files for the prompt."""
    formatted = []
    for path, content in samples.items():
        formatted.append(f"\nFile: {path}\n```\n{content}\n```")
    return "\n".join(formatted)
