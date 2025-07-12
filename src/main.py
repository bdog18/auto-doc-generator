# from pathlib import Path

# from src.core.parsers.python_parser import PythonParser
# from src.utils.llm_client import LLMClient
# from src.config.settings import settings


def main() -> None:
    # Find Python files
    # parser = PythonParser()
    # llm_client = LLMClient()

    # for py_file in Path(".").glob("**/*.py"):
    #     if py_file.name.startswith("test_"):
    #         continue

    #     print(f"Processing {py_file}")
    #     analysis = parser.parse_file(py_file)

    #     # Generate docs for each function
    #     for func in analysis.functions:
    #         if not func.docstring:  # Only generate if missing
    #             # docs = llm_client.generate_docs(func)
    #             print(f"Generated docs for {func.name}")
    #             print(docs)
    #             print("-" * 50)
    return None


if __name__ == "__main__":
    main()
