from pathlib import Path

from src.llm_clients.llm_client_factory import LLMClientFactory
from src.parsers.python_parser import PythonParser


def main() -> None:
    # Find Python files
    parser = PythonParser()
    llm_client = LLMClientFactory().create_client("openai")

    for py_file in Path("./src").glob("**/*.py"):
        if py_file.name.startswith("test_"):
            continue

        print(f"Processing {py_file}")
        analysis = parser.parse_file(py_file)

        # Generate docs for each function
        for func in analysis.functions:
            if func.name.startswith("generate_docs"):
                continue
            if not func.docstring:  # Only generate if missing
                docs = llm_client.generate_docs(func)
                print(f"Generated docs for {func.name}")
                print(docs)
                print("-" * 50)
    return None


if __name__ == "__main__":
    main()
