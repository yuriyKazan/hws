def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) == 1 or len(looking_str) == 0:
        return True
    if looking_str[index] == looking_str[-1]:
        return is_palindrome(looking_str[1: -1])
    return False


assert is_palindrome('mom')
assert is_palindrome('sassas')
assert is_palindrome('o')
