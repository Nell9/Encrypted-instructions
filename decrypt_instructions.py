# id: 133918958


import string


DIGITS = string.digits


def decrypt(encrypted: str) -> str:
    """Декодирует строку с инструкциями"""
    decoded = ''
    multiplier = ''
    stack = []
    for char in encrypted:
        match char:
            case _ if char in DIGITS:
                multiplier = multiplier + char
            case '[':
                stack.append((decoded, int(multiplier)))
                multiplier = ''
                decoded = ''
            case ']':
                previouse_decoded, multiplier_for_decoded = stack.pop()
                decoded = previouse_decoded + decoded * multiplier_for_decoded
            case _:
                decoded += char
    return decoded


if __name__ == '__main__':
    print(decrypt(input()))
