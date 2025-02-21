# id: 133749115


from typing import Optional


def decrypt_instructions(instruction: Optional[str]) -> str:
    """Декодирует строку с инструкциями"""
    decode_string = ''
    mulripliers = []
    mulriplier = ''
    stack = []
    for index in range(len(instruction)):
        if instruction[index].isdigit():
            mulriplier += instruction[index]
            
        elif instruction[index] == '[':
            mulripliers.append((int(mulriplier), index))
            mulriplier = ''
        elif instruction[index] == ']':
            if instruction[mulripliers[-1][1]+1 :index-1]:
                decode_string += instruction[mulripliers[-1][1]:index] * mulripliers[-1][0]          
            else:  
                decode_string += instruction[index-1] * mulripliers[-1][0]  
            mulripliers.pop()
        else:
            ...
            #for multiplier in mulripliers:
            #    decode_string += instruction[index] * multiplier
    return decode_string


if __name__ == '__main__':
    print(decrypt_instructions(input()))
