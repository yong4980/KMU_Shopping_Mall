import random as rd

class SecurityCtrl:
    NetworkSignal = rd.randint(1,100) 
    def __init__(self):
        print('보안프로그램 작동합니다.')
    
    def checkNetworkSignal(self):
        if NetWorkSignal >= 1:
            print('네트워크 접속이 올바릅니다.')
        else :
            print('다시 시도해주세요')
        
    def onSecurityProgram(self):
        print('보안점검이 완료되었습니다')
        return 1
        
    def checkOuterProgram(self):
        print('확장프로그램이 설치되어있습니다.')
        return 1
        
    def checkVirtualMachine(self):
        print('가상 프로그램의 실행을 확인하였습니다.')
        return 1
