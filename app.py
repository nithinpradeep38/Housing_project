from flask import Flask
import sys
from housing.logger import logging

app= Flask(__name__)

@app.route("/", methods= ['GET', 'POST'])

def index():
    logging.info("Testing logging")
    return "CI CD testing"


if __name__ == "__main__":
    app.run(debug=True)