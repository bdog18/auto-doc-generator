from pathlib import Path

from src.llm_clients.llm_client_factory import LLMClientFactory
from src.parsers.python_parser import PythonParser
from src.utils.doc_insertion import find_closing_paren


def main() -> None:
    """
    Generates documentation for Python functions in specified files using a parser and an LLM client.
    
    Args:
        None
    
    Returns:
        None
    """
    # Find Python files
    parser = PythonParser()
    llm_client = LLMClientFactory().create_client("ollama")

    for py_file in Path("./src").glob("**/*.py"):
        if py_file.name.startswith("test_"):
            continue

        print(f"Processing {py_file}")
        analysis = parser.parse_file(py_file)

        # Generate docs for each function
        for func in sorted(
            analysis.functions, key=lambda x: x.line_number, reverse=True
        ):
            if not func.docstring:  # Only generate if missing
                docs = llm_client.generate_docs(func)
                print(f"Generated docs for {func.name}")
                print(f"Line {func.line_number}")
                print(docs)
                print("-" * 50)

                with open(py_file, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                    # Get the function line to determine indentation
                    func_line = lines[func.line_number - 1]
                    indent = len(func_line) - len(func_line.lstrip())

                    # Process the docstring and add proper indentation
                    docstring_lines = docs.split("\n")
                    formatted_lines = []

                    for line in docstring_lines:
                        if line.strip():  # Only process non-empty lines
                            # Add proper indentation (function indent + 4 spaces)
                            formatted_lines.append(" " * (indent + 4) + line + "\n")
                        else:
                            # Keep empty lines but with proper indentation
                            formatted_lines.append(" " * (indent + 4) + "\n")

                    # Insert all docstring lines after the function definition
                    doc_line = find_closing_paren(func.source_code)
                    for i, formatted_line in enumerate(formatted_lines):
                        lines.insert(
                            func.line_number + doc_line + i,
                            formatted_line,
                        )

                with open(py_file, "w", encoding="utf-8") as f:
                    f.writelines(lines)
    return None


if __name__ == "__main__":
    main()
