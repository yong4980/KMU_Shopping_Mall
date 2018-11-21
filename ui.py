from product import Product
from cart import Cart
import orderCtrl

class Ui:
    def __init__(self):
        self.cartList = []
        self.productList = []
        self.cart = Cart()
        self.orderUi = orderCtrl.OrderCtrl()
        
    def getCartInfo(self):
        temp_list = self.cart.getList()
        print("카트에 담겨있는 상품들은 ", temp_list,"있습니다.")
        total = 0
        for i in temp_list:
            total += i[1]
        print("카트에 담겨 있는 상품의 총 금액은 ", total, "원입니다.")
        ch = int(input('바로 구매하시려면 1, 계속 쇼핑하시려면 2를 입력해주세요.'))
        if ch == 1:
            result = self.orderUi.order(total)
            if result == 1 :
                self.cart.clearList()   
        else:
            pass
            
        
    def getProductInfo(self):
        category = int(input("옷은 1, 전자제품은 2, 욕실용품은 3을 입력해주세요"))
        things = 1
        if category == 1 :
            things = int(input("상의는 1, 하의는 1, 겉옷은 3을 입력해주세요"))
        elif category == 2:
            things = int(input("컴퓨터는 1, 핸드폰은 2, 냉장고는 3을 입력해주세요"))
        elif category == 3:
            things = int(input("샴푸는 1, 방향제는 2, 타월은 3을 입력해주세요"))
        product = Product(category, things)
        self.productList = product.getList()
        print(self.productList[0], '의 가격은 ', self.productList[1], '원입니다.')
        ch = int(input('쇼핑카트에 담으시려면 1, 바로 구매하시려면 2, 계속 쇼핑하시려면 3을 입력해주세요.'))
        if ch == 1:
            self.cart.addItemToList(self.productList)
        elif ch == 2:
            price = product.getPrice()
            self.orderUi.order(price)
            
        else:
            pass
            

    def logIn(self):
        #login = LoginSession()
        print("로그인 완료")
        

        

if __name__ == '__main__':
    ui = Ui()
    ui.logIn();
    while 1 :
        ch = int(input("계속 쇼핑하시려면 1, 장바구니를 보시려면 2, 쇼핑을 종료하시려면 3을 입력해주세요"))
        if ch == 1:
            ui.getProductInfo();
        elif ch == 2:
            ui.getCartInfo();
        elif ch == 3:
            print("쇼핑을 종료하겠습니다.")
            break;
        else :
            print("잘못 누르셨습니다.")
    
        
        
