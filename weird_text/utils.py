import re
from typing import List


def get_words(text: str) -> List[str]:
    """
    Get list of words from given text

    :param text: input text
    :return: list of words
    """
    words = re.sub(r"(\W+)", " ", text).split(" ")
    words = [word for word in words if len(word) > 0]
    return words


def get_middle_part(word: str) -> str:
    """
    Get middle part (without first and last character) part of the word

    :param word: input word
    :return: middle part of the word
    """
    return word[1:-1]
