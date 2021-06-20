
class handDetector():
    
    def __init__(self, lmList):
        self.lmList = lmList
        self.maxHandSize = 90
        self.minHandSize = 50
        
    def findhandIstoClose(self):
        result =  self.lmList[0][2] - self.lmList[9][2]
        #print(result)
        if(result > self.maxHandSize):
            return True
        else:
            return False
    def findhandIstoFar(self):
        result =  self.lmList[0][2] - self.lmList[9][2]
    
        if(result < self.minHandSize):
            return True
        else:
            return False
    def findStop(self):
        thumb = self.lmList[4][1] - self.lmList[2][1] 
        index = self.lmList[8][2] - self.lmList[5][2]
        middle = self.lmList[12][2] - self.lmList[9][2]
        ring = self.lmList[16][2] - self.lmList[13][2]
        pinky = self.lmList[20][2] - self.lmList[17][2]
        if(thumb > 0 and index > 0 and middle > 0 and ring > 0 and pinky > 0):
            return True
        else:
            return False    
            
        