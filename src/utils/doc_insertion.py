def find_closing_paren(func_str: str) -> int:
    """
    Finds the line index where the parentheses in the input string are balanced.
    
    Args:
        func_str (str): Multiline string containing parentheses.
    
    Returns:
        int: Index of the line where parentheses close completely.
    """
    depth = 0
    for i, line in enumerate(func_str.split("\n")):
        if "(" in line:
            depth += line.count("(")
        if ")" in line:
            depth -= line.count(")")
            if depth == 0:
                return i
    return 0  # change this to throw an error
