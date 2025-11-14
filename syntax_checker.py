import ast
import sys

def check_syntax(filename):
    with open(filename, 'r') as f:
        source = f.read()
    try:
        ast.parse(source)
        print(f"Syntax is valid in {filename}")
    except SyntaxError as e:
        print(f"Syntax error in {filename} at line {e.lineno}: {e.msg}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        check_syntax(sys.argv[1])
    else:
        print("Usage: python syntax_checker.py <filename>")
