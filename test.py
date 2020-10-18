import requests

def test_route():
	response = requests.get('http://127.0.0.1:5000/')
	assert response.status_code == 200
	print(response)

def test_transactionsummarybymanufacturingcity():
	response = requests.get('http://127.0.0.1:5000/assignment/transactionsummarybymanufacturingcity/1')
	assert response.status_code == 200
	print(response)

def test_transactionsummarybyproducts():
	response = requests.get('http://127.0.0.1:5000/assignment/transactionsummarybyproducts/1')
	assert response.status_code == 200
	print(response)

def test_product():
	response = requests.get('http://127.0.0.1:5000/assignment/product')
	assert response.status_code == 200
	print(response)

def test_transaction():
	response = requests.get('http://127.0.0.1:5000/assignment/transaction')
	assert response.status_code == 200
	print(response)



