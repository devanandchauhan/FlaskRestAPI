from flask_restful import Resource
from flask import jsonify
from utility import csvparser
import json

class Transaction(Resource):
    def get(self):
        transactions = csvparser.transactionsFromCSV()
        json_string = json.dumps([ob.__dict__ for ob in transactions])
        final_dictionary = json.loads(json_string)
        return jsonify(final_dictionary)

    # def get(self):
    #     transactions = csvparser.toTransactions("Transaction_20180101101010.csv")
    #     print(transactions)
    #     return jsonify(transactions)
        



