# AutoDocGen

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> **AI-Powered Documentation Generator**  
> An intelligent documentation generation tool that leverages Large Language Models to automatically create comprehensive docstrings for Python code.

## Overview

AutoDocGen is an automated documentation generator that uses AI to analyze your Python codebase and generate high-quality docstrings. Built with AST-based code analysis and LLM integration, it intelligently identifies functions missing documentation and generates contextually appropriate docstrings following industry standards.

### Key Features

- **Automatic Python docstring generation** using Large Language Models
- **AST-based code analysis** for deep context understanding
- **Command-line interface** for batch processing
- **Multiple docstring formats** (Google-style, with NumPy support planned)
- **Flexible LLM backends** (OpenAI, Ollama with auto-detection)
- **Smart insertion** - only generates docs for functions missing docstrings
- **Multi-language support** (JavaScript and C# planned)

## Architecture

```
src/
├── core/           # Core data models and analysis
├── parsers/        # Language-specific code parsers
├── llm_clients/    # LLM provider integrations
├── utils/          # Utility functions for doc insertion
└── config/         # Configuration management
```

### Components

- **`PythonParser`**: AST-based Python code analysis
- **`LLMClientFactory`**: Auto-detection and creation of LLM clients
- **`OpenAIClient`** & **`OllamaClient`**: Provider-specific implementations
- **`CodeElement`**: Data model for code functions and classes
- **`FileAnalysis`**: Container for parsed file analysis results

## Installation

### Prerequisites

- Python 3.10 or higher
- OpenAI API key (for OpenAI client) or local Ollama installation

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/bdog18/auto-doc-generator.git
   cd auto-doc-generator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   ```bash
   # For OpenAI integration
   export OPENAI_API_KEY="your-api-key-here"
   ```

## Usage

### Basic Usage

Run the documentation generator on your Python source files:

```bash
python src/main.py
```

By default, it will:
- Scan all Python files in the `./src` directory
- Skip test files (files starting with `test_`)
- Generate docstrings for functions missing documentation
- Insert properly formatted docstrings directly into your files

### Configuration

Modify settings in `src/config/settings.py`:

```python
class Settings:
    openai_api_key = "your-key"        # OpenAI API key
    output_dir = Path("docs")          # Output directory
    supported_extensions = [".py"]     # File extensions to process
    max_tokens = 2000                  # Maximum tokens for LLM response
    temperature = 0.3                  # LLM creativity level
```

### LLM Provider Options

The tool automatically detects available LLM providers:

1. **Ollama** (local) - Tried first if available
2. **OpenAI** (API) - Fallback option

You can also specify a provider explicitly:

```python
llm_client = LLMClientFactory().create_client("openai")  # Force OpenAI
llm_client = LLMClientFactory().create_client("ollama")  # Force Ollama
```

## Example Output

**Before:**
```python
def calculate_fibonacci(n):
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
```

**After:**
```python
def calculate_fibonacci(n):
    """
    Calculates the nth Fibonacci number using recursive approach.

    Args:
        n (int): The position in the Fibonacci sequence to calculate.

    Returns:
        int: The Fibonacci number at position n.

    Example:
        >>> calculate_fibonacci(5)
        5
    """
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
```

## Testing

Run the test suite:

```bash
pytest tests/
```

Test files include:
- `test_python_parser.py` - Parser functionality tests
- `test_llm_client_factory.py` - Client factory tests  
- `test_doc_insertion.py` - Documentation insertion tests

## Project Structure

```
auto-doc-generator/
├── LICENSE                       # MIT License
├── README.md                     # This file
├── pyproject.toml                # Project configuration
├── requirements.txt              # Python dependencies
├── src/                          # Source code
│   ├── main.py                   # Entry point
│   ├── config/                   # Configuration
│   │   └── settings.py           # App settings
│   ├── core/                     # Core models
│   │   └── analyzer.py           # Code analysis data models
│   ├── llm_clients/              # LLM integrations
│   │   ├── base_llm_client.py
│   │   ├── api_llm_client.py
│   │   ├── local_llm_client.py
│   │   └── llm_client_factory.py
│   ├── parsers/                  # Code parsers
│   │   ├── python_parser.py
│   │   ├── javascript_parser.py  # Planned
│   │   └── parser_factory.py
│   └── utils/                    # Utilities
│       └── doc_insertion.py
└── tests/                        # Test suite
    ├── test_python_parser.py
    ├── test_llm_client_factory.py
    └── test_doc_insertion.py
```

## Roadmap

### Current Status: Python Support
- [x] Python AST parsing
- [x] OpenAI integration
- [x] Ollama local LLM support
- [x] Google-style docstring format
- [x] Automatic docstring insertion

### Planned Features
- [ ] **JavaScript support** - AST parsing and docstring generation
- [ ] **C# support** - XML documentation comments
- [ ] **NumPy docstring format** support
- [ ] **Configuration file** support (YAML/JSON)
- [ ] **Custom prompts** for different documentation styles
- [ ] **Batch processing** with progress indicators
- [ ] **Git integration** - only process changed files

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Python's `ast` module for robust code parsing
- Powered by OpenAI's GPT models and Ollama for local LLM support
- Inspired by the need for consistent, high-quality code documentation

---

**Made with love by [Brenden](https://github.com/bdog18)**