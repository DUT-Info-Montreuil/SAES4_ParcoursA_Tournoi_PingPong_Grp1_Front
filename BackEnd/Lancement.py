from flask import Flask
#from flask_cors import CORS
from tournoi_routes import tournoi_bp
from personne_routes import personne_bp
from match_routes import match_bp
from lieu_routes import lieu_bp



app = Flask(__name__)
#cors = CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, world!'


app.register_blueprint(tournoi_bp, url_prefix='/api/tournois')
app.register_blueprint(personne_bp, url_prefix='/api/personnes')
app.register_blueprint(match_bp, url_prefix='/api/matchs')
app.register_blueprint(lieu_bp, url_prefix='/api/lieus')




if __name__ == '__main__' :
    app.run(debug=True)
