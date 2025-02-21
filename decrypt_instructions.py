# id: 133789032


def decrypt_instructions(instruction: str) -> str:
    """Декодирует строку с инструкциями"""
    decode_instruction = ''
    curr_values = ''
    multiplier = 0
    stack = []
    for char in instruction:
        if char.isdigit():
            multiplier = multiplier * 10 + int(char)
        elif char == '[':
            stack.append((curr_values, multiplier))
            curr_values = ''
            multiplier = 0
        elif char == ']':
            prev_values, local_mulriplier = stack.pop()
            curr_values = prev_values + (curr_values * local_mulriplier)
            if stack == []:
                decode_instruction += curr_values
                curr_values = ''
        else:
            curr_values += char

    decode_instruction += curr_values
    return decode_instruction


if __name__ == '__main__':
    print(decrypt_instructions(input()))
