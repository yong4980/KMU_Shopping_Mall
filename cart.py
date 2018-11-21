class Cart():
    def __init__(self): 
        self.cartList = [] 
    
    def getList(self):
        return self.cartList
        
    def addItemToList(self, item):
        self.cartList.append(item)
        
    def removeItemToList(self):
        Shop_list.remove(item)
        print(Shop_list)
