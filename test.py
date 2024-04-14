import os
def occurrences(bs: str, cs: str) -> int:
    return sum(1 for char in bs if char in set(cs))

os.system("cls")
# Test cases
print(occurrences("a", "aaa"))            # Expected output: 1
print(occurrences("Hello", "Hello"))      # Expected output: 5
print(occurrences("fooled", "hello world"))  # Expected output: 7
