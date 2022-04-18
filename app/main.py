from flask import Flask, request
from weird_text import encode, decode

app = Flask(__name__)


@app.route("/v1/encode")
def encode_endpoint():
    return encode(request.args.get("text"))


@app.route("/v1/decode")
def decode_endpoint():
    text = request.args.get("text")
    return decode(text)


@app.route("/")
def root():
    return "Welcome"
