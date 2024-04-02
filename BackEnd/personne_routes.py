from flask import Blueprint, jsonify, request
from pymongo import MongoClient
import json
from bson import json_util  # Importez json_util depuis bson pour gérer la sérialisation des objets datetime
import Connection
personne_bp = Blueprint('personnes', __name__)

connection = Connection.Connection()
db = connection.get_database()

@personne_bp.route('/', methods=['GET'])
def get_personne_list():
    personnes = db.personne.find()
    liste_personne = list(personnes)
    liste_personnes_json = json_util.dumps(liste_personne, default=json_util.default)  # Utilisez json_util.default pour gérer la sérialisation des objets datetime
    return liste_personnes_json


@personne_bp.route('/<int:personne_id>', methods=['GET'])
def get_personne_id(personne_id):
    personne = db.personne.find_one({'_id': personne_id})
    if personne:
        return jsonify(personne)
    else:
        return jsonify({"message": "Personne non trouvée"}), 404  # Renvoie une réponse JSON avec un code de statut 404


@personne_bp.route('/<string:personne_nom>/<string:personne_prenom>/<string:personne_dateNaissance>/<string:personne_genre>/<string:personne_niveau>/<string:personne_premierSecours>', methods=['POST'])
def add_personne(personne_nom, personne_prenom, personne_dateNaissance, personne_genre, personne_niveau, personne_premierSecours):
    personne_id = db.personne.find_one({}, {'_id': 1}, sort=[('_id', -1)])
    if personne_id is not None:
        personne_id_int = int(personne_id['_id']) + 1
    else:
        personne_id_int = 1
    db.personne.insert_one(
        {"_id": personne_id_int, "nom": personne_nom, "prenom": personne_prenom, "dateNaissance": personne_dateNaissance, "genre": personne_genre,
         "niveau": personne_niveau, "premierSecours": personne_premierSecours}
    )
    return jsonify({"message": "Personne ajoutée avec succès"}), 200


@personne_bp.route('/', methods=['POST'])
def add2_personne():
    data = request.json

    required_fields = ['nom', 'prenom', 'dateNaissance', 'genre', 'niveau', 'premierSecours']
    if not all(field in data for field in required_fields):
        return jsonify({"message": "Certains champs requis sont manquants"}), 400

    try:
        personne_id = db.personne.find_one({}, {'_id': 1}, sort=[('_id', -1)])
        if personne_id is not None:
            personne_id_int = int(personne_id['_id']) + 1
        else:
            personne_id_int = 1
        data['_id'] = personne_id_int
        db.personne.insert_one(data)
        return jsonify({"message": "Personne ajoutée avec succès"}), 201
    except Exception as e:
        return jsonify({"message": f"Erreur lors de l'ajout de la personne : {str(e)}"}), 500


@personne_bp.route('/<string:personne_id>', methods=['PUT'])
def update_personne(personne_id):
    data = request.json

    if not data:
        return jsonify({"message": "Aucune donnée fournie pour la mise à jour de la personne"}), 400

    personne = db.personne.find_one({'_id': ObjectId(personne_id)})
    if not personne:
        return jsonify({"message": "Personne non trouvée"}), 404

    try:
        db.personne.update_one({'_id': ObjectId(personne_id)}, {'$set': data})
        return jsonify({"message": "Personne mise à jour avec succès"}), 200
    except Exception as e:
        return jsonify({"message": f"Erreur lors de la mise à jour de la personne : {str(e)}"}), 500




if __name__ == "__main__":
    #personnes = db.personne.find()
    #list_personne = list(personnes)
    #print(list_personne)
    pers = get_personne_list()
    print(pers)



#14:06:2004/feminin/debutant/Stacy/Gwen/True
#Stacy/Gwen/14:06:2004/feminin/debutant/True