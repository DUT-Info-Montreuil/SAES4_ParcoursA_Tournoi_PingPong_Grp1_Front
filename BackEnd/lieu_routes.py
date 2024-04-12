from flask import Blueprint, jsonify, request
from pymongo import MongoClient
import json
from bson import json_util # Importez json_util depuis bson pour gérer la sérialisation des objets datetime
import Connection

lieu_bp = Blueprint('lieus', __name__)

connection = Connection.Connection()
db = connection.get_database()

@lieu_bp.route('/', methods=['GET'])
def get_lieu_list():
    lieus = db.lieu.find()
    liste_lieu = list(lieus)
    liste_lieus_json = json.dumps(liste_lieu, default=json_util.default)  # Utilisez json_util.default pour gérer la sérialisation des objets datetime
    return liste_lieus_json


@lieu_bp.route('/<int:lieu_id>', methods=['GET'])
def get_lieu_id(lieu_id):
    lieu = db.lieu.find_one({'_id': lieu_id})
    if lieu:
        return jsonify(lieu)
    else:
        return jsonify({"message": "Lieu non trouvée"}), 404  # Renvoie une réponse JSON avec un code de statut 404


@lieu_bp.route('/<string:nom>/<string:adresse>/<int:capacite>/<int:nbVestiaire>/<string:presenceVentilation>', methods=['POST'])
def add_lieu(nom, adresse, capacite, nbVestiaire, presenceVentilation):
    lieu_id = db.lieu.find_one({}, {'_id': 1}, sort=[('_id', -1)])
    if lieu_id is not None:
        lieu_id_int = int(lieu_id['_id']) + 1
    else:
        lieu_id_int = 1
    db.lieu.insert_one(
        {"_id": lieu_id_int, "nom": nom, "adresse": adresse, "capacite": capacite, "nbVestiaire": nbVestiaire,
         "presenceVentilation": presenceVentilation,}
    )
    return jsonify({"message": "Lieu ajoutée avec succès"}), 200


@lieu_bp.route('/', methods=['POST'])
def add2_lieu():
    data = request.json  # Récupérer les données JSON envoyées dans la requête

    # Valider les données
    required_fields = ['nom', 'adresse', 'capacite', 'nbVestiaire', 'presenceVentilation']
    if not all(field in data for field in required_fields):
        return jsonify({"message": "Certains champs requis sont manquants"}), 400

    # Insérer le lieu dans la base de données
    try:
        lieu_id = db.lieu.find_one({}, {'_id': 1}, sort=[('_id', -1)])
        if lieu_id is not None:
            lieu_id_int = int(lieu_id['_id']) + 1
        else:
            lieu_id_int = 1
        data['_id'] = lieu_id_int
        db.lieu.insert_one(data)
        return jsonify({"message": "Lieu ajouté avec succès"}), 201
    except Exception as e:
        return jsonify({"message": f"Erreur lors de l'ajout du lieu : {str(e)}"}), 500


@lieu_bp.route('/<int:lieu_id>', methods=['PUT'])
def update_lieu(lieu_id):
    data = request.json

    if not data:
        return jsonify({"message": "Aucune donnée fournie pour la mise à jour du lieu"}), 400

    lieu = db.lieu.find_one({'_id': lieu_id})
    if not lieu:
        return jsonify({"message": "Lieu non trouvé"}), 404

    try:
        db.lieu.update_one({'_id': lieu_id}, {'$set': data})
        return jsonify({"message": "Lieu mis à jour avec succès"}), 200
    except Exception as e:
        return jsonify({"message": f"Erreur lors de la mise à jour du lieu : {str(e)}"}), 500
