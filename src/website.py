import base64
from io import BytesIO

from flask import Flask, render_template, request
from PIL import Image

from .processing import (
    read_message_a, read_message_rgb, write_message_a, write_message_rgb
)

app = Flask(__name__)
app.url_map.strict_slashes = False  # Fix issues with some browsers, thanks Grace


@app.route("/")
def index():  # noqa: D103
    return render_template("index.html")


@app.route("/alpha")
def alpha():  # noqa: D103
    return render_template("alpha.html")


@app.route("/rgb")
def rgb():  # noqa: D103
    return render_template("rgb.html")


@app.route("/alpha/encode", methods=["GET", "POST"])
def encode_a():  # noqa: D103
    if request.method == "GET":
        return render_template("encode_a.html")
    io = BytesIO()
    image = Image.open(request.files.get("image").stream)
    image, status = write_message_a(image, request.form["message"].lower(), request.form["key"])
    if not status:
        return (
            "ERROR: Please make sure your message is not too long, and that you don't have any unicode characters in your message (no emojis).",  # noqa: E501
            400,
            {"Content-Type": "text/plain"},
        )
    image.save(io, "PNG")
    io.seek(0)
    return render_template("display.html", src=f"data:image/png;base64,{base64.b64encode(io.read()).decode('utf-8')}")


@app.route("/alpha/decode", methods=["GET", "POST"])
def decode_a():  # noqa: D103
    if request.method == "GET":
        return render_template("decode_a.html")
    image = Image.open(request.files.get("image").stream)
    return read_message_a(image, request.form["key"]), {"Content-Type": "text/plain"}


@app.route("/rgb/encode", methods=["GET", "POST"])
def encode_rgb():  # noqa: D103
    if request.method == "GET":
        return render_template("encode_rgb.html")
    image, status = write_message_rgb(request.form["message"], request.form["key"])
    if not status:
        return (
            "ERROR: Please make sure your message is not too long, and that you don't have any unicode characters in your message (no emojis).",  # noqa: E501
            400,
            {"Content-Type": "text/plain"},
        )
    io = BytesIO()
    image.save(io, "PNG")
    io.seek(0)
    return render_template("display.html", src=f"data:image/png;base64,{base64.b64encode(io.read()).decode('utf-8')}")


@app.route("/rgb/decode", methods=["GET", "POST"])
def decode_rgb():  # noqa: D103
    if request.method == "GET":
        return render_template("decode_rgb.html")
    return read_message_rgb(Image.open(request.files.get("image").stream), request.form["key"]), {
        "Content-Type": "text/plain"
    }
