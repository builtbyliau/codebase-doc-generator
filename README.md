# Codebase Documentation Generator

Generate comprehensive README files for any GitHub repo in seconds using AI.

## Why Use This?

- 🚀 **Fast**: Analyzes repos in under 60 seconds
- 🎯 **Accurate**: Uses actual code analysis, not generic templates  
- 🔒 **Privacy-First**: Runs locally, no data sent to third parties
- 💰 **Cost-Effective**: Uses Gemini (free tier: 15 requests/min)

## Quick Start

```bash
# Install
git clone https://github.com/builtbyliau/codebase-doc-generator
cd codebase-doc-generator
uv sync

# Generate docs
uv run main.py generate https://github.com/user/repo
```

## Example Output

See [examples/sample_output.md](examples/sample_output.md) for a real example generated from the Spoon-Knife repository.

## Roadmap

- [ ] Support for more languages (Go, Rust, Java)
- [ ] Architecture diagram generation
- [ ] Integration with GitHub Actions
- [ ] Custom templates

## Built With

- Python 3.11+
- Gemini 3 Flash Preview
- GitPython
- Click

---

Built by [@builtbyliau](https://github.com/builtbyliau) | [Report Issues](https://github.com/builtbyliau/codebase-doc-generator/issues)