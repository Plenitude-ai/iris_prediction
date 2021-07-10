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


X, y = load_iris(return_X_y=True, as_frame=True)
df = pd.concat([X, y], axis=1)

# ### Train Test split

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(df.drop("target", axis=1), df["target"])

# # Modelling
# ### XGB

model_xgb = xgboost.sklearn.XGBClassifier()

# ### Train

model_xgb.fit(X_train, y_train)


pred = model_xgb.predict(X_test)
pred_proba = model_xgb.predict_proba(X_test)

# ### Evaluation
# We clearly overfit our data, but no problem this is not the interesting part of the project

sklearn.metrics.roc_auc_score(y_test, pred_proba, multi_class='ovr')

# # Serialization of model

with open("model.pkl", "wb") as file:
    pickle.dump(model_xgb, file)
    




# # Prediction for 1 observation

with open("model.pkl", "rb") as file:
    model_loaded = pickle.load(file)


observation = X_test.sample(n=1)


pred_obs = model_loaded.predict(observation)
pred_name = target_names[int(pred_obs)]
print("\n\n\n")
print(pred_name)