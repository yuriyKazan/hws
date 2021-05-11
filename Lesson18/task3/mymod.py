def count_lines(name: str) -> int:
    with open(name) as read_file:
        return len(read_file.readlines())


def count_chars(name: str) -> int:
    with open(name) as read_file:
        return len(read_file.read())


def test(name: str) -> tuple:
    return count_lines(name), count_chars(name)
