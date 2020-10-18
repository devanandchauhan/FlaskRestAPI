from flask_restful import Resource
from flask import jsonify
from utility import csvparser

class TransactionFilter(Resource):
    def get(self,transaction_id):
        print("transaction_id:" +str(transaction_id))
    
        transactions = csvparser.transactionsFromCSV()
        products = csvparser.productsFromCSV()

        for tx in transactions:
            if tx.transactionId == transaction_id:
                for pd in products:
                    if pd.productId == tx.productId:
                        return jsonify(
                                transactionId = tx.transactionId,
                                productName = pd.productName,
                                transactionAmount = tx.transactionAmount,
                                transactionDatetime = tx.transactionAmount)

        return "No Data found!!!"