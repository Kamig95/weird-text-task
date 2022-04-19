from typing import Final

from flask import Flask, request

from weird_text import decode, encode
from weird_text.exceptions import WrongEncodedMessageException

app = Flask(__name__)

TEXT_ARG_NEEDED: Final[str] = "`text` argument needed"


@app.route("/v1/encode")
def encode_endpoint():
    text = request.args.get("text")
    if not text:
        return TEXT_ARG_NEEDED, 400
    return encode(request.args.get("text"))


@app.route("/v1/decode")
def decode_endpoint():
    text = request.args.get("text")
    if not text:
        return TEXT_ARG_NEEDED, 400
    try:
        decoded_text = decode(text)
    except WrongEncodedMessageException as e:
        return str(e), 400
    return decoded_text
