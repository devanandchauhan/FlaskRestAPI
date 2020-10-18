from datetime import datetime

class TransactionModel:
    def __init__(self,transactionId,productId,transAmount,transDatetime):
        self.transactionId = transactionId
        self.productId = productId
        self.transactionAmount = transAmount
        self.transactionDatetime = transDatetime

    @property
    def txDate(self):
        return datetime.strptime(self.transactionDatetime, '%Y-%m-%d %H:%M:%S')