from flask import Flask, request
from flask import jsonify

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        response = "Hello, I got a GET"
    elif request.method == 'POST':
        response = "Hello, POST method"
    else:
        # iako nema smisla jer su dozovljene samo GET i POST metode ali neka se nađe  za sada :-)
        response = "Something else I don't understand"
    return jsonify(response)
