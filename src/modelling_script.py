# # Iris Prediction
# We import the iris dataset, train and evaluate a XGBoost, and use this fitted model to make a prediction on a single observation.  
# The objective is then to be able to make predictions on demand using Flask server and docker container.



# ### Imports

import numpy as np
import pandas as pd
import pickle

import xgboost
import sklearn
from sklearn.datasets import load_iris

# # Load Data

# data = load_iris()
# data.target_names

target_names = ['setosa', 'versicolor', 'virginica']

def train_model(model_path="model.pkl"):
    """Loads Iris from sklearn, fits a XGBoots and stores it to the passed argument
    Returns X_test, y_test"""
    X, y = load_iris(return_X_y=True, as_frame=True)
    df = pd.concat([X, y], axis=1)

    # ### Train Test split
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(df.drop("target", axis=1), df["target"])

    # # Modelling
    # ### XGB
    model_xgb = xgboost.sklearn.XGBClassifier(use_label_encoder=False)

    # ### Train
    model_xgb.fit(X_train, y_train)

    # # Serialization of model
    with open(model_path, "wb") as file:
        pickle.dump(model_xgb, file)

    return X_test, y_test
    
def evaluate_model(model, X_test, y_test):
    """Returns AUC of given model"""
    pred = model.predict(X_test)
    pred_proba = model.predict_proba(X_test)
    # ### Evaluation
    # We clearly overfit our data, but no problem this is not the interesting part of the project
    auc = sklearn.metrics.roc_auc_score(y_test, pred_proba, multi_class='ovr')
    return auc


def predict_observation(arg, model_path="model.pkl"):
    if type(arg)==list:
        observation = pd.DataFrame([arg], columns=["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"])
    else:
        raise TypeError("arg should be List")
    # # Prediction for 1 observation
    with open(model_path, "rb") as file:
        model_loaded = pickle.load(file)
    pred_obs = model_loaded.predict(observation)

    target_names = ['setosa', 'versicolor', 'virginica']
    pred_name = target_names[int(pred_obs)]
    return pred_name




# # TRAINING MODEL
# train_model(model_path="model.pkl")

# # GETTING THE ARGUMENTS
# arg = [7.3, 2.9, 6.3, 1.8]



# # PREDICTING ON OBSERVATION
# pred_name = predict_observation(arg, model_path="model.pkl")
# print("\n\n\n")
# print(pred_name)