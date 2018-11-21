import payment
import creditCard

class CardPayment(payment.Payment): #상속
    def __init__(self):
        super().__init__()
        self.account = creditCard.CreditCard()
        
    def requestPayment(self, price): #overriding
        self.amount = price
        print("카드 결제를 진행합니다.", self.amount)
    
    
        
