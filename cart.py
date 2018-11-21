class Cart():
    def __init__(self): 
        self.cartList = [] 
    
    def getList(self):
        return self.cartList
        
    def addItemToList(self, item):
        self.cartList.append(item)
        
    def clearList(self):
        self.cartList.clear()
        
