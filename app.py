from flask import Flask, render_template, request
from data import Book, BOOK_TYPES
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        **{"greeting": "Welcome!", "book_types": BOOK_TYPES.keys()}
    )


@app.route("/charges", methods=["POST"])
def charges():
    data = request.get_json()
    books = [Book(**item).to_dict() for item in data]
    return json.dumps(books)
