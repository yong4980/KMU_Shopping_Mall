
class CashPayment:
    def __init__(self):
        self.amount = 0
        
    def payment(self, price):
        self.amount = price
        print("cash", self.amount)
