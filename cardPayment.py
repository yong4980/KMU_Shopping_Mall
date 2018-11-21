
class CardPayment:
    def __init__(self):
        self.amount = 0
        
    def payment(self, price):
        self.amount = price
        print("card", self.amount)
