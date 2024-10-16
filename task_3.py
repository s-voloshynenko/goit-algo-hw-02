def is_symmetric(string_to_check):
    brackets = {'(': ')', '{': '}', '[': ']'}
    symbols_stack = []

    for char in string_to_check:
        if char in brackets.keys():
            symbols_stack.append(char)
        elif char in brackets.values():
            if not symbols_stack or brackets[symbols_stack.pop()] != char:
                return False

    return not symbols_stack

strings = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }",
    "(({)})"
]

if __name__ == "__main__":
    for string in strings:
        print(f"'{string}' is {'symmetric' if is_symmetric(string) else "not symmetric"}.")
