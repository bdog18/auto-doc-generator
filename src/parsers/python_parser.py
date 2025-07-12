import ast
from pathlib import Path
from typing import List

from src.core.analyzer import CodeElement, FileAnalysis


class PythonParser:
    def parse_file(self, file_path: Path) -> FileAnalysis:
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

        return FileAnalysis(file_path=file_path, functions=functions, classes=classes)

    def _get_source(self, node: ast.AST, content: str) -> str:
        lines = content.split("\n")
        if hasattr(node, "lineno") and hasattr(node, "end_lineno"):
            return "\n".join(
                lines[
                    getattr(node, "lineno", 1)
                    - 1 : getattr(node, "end_lineno", getattr(node, "lineno", 1))
                ]
            )
        return ""
