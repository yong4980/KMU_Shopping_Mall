import security

class LoginSessionCtrl:
    id1 = 'user1'
    id2 = 'user2'
    id3 = 'user3'
    pw1 = 123
    pw2 = 456
    pw3 = 789
    
    login_dic = {id1:pw1, id2:pw2, id3:pw3}
    
    def __init__(self):
        self.security = security.SecurityCtrl()
        self.security.onSecurityProgram()
        self.checkid = 0
        self.checkpw = 0
        
        
    def checkID(self):
        self.input_id = input("아이디를 입력해주세요 >> ")
        if self.input_id in self.login_dic.keys():
            self.checkid = 1
        else:
            self.checkid = 0
        
    def checkPW(self):
        self.input_pw = input("비밀번호를 입력해주세요 >> ")
        if self.input_id in self.login_dic.keys():
            if self.login_dic[self.input_id] == self.input_pw:
                self.checkpw = 1
            else :
                self.checkpw = 0
            
    def isSafe(self):
        if self.checkid == True and self.checkpw == True:
            print('로그인 되었습니다.')
            return 1
        else:
            print('아이디 또는 비밀번호가 잘못되었습니다.')
            return 0

    def makeID(self):
        self.input_id = input("아이디를 입력해주세요 >> ")
        self.input_pw = input("비밀번호를 입력해주세요 >> ")
        self.login_dic[self.input_id] = self.input_pw
        print('회원가입 되셨습니다.')
        
