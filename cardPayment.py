import payment
import creditCard

class CardPayment(payment.Payment): #상속
    def __init__(self):
        super().__init__()
        self.account = creditCard.CreditCard()
        self.cardBank = ''
        self.cardNum = ''
        
    def requestPayment(self, price): #Overriding
        self.amount = price
        print(self.amount, "원의 카드 결제를 진행합니다.")
        self.accountBank = input("카드 회사를 입력해주세요 >> ")
        self.accountNum = input("카드번호를 입력해주세요 >> ")
        result = self.account.checkCard(self.accountBank,self.accountNum)
        if result == 1:
            print('구매가 정상적으로 되었습니다. 감사합니다.')
        return result
    
    
        
