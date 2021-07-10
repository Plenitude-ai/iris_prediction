# IMPORTS
import sys
import modelling_script
 

if __name__== '__main__':

    # TRAINING MODEL
    modelling_script.train_model(model_path="model.pkl")

    # GETTING THE ARGUMENTS
    args_str = sys.argv[1:]
    joint_str = " ".join([x for x in args_str])
    list_str = joint_str.strip('[]').split(',')
    arg = [float(x) for x in list_str]
    print("arg, ", arg)

    # PREDICTING ON OBSERVATION
    pred_name = modelling_script.predict_observation(arg, model_path="model.pkl")
    print("\n")
    print(pred_name)






# # FLASK
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'Hey, we have Flask in a Docker container!'
# if __name__== '__main__':
#   app.run(debug=True, use_reloader=False) #, host='0.0.0.0'

  