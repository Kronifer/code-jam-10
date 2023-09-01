from flask import Flask, request

from processing import generate_alphabet

app = Flask(__name__)


@app.route("/")
def index():  # noqa: D103
    return "<h1>Placeholder, see <a href=/generate>/generate</a> for integration with image_processing module</h1>"


@app.route("/generate")
def generate():  # noqa: D103
    key = request.args.get("key", None)
    if key is None:
        return "Please provide a key using URL flags", 400, {"Content-Type": "text/plain"}
    return str(generate_alphabet(key)), 200, {"Content-Type": "application/json"}


app.run("127.0.0.1", 8080)  # TODO: Replace with Gunicorn
