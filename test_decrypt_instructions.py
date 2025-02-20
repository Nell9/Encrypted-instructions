import pytest

from main import decrypt_instructions

STRINGS = {
    '3[a]2[bc]': 'aaabcbc',
    '3[a2[c]]': 'accaccacc',
    '2[abc]3[cd]ef': 'abcabccdcdcdef'
}


def test_decrypt_instructions():
    for string in STRINGS:
        assert decrypt_instructions(string) == STRINGS[string]
