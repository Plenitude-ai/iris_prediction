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
    return flask.render_template("index.html", prediction="No prediction", prediction_service_name="iris_prediction")

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

    # iris_prediction_service_name_in_docker_compose = "iris_prediction"
    # root = "http:/"+iris_prediction_service_name_in_docker_compose+"/"
    root = "https://iris-plenitudeai.herokuapp.com"
    response = requests.get(root+'/pred_args?'+"sepal_length={}&sepal_width={}&petal_length={}&petal_width={}".format(sepal_length, sepal_width, petal_length, petal_width))
    prediction = response.text
    # prediction="COEJBVOJB"
    return flask.render_template("index.html", prediction=prediction)


################### RUN DE L'APP #########################
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)