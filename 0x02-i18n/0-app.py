#!/usr/bin/env python3
"""A flask app"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def main():
    """A main function that displays a basic index.html page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
