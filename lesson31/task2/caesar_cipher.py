# c = (x + n) % 26

def encrypt(text, shift):
    encrypted_list = []

    for symbol in text:
        # check if character is an uppercase letter
        if symbol.isupper():
            # find the position in 0-25
            symbol_unicode = ord(symbol)
            symbol_index = symbol_unicode - ord("A")
            # perform the shift
            new_index = (symbol_index + shift) % 26
            # convert to new character
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            # append to encrypted string
            encrypted_list.append(new_character)
        elif symbol.islower():  # check if its a lowercase character

            # subtract the unicode of 'a' to get index in [0-25) range
            symbol_index = ord(symbol) - ord('a')

            symbol_shifted = (symbol_index + shift) % 26 + ord('a')

            symbol_new = chr(symbol_shifted)
            encrypted_list.append(symbol_new)

        elif symbol.isdigit():

            # if it's a number,shift its actual value
            symbol_new = (int(symbol) + shift) % 10

            encrypted_list.append(str(symbol_new))
        else:
            # since character is not uppercase, leave it as it is
            encrypted_list += [symbol]

    return ''.join(encrypted_list)


def decrypt(ciphertext, key):
    decrypted = ""
    for c in ciphertext:
        if c.isupper():
            c_index = ord(c) - ord('A')
            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isdigit():
            # if it's a number,shift its actual value
            c_og = (int(c) - key) % 10
            decrypted += str(c_og)
        else:
            # if its neither alphabetical nor a number, just leave it like that
            decrypted += c
    return decrypted
