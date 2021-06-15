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


@app.route("/sensors", methods=['GET', 'POST'])
def returnSensorsData():
    if request.method == 'GET':
        return send_from_directory("./", "sensors.json")
    elif request.method == 'POST':
        print("Evo podataka iz POST metode")
        print(request.get_json(force=True, silent=False))
        return jsonify("End of transmission!")
    else:
        return jsonify("Something else I don't understand")


@app.route("/experiments", methods=['GET'])
def returnExperimentsData():
    return send_from_directory("./", "experiments.json")
