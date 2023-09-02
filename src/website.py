import base64
import os
from io import BytesIO

from flask import Flask, render_template, request
from PIL import Image

from .processing import read_message, write_message

template_dir = os.path.abspath("src/assets")
app = Flask(__name__, template_folder=template_dir)


@app.route("/")
def index():  # noqa: D103
    return render_template("base.html")


@app.route("/encode/", methods=["GET", "POST"])
def encode():  # noqa: D103
    if request.method == "GET":
        return render_template("encode.html")
    io = BytesIO()
    image = Image.open(request.files.get("image").stream)
    image, status = write_message(image, request.form["message"].lower(), request.form["key"])
    if not status:
        return (
            "ERROR: Please make sure your message is not too long, and that you don't have any unicode characters in your message (no emojis).",  # noqa: E501
            400,
            {"Content-Type": "text/plain"},
        )
    image.save(io, "PNG")
    io.seek(0)
    return render_template("display.html", src=f"data:image/png;base64,{base64.b64encode(io.read()).decode('utf-8')}")


@app.route("/decode/", methods=["GET", "POST"])
def decode():  # noqa: D103
    if request.method == "GET":
        return render_template("decode.html")
    image = Image.open(request.files.get("image").stream)
    return read_message(image, request.form["key"]), {"Content-Type": "text/plain"}
