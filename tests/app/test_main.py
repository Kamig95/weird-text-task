from app.main import app, TEXT_ARG_NEEDED
from urllib.parse import quote


def test_encode_endpoint():
    response = app.test_client().get(f'/v1/encode?text={quote("this")}')
    assert response.data.decode("utf-8") == "\n—weird—\ntihs\n—weird—\nthis"


def test_encode_endpoint_no_input_text():
    response = app.test_client().get("/v1/encode")
    assert response.data.decode("utf-8") == TEXT_ARG_NEEDED
    assert response.status_code == 400


def test_decode_endpoint():
    decoded_text = "\n—weird—\ntihs\n—weird—\nthis"
    response = app.test_client().get(f"/v1/decode?text={quote(decoded_text)}")
    assert response.data.decode("utf-8") == "this"


def test_decode_endpoint_no_input_text():
    response = app.test_client().get("/v1/decode")
    assert response.data.decode("utf-8") == TEXT_ARG_NEEDED
    assert response.status_code == 400


def test_decode_endpoint_wrong_decoded_text():
    response = app.test_client().get(f'/v1/decode?text={quote("some random input")}')
    assert response.status_code == 400
