
# # FLASK
import pickle
import flask
from flask import Flask, request
from flask.json import jsonify
import pandas as pd



app = Flask(__name__)


model_path = "model.pkl"
MODEL = pickle.load(open(model_path, "rb"))
TARGET_NAMES = ['setosa', 'versicolor', 'virginica']


@app.route('/', methods=["GET"])
def hello_world():
    """
    Home/index: Returns 'Welcome'
    ---
    get:
      summary: "Index"
      description: "returns 'welcome'"
      responses:
        "405":
          description: "Invalid input"
    """
    return 'Hey, we have Flask in a Docker container !'



@app.route('/pred_args', methods=["GET"])
def get_pred_args():
    # Retrieve query parameters related to this request.
    sepal_length = float(flask.request.args.get('sepal_length'))
    sepal_width = float(flask.request.args.get('sepal_width'))
    petal_length = float(flask.request.args.get('petal_length'))
    petal_width = float(flask.request.args.get('petal_width'))

    features = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], columns=["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"])
    pred_obs = MODEL.predict(features)
    pred_name = TARGET_NAMES[int(pred_obs)]
    return pred_name



@app.route('/pred_json', methods=["GET"])
def get_pred_json():
    # Retrieve query parameters related to this request.
    dict_data = request.json
    sepal_length = dict_data["sepal_length"]
    sepal_width = dict_data["sepal_width"]
    petal_length = dict_data["petal_length"]
    petal_width = dict_data["petal_width"]

    features = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], columns=["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"])
    pred_obs = MODEL.predict(features)
    pred_name = TARGET_NAMES[int(pred_obs)]
    return pred_name



if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

  