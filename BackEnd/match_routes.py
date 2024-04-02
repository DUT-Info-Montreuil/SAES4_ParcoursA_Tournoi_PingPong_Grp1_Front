from flask import Blueprint, jsonify, request
from pymongo import MongoClient
import json
from bson import json_util  # Importez json_util depuis bson pour gérer la sérialisation des objets datetime
import Connection
match_bp = Blueprint('matchs', __name__)

connection = Connection.Connection()
db = connection.get_database()


@match_bp.route('/', methods=['GET'])
def get_match_list():
    matchs = db.match.find()
    liste_match = list(matchs)
    liste_matchs_json = json.dumps(liste_match, default=json_util.default)  # Utilisez json_util.default pour gérer la sérialisation des objets datetime
    return liste_matchs_json

@match_bp.route('/<int:match_id>', methods=['GET'])
def get_match_id(match_id):
    match = db.match.find_one({'_id': match_id})
    if match:
        return jsonify(match)
    else:
        return jsonify({"message": "Match non trouvée"}), 404  # Renvoie une réponse JSON avec un code de statut 404


@match_bp.route('/<int:score1>/<int:score2>/<string:horaire>/<int:id_joueur1>/<int:id_joueur2>', methods=['POST'])
def add_match(score1, score2, horaire, id_joueur1, id_joueur2):
    match_id = db.match.find_one({}, {'_id': 1}, sort=[('_id', -1)])
    if match_id is not None:
        match_id_int = int(match_id['_id']) + 1
    else:
        match_id_int = 1
    db.match.insert_one(
        {"_id": match_id_int, "score1": score1, "score2": score2, "horaire": horaire, "joueur1": id_joueur1,
         "joueur2": id_joueur2,}
    )
    return jsonify({"message": "Match ajoutée avec succès"}), 200


@match_bp.route('/', methods=['POST'])
def add2_match():
    data = request.json

    required_fields = ['score1', 'score2', 'horaire', 'joueur1', 'joueur2']
    if not all(field in data for field in required_fields):
        return jsonify({"message": "Certains champs requis sont manquants"}), 400

    try:
        match_id = db.match.find_one({}, {'_id': 1}, sort=[('_id', -1)])
        if match_id is not None:
            match_id_int = int(match_id['_id']) + 1
        else:
            match_id_int = 1
        data['_id'] = match_id_int
        db.match.insert_one(data)
        return jsonify({"message": "Match ajouté avec succès"}), 201
    except Exception as e:
        return jsonify({"message": f"Erreur lors de l'ajout du match : {str(e)}"}), 500


@match_bp.route('/<string:match_id>', methods=['PUT'])
def update_match(match_id):
    data = request.json

    if not data:
        return jsonify({"message": "Aucune donnée fournie pour la mise à jour du match"}), 400

    match = db.match.find_one({'_id': ObjectId(match_id)})
    if not match:
        return jsonify({"message": "Match non trouvé"}), 404

    try:
        db.match.update_one({'_id': ObjectId(match_id)}, {'$set': data})
        return jsonify({"message": "Match mis à jour avec succès"}), 200
    except Exception as e:
        return jsonify({"message": f"Erreur lors de la mise à jour du match : {str(e)}"}), 500