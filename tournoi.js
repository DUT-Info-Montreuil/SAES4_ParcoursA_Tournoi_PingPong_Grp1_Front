
db = db.getSiblingDB("tournoi");

db.personne.drop();
db.match.drop();
db.lieu.drop();
db.tournoi.drop();
db.activité.drop();
db.equipement.drop();
db.personne.insertMany([
    {"_id": 1, "nom":"Cor","prenom":"Edgar", "anneeNaissance":  2000, "genre":"homme",
    "premierSecours": true},
    {"_id": 2, "nom":"Zinzin","prenom":"Guille", "anneeNaissance":  2004, "genre":"homme",
    "premierSecours": false, "niveau":"débutant"},
    {"_id": 3, "nom":"Cann","prenom":"Luna", "anneeNaissance":  2002, "genre":"femme",
    "premierSecours": true, "niveau":"débutant"},
    {"_id": 4, "nom":"Asagi","prenom":"Yasuo", "anneeNaissance":  2003, "genre":"homme",
    "premierSecours": true, "niveau":"débutant"}

]);

db.match.insertOne([
    {"_id": 1, "scoreJ1": 7, "scoreJ2":11, horaire:"9h00", "joueur1":2,"joueur2":3, "arbitre":4 }
]);
db.lieu.insertOne([
    {"_id": 1, "lieu":"LaDoumègue", "adresse" : "65 rue LaDoumègue", "capacite": 5000,
    "nbVestiaire": 20, "presenceVentilation": true} 
]);
db.tournoi.insertOne([
    {"_id": 1, "date": "01/06/2024", "niveauCompetition": "débutant",
    "catégorie": "mixte", "duréeMax": "4h", "listeJoueur" : [{"_id" : 2,"status":"joueur","points":0},{"_id" : 3,"status":"joueur","points":0},{"_id" : 4,"status":"joueur","points":0}],
    "idLieu": 1, "equipement": [{"nbBalles": 50, "nbTables": 8, "nbMarqueurs": 20, "nbFilets": 9,
    "nbRaquettes": 20}]}]);
