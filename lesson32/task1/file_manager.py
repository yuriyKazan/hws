from variables import FILE_NAME


def write_to_file(file_prefix: str, content: str, cont_encoding: str) -> None:
    with open(file_prefix + FILE_NAME, 'w', encoding=cont_encoding) as file_to_write:
        file_to_write.write(content)
