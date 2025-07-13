def find_closing_paren(func_str: str) -> int:
    depth = 0
    for i, line in enumerate(func_str.split("\n")):
        if "(" in line:
            depth += line.count("(")
        if ")" in line:
            depth -= line.count(")")
            if depth == 0:
                return i
    return 0  # change this to throw an error
