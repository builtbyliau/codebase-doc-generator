"""Analyze repository structure and extract file information."""

import os
import shutil
import tempfile
from pathlib import Path
from typing import Dict

import git


def clone_repo(repo_url: str) -> Path:
    """
    Clone a GitHub repository to a temporary directory.
    Returns Path object to the temp dir.
    """
    # Use mkdtemp to create a unique, safe temporary directory
    temp_dir = tempfile.mkdtemp(prefix="repo_doc_gen_")

    print(f"⏳ Cloning repository: {repo_url}...")
    try:
        git.Repo.clone_from(repo_url, temp_dir)
        return Path(temp_dir)
    except Exception as e:
        # If clone fails, clean up the empty dir immediately
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        raise e


def analyze_structure(repo_path: Path) -> Dict:
    """Analyze repository structure and file types."""

    # File extensions we care about
    SUPPORTED_EXTENSIONS = {".py", ".js", ".jsx", ".ts", ".tsx", ".json", ".md"}

    structure = {
        "total_files": 0,
        "file_types": {},
        "directory_tree": [],
    }

    # walk through directory
    for root, dirs, files in os.walk(repo_path):
        # skip common directories
        dirs[:] = [
            d
            for d in dirs
            if d
            not in {
                ".git",
                "node_modules",
                "__pycache__",
                ".venv",
                "venv",
                "dist",
                "build",
            }
        ]

        for file in files:
            file_path = Path(root) / file
            ext = file_path.suffix

            if ext in SUPPORTED_EXTENSIONS:
                structure["total_files"] += 1
                structure["file_types"][ext] = structure["file_types"].get(ext, 0) + 1

                # store relative path for tree view
                try:
                    rel_path = file_path.relative_to(repo_path)
                    structure["directory_tree"].append(str(rel_path))
                except ValueError:
                    continue

    return structure


def get_sample_files(repo_path: Path, max_files: int = 3) -> Dict[str, str]:
    """Extract content from a few sample files."""
    samples = {}
    count = 0

    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in {".git", "node_modules", "__pycache__"}]

        for file in files:
            if count >= max_files:
                break

            file_path = Path(root) / file
            ext = file_path.suffix

            # only read Python/JS files
            if ext in {".py", ".js", ".jsx", ".ts", ".tsx"}:
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        # limit to 2000 chars to save tokens
                        content = f.read(2000)
                        rel_path = file_path.relative_to(repo_path)
                        samples[str(rel_path)] = content
                        count += 1
                except Exception as e:
                    print(f"⚠️ Could not read {file_path}: {e}")
                    continue

    return samples
