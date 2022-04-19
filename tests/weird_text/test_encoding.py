from unittest.mock import MagicMock, patch

import pytest

from weird_text import encode, shuffle


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        pytest.param("", ""),
        pytest.param("a", "a"),
        pytest.param("in", "in"),
        pytest.param("one", "one"),
        pytest.param("this", "tihs"),
    ],
)
def test_shuffle_short(input_text: str, expected_output: str):
    assert expected_output == shuffle(input_text)


def test_shuffle_long():
    input_text = "water"
    for i in range(100):
        output_text = shuffle(input_text)
        assert output_text in ["waetr", "weatr", "wetar", "wtaer", "wtear"]


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        pytest.param(
            "",
            "\n—weird—\n\n—weird—\n",
        ),
        pytest.param(
            "at",
            "\n—weird—\nat\n—weird—\n",
        ),
        pytest.param(
            "This is a long looong test sentence, \nwith some big (biiiiig) words!",
            "\n—weird—\nT__s is a l__g l____g t__t s______e, \nw__h s__e big (biiiiig) w___s!\n—weird—\nlong looong "
            "sentence some test This with words",
        ),
    ],
)
@patch("weird_text.encoding.random")
def test_encode(random_mock: MagicMock, input_text: str, expected_output: str):
    random_mock.sample = lambda text, length: ["_"] * length
    assert expected_output == encode(input_text)
