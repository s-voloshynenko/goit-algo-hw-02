from collections import deque

def is_palindrome(string_to_check):
    symbols_deque = deque(char for char in string_to_check.lower() if char != " ")

    while len(symbols_deque) > 1:
        if symbols_deque.popleft() != symbols_deque.pop():
            return False
    return True

strings = [
    "tenet",
    "test",
    "123 321",
]

if __name__ == "__main__":
    for string in strings:
        print(f"'{string}' is {'a'if is_palindrome(string) else "not a"} palindrom.")
