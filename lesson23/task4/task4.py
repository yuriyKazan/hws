def reverse(input_str: str) -> str:
    if len(input_str) == 1 or len(input_str) == 0:
        return input_str
    return input_str[-1] + reverse(input_str[: -1])


reverse("hello") == "olleh"
reverse("o") == "o"
