import flask
from flask import Flask, request, render_template, jsonify
import requests
app = Flask(__name__)

import logging
log = logging.getLogger("my-logger")



#################### Page d'accueil #####################
@app.route('/')
@app.route('/index')
def home():
    vars = {"prediction": "NO PREDICTION"}
    return flask.render_template("index.html", data=vars)

################### Page avec la carte ##################
@app.route('/', methods=['POST'])
def show_prediction():
    #Coordonneeshttp://localhost:8888/notebooks/Documents/Work/Centrale/CodePython/HugZer%20Clean/FLASK.ipynb#
    #Renvoi du template HTML, avec la variable JSON

    sepal_length = request.form['sepal_length']
    sepal_width = request.form['sepal_width']
    petal_length = request.form['petal_length']
    petal_width = request.form['petal_width']

    print("sepal_length, sepal_width, petal_length, petal_width : ", sepal_length, sepal_width, petal_length, petal_width)
    log.info("sepal_length, sepal_width, petal_length, petal_width : ", sepal_length, sepal_width, petal_length, petal_width)

    # root = "https://iris-plenitudeai.herokuapp.com"

    # iris_prediction_service_name_in_docker_compose
    root = "http://iris_prediction:80"
    
    response = requests.get(root+'/pred_args?'+"sepal_length={}&sepal_width={}&petal_length={}&petal_width={}".format(sepal_length, sepal_width, petal_length, petal_width))
    prediction = response.text
    vars = {"prediction": prediction,
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width}
    return flask.render_template("index.html", data=vars)


################### RUN DE L'APP #########################
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)