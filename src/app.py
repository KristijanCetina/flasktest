from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        response = "I got a GET"
    elif request.method == 'POST':
        response = "Hello, POST method"
    else:
        # iako nema smisla jer su dozovljene samo GET i POST metode ali neka se nađe  za sada :-)
        response = "Something else I don't understand"
    return jsonify(response)


@app.route("/sensors", methods=['GET'])
def returnSensorsData():
    return send_from_directory("./", "sensors.json")


@app.route("/experiments", methods=['GET'])
def returnExperimentsData():
    return send_from_directory("./", "experiments.json")
