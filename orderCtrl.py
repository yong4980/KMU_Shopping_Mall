import cashPayment
import cardPayment

class OrderCtrl:
    def __init__(self):
        self.card = cardPayment.CardPayment()
        self.case = cashPayment.CashPayment()
        self.amount = 0
        
    def order(self, price):
        print(price, "원의 결제를 진행하겠습니다")
        self.amount = price
        ch = int(input("카드결제는 1, 무통장입금은 2를 입력해주세요"))
        if ch == 1:
            self.card.payment(self.amount)
        elif ch == 2:
            self.cash.payment(self.amount)
            
        
