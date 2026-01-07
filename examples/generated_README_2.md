# Codebase Doc Generator

An AI-powered CLI tool that automatically generates comprehensive, professional `README.md` files for any GitHub repository. By analyzing the codebase structure and sample file content, it leverages the Gemini API to produce high-quality documentation in seconds.

## Description

`codebase-doc-generator` takes the manual effort out of documenting your projects. It clones a target repository, performs a structural analysis of its files, extracts representative code samples, and feeds this context into Google's Gemini 1.5 Flash model. The result is a structured Markdown file that includes project descriptions, installation steps, usage guides, and directory overviews.

## Features

- **Automated Repository Cloning**: Securely clones repositories to temporary directories for analysis.
- **Intelligent Code Analysis**: Scans project structure while ignoring non-essential directories (e.g., `.git`, `node_modules`, `venv`).
- **AI-Powered Insights**: Uses the latest Gemini 1.5 Flash model to understand code intent and generate human-like documentation.
- **Customizable Output**: Specify your own output filename via CLI options.
- **Safe Cleanup**: Automatically removes temporary cloned files and data after the documentation is generated.
- **Extensible Architecture**: Modular design separating the analyzer, generator, and CLI logic.

## Installation

### Prerequisites

- Python 3.8+
- [Git](https://git-scm.com/) installed on your system.
- A Google Gemini API Key.

### Setup

1. **Clone this repository**:
   ```bash
   git clone https://github.com/builtbyliau/codebase-doc-generator
   cd codebase-doc-generator
   ```

2. **Install dependencies**:
   ```bash
   pip install click gitpython google-generativeai python-dotenv
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

The tool is controlled via a simple Command Line Interface (CLI).

### Generate a README

Run the `generate` command followed by the URL of the GitHub repository you wish to document:

```bash
python main.py generate https://github.com/username/repo-name
```

### Options

- `--output` or `-o`: Specify a custom name for the generated file (default is `generated_README.md`).

```bash
python main.py generate https://github.com/username/repo-name -o DOCUMENTATION.md
```

## Project Structure

```text
├── main.py              # Entry point for the CLI application
├── src/
│   ├── main.py          # Click CLI command definitions and orchestration
│   ├── analyzer.py      # Logic for cloning and scanning repository structure
│   ├── generator.py     # Gemini API integration and prompt engineering
│   └── __init__.py      # Package initialization
├── examples/
│   └── sample_output.md # Example of a generated README
└── .vscode/             # Editor-specific settings
```

## Contributing

Contributions are welcome! To contribute to this project, follow these steps:

1. **Fork** the repository.
2. **Create a new branch** (`git checkout -b feature/your-feature`).
3. **Commit your changes** (`git commit -m 'Add some feature'`).
4. **Push to the branch** (`git push origin feature/your-feature`).
5. **Open a Pull Request**.

Please ensure your code follows the existing style and includes comments where necessary.