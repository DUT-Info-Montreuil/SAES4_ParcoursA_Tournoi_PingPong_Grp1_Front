from flask import Blueprint, jsonify, request
from pymongo import MongoClient
import json
from bson import json_util  # Importez json_util depuis bson pour gérer la sérialisation des objets datetime
import Connection

tournoi_bp = Blueprint('tournois', __name__)

connection = Connection.Connection()
db = connection.get_database()


@tournoi_bp.route('/', methods=['GET'])
def get_tournoi_list():
    tournois = db.tournoi.find()
    liste_tournois = list(tournois)
    liste_tournois_json = json.dumps(liste_tournois,
    default=json_util.default)  # Utilisez json_util.default pour gérer la sérialisation des objets datetime
    return liste_tournois_json


@tournoi_bp.route('/<int:tournoi_id>', methods=['GET'])
def get_tournoi_id(tournoi_id):
    tournoi = db.tournoi.find_one({'_id': tournoi_id})
    if tournoi:
        return jsonify(tournoi)
    else:
        return jsonify({"message": "Tournoi non trouvée"}), 404  # Renvoie une réponse JSON avec un code de statut 404


@tournoi_bp.route('/', methods=['POST'])
def add_tournoi():
    data = request.json

    required_fields = ['date', 'niveauCompet', 'categorie', 'dureeMax', 'listePersonne', 'idLieu', 'equipement']
    if not all(field in data for field in required_fields):
        return jsonify({"message": "Certains champs requis sont manquants"}), 400

    try:
        db.tournoi.insert_one(data)
        return jsonify({"message": "Tournoi ajouté avec succès"}), 201
    except Exception as e:
        return jsonify({"message": f"Erreur lors de l'ajout du tournoi : {str(e)}"}), 500


"""
@tournoi_bp.route('/<string:date>/<string:niveauCompet>/<string:categorie>/<string:dureeMax>/<', methods=['POST'])
def add_tournoi():

"""


@tournoi_bp.route('/<int:tournoi_id>', methods=['PUT'])
def update_tournoi(tournoi_id):
    data = request.json

    if not data:
        return jsonify({"message": "Aucune donnée fournie pour la mise à jour du tournoi"}), 400

    tournoi = db.tournoi.find_one({'_id': tournoi_id})
    if not tournoi:
        return jsonify({"message": "Tournoi non trouvé"}), 404

    try:
        db.tournoi.update_one({'_id': tournoi_id}, {'$set': data})
        return jsonify({"message": "Tournoi mis à jour avec succès"}), 200
    except Exception as e:
        return jsonify({"message": f"Erreur lors de la mise à jour du tournoi : {str(e)}"}), 500


if __name__ == '__main__':
    tournois = db.personne.find()
    liste_tournois = list(tournois)
    print(liste_tournois)
    print(liste_tournois[0])
    print(type(liste_tournois))
    """
    liste = get_tournoi_list()
    print(liste)
    print(liste[1])
    print(type(liste))
    """