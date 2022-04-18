import random
from typing import Final, List, Tuple

from weird_text.utils import get_words, get_middle_part

MAGIC_WORD: Final[str] = "\n—weird—\n"


def encode(text: str) -> str:
    """
    Encode text using WeirdText method

    :param text: text to encode
    :return: encoded text
    """
    words = get_words(text)
    shuffled_words = [shuffle(word) for word in words]
    encoded_text, changed_words = replace_words(text, words, shuffled_words)
    changed_words.sort(key=lambda w: w.lower())
    return MAGIC_WORD + encoded_text + MAGIC_WORD + " ".join(changed_words)


def replace_words(
    text: str, words: List[str], shuffled_words: List[str]
) -> Tuple[str, List[str]]:
    """
    Replace words in text with shuffled words

    :param text: text with words to replace
    :param words: words that have to be replaced
    :param shuffled_words: shuffled versions of words to replace
    :return: text with changed words and changed words
    """
    changed_words = []
    for word, shuffled_word in zip(words, shuffled_words):
        if word == shuffled_word:
            continue
        text = text.replace(word, shuffled_word, 1)
        changed_words.append(word)
    return text, changed_words


def shuffle(word: str) -> str:
    """
    Shuffle middle part (without first and last) of the word as long until the word is different from the original

    :param word: word to be changed
    :return: shuffled word
    """
    if len(word) < 4:
        return word
    if len(set(get_middle_part(word))) == 1:
        return word
    new_word = word
    while word == new_word:
        new_word = "".join(
            [word[0]] + random.sample(get_middle_part(word), len(word) - 2) + [word[-1]]
        )
    return new_word
