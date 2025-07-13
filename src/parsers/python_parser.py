import ast
from pathlib import Path
from typing import List

from src.core.analyzer import CodeElement, FileAnalysis


class PythonParser:
    def parse_file(self, file_path: Path) -> FileAnalysis:
        """
        Parses a Python file to extract functions and classes with their metadata.
        Returns a FileAnalysis object containing the parsed elements.

        Args:
            file_path (Path): Path to the Python file to parse.

        Returns:
            FileAnalysis: Object containing lists of functions and classes found.
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
        Extract source code segment corresponding to an AST node from the given content.

        Args:
            node (ast.AST): The AST node to extract source for.
            content (str): The full source code as a string.

        Returns:
            str: The source code segment for the node, or an empty string if unavailable.
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
