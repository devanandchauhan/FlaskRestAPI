# Assignment

## Assignment Environment:
1.This application populates and provides retrieval features for transactions of a company.
2.Transaction information is coming as files (let’s say every 5 minutes) in a folder.
3.Another folder contains a file, which contains a reference data for products, against which thetransaction are happening.
4.This application is an in-memory application so no persistent storage is required. i.e. You canreload the already available data in the transaction folder upon start-up of the application.
5.A transaction record contains following attributes in a comma separated formata.transactionIdb.productIdc.transactionAmountd.transactionDatetime
6.The product reference data have following attributes in a CSV.a.productIdb.productNamec.productManufacturingCity
7.Reference data is static and transaction data is keep coming in real-time in their respectivefolders.

## Steps
- Before proceeding please install all the dependencies using the requirements.txt file in the root folder by using,
```pip install -r requirements.txt``` or ```python -m pip install -r requirements.txt```

- Start the app by using the command, ```python main.py```, if all the dependencies are installed properly you can see the app running at ```127.0.0.0/5000``` or ```localhost/5000``` in your browser as follows.**

## Screenshots

**CMD** <br>
<img src="./images/server.JPG" height="100" width="400">

**Home** <br>
<img src="./images/home.JPG" height="350" width="520">

**Product** <br>
<img src="./images/product.JPG" height="350" width="520">

**Transaction** <br>
<img src="./images/transaction.JPG" height="350" width="520">

**Transaction ID** <br>
<img src="./images/transactionid.JPG" height="350" width="520">

**Transaction Summary By Product** <br>
<img src="./images/transactionsummarybyproduct.JPG" height="350" width="520">

**Transaction Summary By Manufacture City** <br>
<img src="./images/transactionsummarybycity.JPG" height="350" width="520">

**Unit Tests**
<img src="./images/test.JPG" height="350" width="520">
