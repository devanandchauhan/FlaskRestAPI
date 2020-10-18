from flask import Flask
from flask_restful import Api
from resources.transaction import Transaction
from resources.transactionfilter import TransactionFilter
from resources.summarybyproducts import SummaryByProducts
from resources.summarybymanufacturingcity import SummaryByManufacturingCity
from resources.product import Product

app = Flask(__name__)
api = Api(app)

api.add_resource(Transaction, '/assignment/transaction')
api.add_resource(TransactionFilter, '/assignment/transaction/<int:transaction_id>')
api.add_resource(SummaryByProducts, '/assignment/transactionsummarybyproducts/<int:last_n_days>')
api.add_resource(SummaryByManufacturingCity, "/assignment/transactionsummarybymanufacturingcity/<int:last_n_days>")
api.add_resource(Product, '/assignment/product')

@app.route("/")
def home(): 
    return "Welcome to Rest API Page!!!"

if __name__ == "__main__":
    app.run(debug=True)