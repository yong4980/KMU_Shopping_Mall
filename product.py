
class Product:
    def __init__(self,category, things):
        self.pro_id = things -1
        self.pro_kind = category -1
        self.pro_description = ''
        self.pro_list = [[['티셔츠', 10000], ['반바지', 20000], ['패딩', 50000]], [['노트북', 500], ['사과폰', 100], ['김치냉장고', 1000]], [['헤어샴푸', 10], ['포도향', 20], ['때밀이', 30]]]
        
    def getId(self):
        return self.pro_id
    def getName(self):
        return self.pro_list[self.pro_kind][self.pro_id][0]
    def getKind(self):
        return self.pro_kind
    def getDescription(self):
        return self.pro_description
    def getList(self):
        select_list = self.pro_list[self.pro_kind][self.pro_id]
        return select_list
    def getPrice(self):
        return self.pro_list[self.pro_kind][self.pro_id][1]

    def setId(self):
        self.pro_id = pro_id
    def setName(self):
        self.pro_name = pro_name
    def setKind(self):
        self.pro_kind = pro_kind
    def setDescription(self):
        self.pro_description = pro_description
    def setImage(self):
        self.pro_image = pro_image

    
