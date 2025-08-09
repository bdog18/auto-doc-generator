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
        Retrieves a parser class based on the file extension and returns an instance of it if found.
        
        Args:
            cls (type): The class containing parsers for different extensions.
            file_path (Path): The path to the file whose extension determines the parser.
        
        Returns:
            Optional[Any]: An instance of the parser class or None if no matching parser is found.
        """
        extension = file_path.suffix.lower()
        parser_class = cls.PARSERS.get(extension)
        if parser_class:
            return parser_class()
        return None
