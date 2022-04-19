from weird_text.encoding import MAGIC_WORD
from weird_text.exceptions import WrongEncodedMessageException
from weird_text.utils import get_middle_part, get_words

from collections import Counter




def decode(encoded_text: str) -> str:
    """
    Decode text encoded WeirdText method

    :param encoded_text: text encoded with WeirdText method
    :return: decoded text
    """
    text_parts = encoded_text.split(MAGIC_WORD)
    if len(text_parts) != 3:
        raise WrongEncodedMessageException(
            repr(
                f"Wrong input format. Use WeirdText format: {MAGIC_WORD}decoded text{MAGIC_WORD}sorted changed words"
            )
        )

    encoded_part = text_parts[1]
    original_words = text_parts[2].split()
    words = get_words(encoded_part)
    for org_word in original_words:
        for decoded_word in words:
            if is_middle_anagram(org_word, decoded_word):
                encoded_part = encoded_part.replace(decoded_word, org_word)
    return encoded_part


def is_middle_anagram(first_word: str, second_word: str) -> bool:
    """
    Check if middle parts (without first and last letter) of two words are anagrams

    :param first_word: first word to check
    :param second_word: second word to check
    :return: True if middle parts of two words are anagrams, otherwise False
    """
    return Counter(get_middle_part(first_word)) == Counter(get_middle_part(second_word))
