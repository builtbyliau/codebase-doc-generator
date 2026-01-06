# Codebase Documentation Generator

## Problem
Developers hate writing documentation. READMEs are outdated. New team members waste hours understanding codebases.

## Solution
AI-powered tool that analyzes a GitHub repo and auto-generates:
- README with project overview
- Architecture summary
- API documentation
- Setup instructions

## MVP Scope (Week 1)
**IN SCOPE:**
- ✅ Input: GitHub repo URL
- ✅ Clone repo locally
- ✅ Analyze file structure
- ✅ Generate README using Claude API
- ✅ Output: Markdown file

**OUT OF SCOPE (Future):**
- ❌ Architecture diagrams (too complex for MVP)
- ❌ Multi-language support (start with Python/JS only)
- ❌ GitHub integration (manual output is fine)
- ❌ Custom templates

## Tech Stack
- Python 3.11+
- LLM Agnostic Design (Gemini Flash for Dev, support for Claude/Groq)
- GitPython (for cloning repos)
- Click (CLI interface)
- uv (Dependency Management)

## Success Criteria
Can generate a useful README for any public Python/JavaScript repo in under 2 minutes.