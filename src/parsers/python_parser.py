import ast
from pathlib import Path
from typing import List

from src.core.analyzer import CodeElement, FileAnalysis


class PythonParser:
    def parse_file(self, file_path: Path) -> FileAnalysis:
        """
        Parses a Python file to extract functions and classes, returning their details including source code and docstrings.
        
        Args:
            file_path (Path): The path to the Python file to be parsed.
        
        Returns:
            FileAnalysis: An object containing the paths of the file and its parsed components such as functions and classes.
        """
        with open(file_path, "r") as f:
            content = f.read()

        tree = ast.parse(content)
        functions = []
        classes: List[CodeElement] = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append(
                    CodeElement(
                        name=node.name,
                        type="function",
                        source_code=self._get_source(node, content),
                        docstring=ast.get_docstring(node),
                        line_number=node.lineno,
                    )
                )
            elif isinstance(node, ast.ClassDef):
                classes.append(
                    CodeElement(
                        name=node.name,
                        type="class",
                        source_code=self._get_source(node, content),
                        docstring=ast.get_docstring(node),
                        line_number=node.lineno,
                    )
                )

        return FileAnalysis(file_path=file_path, functions=functions, classes=classes)

    def _get_source(self, node: ast.AST, content: str) -> str:
        """
        Retrieves the source code of a given AST node from its content.
        
        Args:
            node (ast.AST): The abstract syntax tree node.
            content (str): The string containing the full source code.
        
        Returns:
            str: The source code of the specified AST node, or an empty string if not applicable.
        """
        lines = content.split("\n")
        if hasattr(node, "lineno") and hasattr(node, "end_lineno"):
            return "\n".join(
                lines[
                    getattr(node, "lineno", 1)
                    - 1 : getattr(node, "end_lineno", getattr(node, "lineno", 1))
                ]
            )
        return ""


if __name__ == "__main__":
    # Example usage
    parser = PythonParser()
    analysis = parser.parse_file(
        Path("C:\\Users\\Brend\\Documents\\repos\\doc-generator-agent\\tests\\test.py")
    )  # Replace with your file path
    # print(analysis)
    for func in analysis.functions:
        print(f"Function: {func.name}, Docstring: {func.docstring}")
        print(f"Source Code:\n{func.source_code}\n")
