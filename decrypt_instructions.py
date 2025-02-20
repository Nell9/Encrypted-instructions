# id: 133749115

from typing import Optional, Iterable


BRACKETS = ('[', ']')
MULTIPLIER_CAPACITY = 3


def find_digits_count(string: str) -> Optional[int]:
    """Возвращает количество чисел в строке."""
    digits_count = 0
    for char in string:
        if char.isdigit():
            digits_count += 1
        else:
            return digits_count
    return digits_count or None


def find_closed_bracket(string: Iterable) -> Optional[int]:
    """
    Возвращает издекс последней закрывающейся скобки.
    При входи [x[x]x] вернет 6.
    """
    stack = []
    for index, char in enumerate(string):
        if char in BRACKETS:
            stack.append(char)
        if stack[-1] == BRACKETS[1]:
            stack.pop()
            stack.pop()
        if stack == []:
            return index
    return None


def decrypt_instructions(instruction: str):
    """Декодирует строку с инструкциями"""
    decode_string = ''
    index = 0
    while index < len(instruction):
        if instruction[index].isdigit():
            digits_count = find_digits_count(
                instruction[index:index+MULTIPLIER_CAPACITY])
            multiplier = int(instruction[index:index+digits_count])
            index += digits_count
            right_index = index + find_closed_bracket(instruction[index:])
            decode_string += multiplier * decrypt_instructions(
                instruction[index+1:right_index]
                if right_index - index > 2
                else [instruction[index+1]])
            index = right_index
        else:
            decode_string += instruction[index]
        index += 1
    return decode_string


if __name__ == '__main__':
    print(decrypt_instructions(input()))
