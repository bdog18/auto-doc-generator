import tempfile
from pathlib import Path

from src.parsers.python_parser import PythonParser


class TestPythonParser:
    def setup_method(self) -> None:
        """Set up test fixtures before each test method."""
        self.parser = PythonParser()

    def test_parse_simple_function(self) -> None:
        """Test parsing a simple function without docstring."""
        test_code = """def add(a: int, b: int) -> int:
                        return a + b
                    """
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            print(f)
            f.write(test_code)
            f.flush()

            analysis = self.parser.parse_file(Path(f.name))

            assert len(analysis.functions) == 1
            assert analysis.functions[0].name == "add"
            assert analysis.functions[0].type == "function"
            assert analysis.functions[0].docstring is None
            assert analysis.functions[0].line_number == 1

    def test_parse_function_with_docstring(self) -> None:
        """Test parsing a function that already has a docstring."""
        test_code = '''def multiply(x: int, y: int) -> int:
                        """Multiplies two integers."""
                        return x * y
                    '''
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            print(f)
            f.write(test_code)
            f.flush()

            analysis = self.parser.parse_file(Path(f.name))

            assert len(analysis.functions) == 1
            assert analysis.functions[0].docstring == "Multiplies two integers."

    def test_parse_class(self) -> None:
        """Test parsing a class definition."""
        test_code = '''class Calculator:
                            """A simple calculator class."""

                            def add(self, a: int, b: int) -> int:
                                return a + b
                    '''
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            print(f)
            f.write(test_code)
            f.flush()

            analysis = self.parser.parse_file(Path(f.name))

            assert len(analysis.classes) == 1
            assert len(analysis.functions) == 1  # method inside class
            assert analysis.classes[0].name == "Calculator"
            assert analysis.classes[0].docstring == "A simple calculator class."
