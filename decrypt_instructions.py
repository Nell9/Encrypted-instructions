# id: 133910664

MAX_MULTIPLIER_SIZE = 300
MULTIPLIERS = tuple(str(i) for i in range(MAX_MULTIPLIER_SIZE))


def decrypt_encrypted_texts(encrypted_text: str) -> str:
    """Декодирует строку с инструкциями"""
    decoded_text = ''
    multiplier = ''
    stack = []
    for char in encrypted_text:
        match char:
            case char if (char in MULTIPLIERS):
                multiplier = multiplier + char
            case '[':
                stack.append([decoded_text, int(multiplier)])
                multiplier = ''
                decoded_text = ''
            case ']':
                prev_values, local_mulriplier = stack.pop()
                decoded_text = prev_values + decoded_text * local_mulriplier
            case _:
                decoded_text += char
    return decoded_text


if __name__ == '__main__':
    print(decrypt_encrypted_texts(input()))
