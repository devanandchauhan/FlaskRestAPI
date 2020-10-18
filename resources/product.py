from flask_restful import Resource
from flask import jsonify
from utility import csvparser
import json

class Product(Resource):
     
    def get(self):
        products = csvparser.productsFromCSV()
        json_string = json.dumps([ob.__dict__ for ob in products])
        final_dictionary = json.loads(json_string)
        return jsonify(final_dictionary)

    # def get(self):
    #     productJSON=csvparser.toJson("ProductReference.csv")
    #     #print(productJSON)
    #     return productJSON

