from flask import Blueprint, jsonify, request
from pymongo import MongoClient
import json

class Connection:

    def __init__(self):
        self.connection = MongoClient(host="localhost", port=27017)
        self.database = self.connection.pingpongTournoi

    def get_database(self):
        return self.database