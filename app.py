from flask import Flask
from os import environ as env

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World - from Crossvale on OCP Azure! " + env.get('password')

if __name__ == "__main__":
     app.run(host="0.0.0.0", debug=True, port=5000)
