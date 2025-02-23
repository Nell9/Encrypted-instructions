# id: 133912933


MULTIPLIERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')


def decrypt(encrypted_text: str) -> str:
    """Декодирует строку с инструкциями"""
    decoded, multiplier = '', ''
    stack = []
    for char in encrypted_text:
        match char:
            case _ if char in MULTIPLIERS:
                multiplier = multiplier + char
            case '[':
                stack.append([decoded, int(multiplier)])
                multiplier, decoded = '', ''
            case ']':
                previouse_decoded, local_multiplier = stack.pop()
                decoded = previouse_decoded + decoded * local_multiplier
            case _:
                decoded += char
    return decoded


if __name__ == '__main__':
    print(decrypt(input()))
