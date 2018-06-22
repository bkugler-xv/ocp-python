from flask import Flask
from os import environ as env
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    apikey = env.get('password')
    hostname = env.get('HOSTNAME')
    url = 'https://masterdnsx6zh27iw534mg.eastus.cloudapp.azure.com/api/v1/namespaces'
    headers = {'Authorization': 'Bearer '+str(apikey)}
    resp = requests.get(url, headers=headers, verify=False)	
    return "<p>Hello World - from Crossvale on OCP Azure on {}!</p> <p> About me: {} </p>".format(hostname, str(resp.json()))

if __name__ == "__main__":
     app.run(host="0.0.0.0", debug=True, port=5000)
