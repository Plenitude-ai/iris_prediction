import flask
from flask import Flask, request, render_template, jsonify
app = Flask(__name__)



#################### Page d'accueil #####################
@app.route('/')
def home():
    return flask.render_template("index.html", prediction=" --- ", prediction_service_name="iris_prediction")

################### Page avec la carte ##################
@app.route('/', methods=['GET'])
def show_map():
    #Coordonneeshttp://localhost:8888/notebooks/Documents/Work/Centrale/CodePython/HugZer%20Clean/FLASK.ipynb#
    adress = request.form['text_id']
    reponse = request.form['question']
    coord = get_coordonnees(adress)
    print(reponse)
    #Scores des stations
    df = get_station(coord, prices)
    
    #Meilleur Scores
    df2 = meilleur_score(df, adress)
        
    #Renvoi du template HTML, avec la variable JSON
    return render_template("map.html",
                           coordinates = invert_coord(coord),
                           result = df,
                          result2 = df2,
                          adresse = adress,
                          oui = reponse)


################### RUN DE L'APP #########################
if __name__ == "__main__":
    app.run()