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
        """
        Returns an instance of the parser corresponding to the file extension. 
        
        Args:
            file_path (Path): Path object representing the file.
        
        Returns:
            Optional[Any]: Instance of the parser class if found, otherwise None.
        """
        extension = file_path.suffix.lower()
        parser_class = cls.PARSERS.get(extension)
        if parser_class:
            return parser_class()
        return None
