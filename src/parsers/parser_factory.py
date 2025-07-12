# src/parsers/parser_factory.py
from pathlib import Path
from typing import Any, Dict, Optional, Type

from .python_parser import PythonParser

# from .javascript_parser import JavaScriptParser


class ParserFactory:
    PARSERS: Dict[str, Type] = {
        ".py": PythonParser,
        # '.js': JavaScriptParser,
        # '.ts': JavaScriptParser,
        # '.jsx': JavaScriptParser,
        # '.tsx': JavaScriptParser,
        # '.java': JavaParser,
        # '.cpp': CppParser,
        # '.c': CParser,
    }

    @classmethod
    def get_parser(cls, file_path: Path) -> Optional[Any]:
        extension = file_path.suffix.lower()
        parser_class = cls.PARSERS.get(extension)
        if parser_class:
            return parser_class()
        return None
