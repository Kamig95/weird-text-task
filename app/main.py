from flask import Flask, request
from weird_text import encode, decode
from weird_text.exceptions import WrongEncodedMessageException

app = Flask(__name__)


@app.route("/v1/encode")
def encode_endpoint():
    return encode(request.args.get("text"))


@app.route("/v1/decode")
def decode_endpoint():
    text = request.args.get("text")
    try:
        decoded_text = decode(text)
    except WrongEncodedMessageException as e:
        return str(e), 400
    return decoded_text


@app.route("/")
def root():
    return "Welcome"
