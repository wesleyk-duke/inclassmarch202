from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    """
    Returns the string "Hello, world" to the caller
    """
    return "Hello, world"


@app.route("/data/<name>", methods=["GET"])
def hello_name(
        name):  # the name variable being passed in here is the string that the client puts in the <name> part of the url
    return "Hello, {}".format(name)


@app.route("/data", methods=["GET"])
def getData():
    """
    Returns the data dictionary below to the caller as JSON
    """
    data = {
        "name": "Wesley",
        "team": "student"
    }
    return jsonify(
        data)  # respond to the API caller with a JSON representation of data. jsonify is important, as it sets response headers that indicate the respose is in JSON as well
