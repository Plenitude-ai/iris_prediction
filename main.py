# IMPORTS
import pickle
import pandas as pd

if __name__=="main":

    # GETTING THE ARGUMENTS
    arg = [7.3, 2.9, 6.3, 1.8]
    observation = pd.DataFrame([arg], columns=["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"])


    # OPENING MODEL
    with open("model.pkl", "rb") as file:
        model_loaded = pickle.load(file)


    # PREDICTING ON OBSERVATION
    pred_obs = model_loaded.predict(observation)

    target_names = ['setosa', 'versicolor', 'virginica']
    pred_name = target_names[int(pred_obs)]
    print("\n\n\n")
    print(pred_name)

    # GETTING BACK PREDICTION