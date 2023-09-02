import base64
from io import BytesIO

from flask import Flask, render_template, request
from PIL import Image

from processing import read_message, write_message

app = Flask(__name__)


@app.route("/")
def index():  # noqa: D103
    return render_template("index.html")


@app.route("/encode", methods=["GET", "POST"])
def encode():  # noqa: D103
    if request.method == "GET":
        return render_template("encode.html")
    io = BytesIO()
    image = Image.open(request.files.get('image').stream)
    write_message(image, request.form["message"], request.form["key"])[0].save(io, format="PNG")
    io.seek(0)
    return render_template("display.html",
                           src=f"data:image/png;base64,{base64.b64encode(io.read()).decode('utf-8')}")


@app.route("/decode", methods=["GET", "POST"])
def decode():  # noqa: D103
    if request.method == "GET":
        return render_template("decode.html")
    image = Image.open(request.files.get('image').stream)
    return read_message(image, request.form["key"])


app.run("127.0.0.1", 8080)  # TODO: Replace with Gunicorn
