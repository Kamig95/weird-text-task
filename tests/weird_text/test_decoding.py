import pytest

from weird_text import decode, encode

from weird_text.exceptions import WrongEncodedMessageException


@pytest.mark.parametrize(
    "input_text",
    [
        pytest.param(""),
        pytest.param("a"),
        pytest.param("in"),
        pytest.param("one"),
        pytest.param("this"),
        pytest.param(
            "This is a long looong test sentence, \nwith some big (biiiiig) words!"
        ),
    ],
)
def test_decode(input_text: str):
    assert input_text == decode(encode(input_text))


def test_decode_exception():
    with pytest.raises(WrongEncodedMessageException):
        decode("Some text in wrong format.")
