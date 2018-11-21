import payment
import cashAccount

class CashPayment(payment.Payment): #상속
    def __init__(self):
        super().__init__()
        self.account = cashAccount.CashAccount()
        self.accountNum = ''
        self.accountBank = ''
        
    def requestPayment(self, price): #Overriding
        self.amount = price
        print("무통장 결제를 진행합니다.", self.amount)
        self.accountBank = input("은행명을 입력해주세요 >> ")
        self.accountNum = input("계좌번호를 입력해주세요 >> ")
        result = self.account.checkAccount(self.accountBank, self.accountNum)
        if result == 1:
            print('구매가 정상적으로 되었습니다. 감사합니다.')
        return result

