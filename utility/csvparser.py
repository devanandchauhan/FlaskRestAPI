import csv
import json
import os
from models.productmodel import ProductModel
from models.transactionmodel import TransactionModel

def retriveCSV(dir_path):
    inputfiles = [file for file in os.listdir(dir_path) if file.endswith('.csv')]
    listData = []
    for file in inputfiles:
        filepath = os.path.join(dir_path, file)
        listData.append(filepath)
    return listData

BASE_PATH = 'raw/'

def productsFromCSV():
    products = []
    files = retriveCSV(BASE_PATH + 'Products/')
    for filepath in files:
        with open(filepath, "r") as csvfile:       
            reader = csv.DictReader(csvfile)        
            for row in reader:
                products.append(ProductModel(int(row['productId']), row['productName'], row['productManufacturingCity']))
    return products

def transactionsFromCSV():
    transactions = []
    files = retriveCSV(BASE_PATH + 'Transactions/')
    for filepath in files:
        with open(filepath, "r") as csvfile:       
            reader = csv.DictReader(csvfile)        
            for row in reader:
                transactions.append(TransactionModel(int(row['transactionId']), int(row['productId']), float(row['transactionAmount']), row['transactionDatetime']))    
    return transactions

def toJson(csvFile): 
    json_from_csv = json.dumps(toList(csvFile))
    return json_from_csv

def toList(csvFile): 
    file = open(csvFile, "r")
    dict_reader = csv.DictReader(file)
    return list(dict_reader)

def toProducts(csvFile): 
    file = open(csvFile, "r")
    dict_reader = csv.DictReader(file)
    products = []
    for row in dict_reader:
        products.append(ProductModel(int(row['productId']), row['productName'], row['productManufacturingCity']))
    return products    
