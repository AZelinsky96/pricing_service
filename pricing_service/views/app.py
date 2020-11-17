from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def new_item():
    return "Hello World"


def main():
    app.run(debug=True)
