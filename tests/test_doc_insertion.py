from src.utils.doc_insertion import find_closing_paren


class TestDocInsertion:
    def test_simple_function_signature(self) -> None:
        """Test finding closing paren in simple function."""
        func_str = "def add(a, b):\n    return a + b"
        result = find_closing_paren(func_str)
        assert result == 0

    def test_multiline_function_signature(self) -> None:
        """Test finding closing paren in multiline function."""
        func_str = """def complex_function(
                        param1: str,
                        param2: int
                    ):
                        return param1 * param2"""
        result = find_closing_paren(func_str)
        assert result == 3

    def test_nested_parentheses(self) -> None:
        """Test function with nested parentheses in default values."""
        func_str = """def func_with_defaults(
                        data: list = list(),
                        callback: callable = lambda x: print(x)
                    ):
                        pass"""
        result = find_closing_paren(func_str)
        assert result == 3
