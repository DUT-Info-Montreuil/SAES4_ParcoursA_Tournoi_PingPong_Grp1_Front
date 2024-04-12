from flask import Blueprint, jsonify, request
from pymongo import MongoClient
import json
from bson import json_util, ObjectId  # Importez json_util depuis bson pour gérer la sérialisation des objets datetime
import Connection
from collections import Counter
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


@match_bp.route('/<int:match_id>', methods=['PUT'])
def update_match(match_id):
    data = request.json

    if not data:
        return jsonify({"message": "Aucune donnée fournie pour la mise à jour du match"}), 400

    match = db.match.find_one({'_id': match_id})
    if not match:
        return jsonify({"message": "Match non trouvé"}), 404

    try:
        db.match.update_one({'_id': match_id}, {'$set': data})
        return jsonify({"message": "Match mis à jour avec succès"}), 200
    except Exception as e:
        return jsonify({"message": f"Erreur lors de la mise à jour du match : {str(e)}"}), 500


@match_bp.route('/creationMatch',methods=['POST'])
def creation_match():
    tournoi_id = db.tournoi.find_one({}, {'_id': 1}, sort=[('_id', -1)])
    if tournoi_id is None:
        return jsonify({"message": "Pas de tournoi créer"})
    else :
        list_pers_tour_list = db.tournoi.find_one({'_id': tournoi_id['_id'], 'listePersonne.status': 'joueur'}, {'listePersonne.idPers': 1})
        list_details_tour = db.tournoi.find_one({'_id': tournoi_id['_id']}, {'equipement.nbTables': 1,'dureeMax': 1})
        tab_horaire = []
        if list_pers_tour_list is None:
            return jsonify({"message": "Liste de personne vide"}), 400
        else :
            verif_match = db.match.find_one({'idTournoi': tournoi_id['_id'], 'score1': { '$exists': True }, 'score2': { '$exists': True }})
            if verif_match is None:
                heure = 11
                minute = 30
                string_horaire = str(heure) + ":" + str(minute)
                for i in range(0, len(list_pers_tour_list['listePersonne']), 2):
                    idJ1 = list_pers_tour_list['listePersonne'][i]['idPers']
                    idJ2 = list_pers_tour_list['listePersonne'][i+1]['idPers']
                    verif_joueur = db.match.find_one({'joueur1': idJ1, 'idTournoi': tournoi_id['_id'], 'score1': { '$exists': False }, 'score2': { '$exists': False }})
                    verif_joueur2 = db.match.find_one({'joueur2': idJ2, 'idTournoi': tournoi_id['_id'],'score1': { '$exists': False }, 'score2': { '$exists': False }})

                    if verif_joueur is None or verif_joueur2 is None:

                        compt = 0;
                        if string_horaire in tab_horaire:
                            for hor in tab_horaire:
                                if hor == string_horaire:
                                    compt += 1
                            if(compt >= list_details_tour['equipement']['nbTables']):
                                if minute < 55 :
                                    minute = minute + 5
                                else :
                                    heure = heure + 1
                                    minute = 0
                        string_horaire = str(heure) + ":" + str(minute)
                        tab_horaire.append(string_horaire)
                        try:
                            match_id = db.match.find_one({}, {'_id': 1}, sort=[('_id', -1)])
                            if match_id is not None:
                                match_id_int = int(match_id['_id']) + 1
                            else:
                                match_id_int = 1
                            if(i + 1 < len(list_pers_tour_list['listePersonne'])):
                                data = {
                                    '_id': match_id_int,
                                    'horaire': string_horaire,
                                    'joueur1': list_pers_tour_list['listePersonne'][i]['idPers'],
                                    'joueur2': list_pers_tour_list['listePersonne'][i+1]['idPers'],
                                    'idTournoi': tournoi_id['_id']
                                }
                                db.match.insert_one(data)
                        except Exception as e:
                            return jsonify({"message": f"Erreur lors de l'ajout du match "}), 500
                return jsonify({"message": "Si il avait des matchs à ajouté, ils ont été ajouté avec succès"}), 200
            else :
                # Vérifier si tous les matchs de la phase précédente ont été joués
                nb_matchs_phase_precedente = db.match.count_documents({'idTournoi': tournoi_id['_id']})
                nb_matchs_joues = db.match.count_documents(
                    {'idTournoi': tournoi_id['_id'], 'score1': {'$exists': True}, 'score2': {'$exists': True}})

                if nb_matchs_phase_precedente != nb_matchs_joues:
                    return jsonify({"message": "Tous les matchs de la phase précédente n'ont pas été joués."}), 400

                # Récupérer tous les joueurs qui ont participé à la phase de tournoi en cours
                players = db.match.distinct("joueur1", {"idTournoi": tournoi_id['_id']})
                players += db.match.distinct("joueur2", {"idTournoi": tournoi_id['_id']})
                players = list(set(players))  # Supprimer les doublons

                # Compter le nombre de matchs gagnés par chaque joueur dans la phase de tournoi en cours
                wins_counter = Counter()

                for player in players:
                    wins_counter[player] = db.match.count_documents({
                        "$or": [{"joueur1": player, "score1": {"$gt": "score2"}},
                                {"joueur2": player, "score2": {"$gt": "score1"}}],
                        "score1": {"$exists": True},
                        "score2": {"$exists": True},
                        "idTournoi": tournoi_id['_id']
                    })

                maw_wins = max(wins_counter.values())

                remaining_players = [player for player, wins in wins_counter.items() if wins == maw_wins]

                if len(remaining_players) < 2:
                    j = db.personne.find_one({'_id': remaining_players[0]}, {'nom': 1, 'prenom': 1})
                    return jsonify({"message": f"Le vainqueur du tournoi est {j['prenom']} {j['nom']}."}), 200

                # Planifier les matchs pour la phase suivante du tournoi
                heure = 9
                minute = 0

                horraire = db.match.find({"idTournoi": tournoi_id['_id'] }, {'horaire': 1})
                list_hor = list(horraire)
                for i in range(len(list_hor)):
                    valeur = list_hor[i]['horaire']
                    heure2, minute2 = map(int, valeur.split(':'))
                    if heure2 > heure or (heure == heure2 and minute2 > minute):
                        heure = heure2
                        minute = minute2

                if minute < 55 :
                    minute =+ 5
                else :
                    heure += 1
                    minute = 0

                tab_horaire = []

                for i in range(0, len(remaining_players), 2):
                    compt = 0
                    string_horaire = str(heure) + ":" + str(minute)

                    if string_horaire in tab_horaire:
                        for hor in tab_horaire:
                            if hor == string_horaire:
                                compt += 1
                        if compt >= list_details_tour['equipement']['nbTables']:
                            if minute < 55:
                                minute += 5
                            else:
                                heure += 1
                                minute = 0

                    string_horaire = str(heure) + ":" + str(minute)
                    tab_horaire.append(string_horaire)

                    try:
                        match_id = db.match.find_one({}, {'_id': 1}, sort=[('_id', -1)])
                        if match_id is not None:
                            match_id_int = int(match_id['_id']) + 1
                        else:
                            match_id_int = 1

                        if i + 1 < len(remaining_players):
                            data = {
                                '_id': match_id_int,
                                'horaire': string_horaire,
                                'joueur1': remaining_players[i],
                                'joueur2': remaining_players[i + 1],
                                'idTournoi': tournoi_id['_id']
                            }
                            db.match.insert_one(data)
                    except Exception as e:
                        return jsonify({"message": f"Erreur lors de l'ajout du match : {str(e)}"}), 500

                return jsonify(
                    {"message": "Les matchs pour la phase suivante du tournoi ont été planifiés avec succès."}), 200
