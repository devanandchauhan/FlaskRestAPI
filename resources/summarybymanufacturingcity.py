from flask_restful import Resource
from flask import jsonify
from datetime import datetime, timedelta
from utility import csvparser

class SummaryByManufacturingCity(Resource):
    def get(self,last_n_days):
        #print("numberOfDays" + str(last_n_days))
        transactions = csvparser.transactionsFromCSV()

        max_tx_date = lastRecentDate(transactions)
        #print(max_tx_date)
        
        date_N_days_ago = max_tx_date - timedelta(days = last_n_days)
        #print(date_N_days_ago)

        prod = []
        for tx in transactions:
            if tx.txDate > date_N_days_ago:
                if updateProduct(prod, tx.productId, tx.transactionAmount) == False:
                    prod.append({"cityName" : cityName(tx.productId), "totalAmount" : tx.transactionAmount})
                    print(prod)

        return jsonify(summary = prod)

def lastRecentDate(transactions):
    if len(transactions) > 0:
        last_recent_date = transactions[0].txDate
        for tx in transactions:
            if tx.txDate > last_recent_date:
                last_recent_date = tx.txDate
        return last_recent_date

def updateProduct(products, productId, amount):
    for row in products:
        if row["cityName"] == cityName(productId):
            row["totalAmount"] += amount
            return True
    return False

def cityName(productId):
    for obj in csvparser.productsFromCSV():
        if obj.productId == productId:
            return obj.productManufacturingCity