
class handDetector():
    
    def __init__(self, lmList):
        self.lmList = lmList
        
    def findhandIstoClose(self):
        print("hello")
        result =  self.lmList[0][2] - self.lmList[12][2]
        result2 = self.lmList[11][2] - self.lmList[12][2]
        if(result > 175 and result2 >= 0):
            return True
        else:
            return False
    def findhandIstoFar(self):
        result =  self.lmList[0][2] - self.lmList[12][2]
        result2 = self.lmList[11][2] - self.lmList[12][2]
        if(result < 100 and result2 >= 0):
            return True
        else:
            return False
            
        