from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


@dataclass
class CodeElement:
    name: str
    type: str  # 'function', 'class', 'module'
    source_code: str
    docstring: Optional[str] = None
    line_number: int = 0


@dataclass
class FileAnalysis:
    file_path: Path
    functions: List[CodeElement]
    classes: List[CodeElement]
    module_docstring: Optional[str] = None
