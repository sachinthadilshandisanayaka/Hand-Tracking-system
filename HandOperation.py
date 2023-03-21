import math
turnList = ["left", "right", "gohead"]
class handDetector():
    
    def __init__(self, lmList):
        self.lmList = lmList
        self.maxHandSize = 90
        self.minHandSize = 50
        
    def findhandIstoClose(self):
        # [0][2] - 0 means hand lankmark number, 2 means y axis
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
        #thumb = self.lmList[4][1] - self.lmList[2][1] 
        index = self.lmList[8][2] - self.lmList[5][2]
        middle = self.lmList[12][2] - self.lmList[9][2]
        ring = self.lmList[16][2] - self.lmList[13][2]
        pinky = self.lmList[20][2] - self.lmList[17][2]
        if(index > 0 and middle > 0 and ring > 0 and pinky > 0):
            return True
        else:
            return False
    
    def calculateAngle(self):
        fingerList = [4, 8, 12, 16]
        returnList = []
        for i in fingerList:
            a = math.sqrt((self.lmList[i][1] - self.lmList[i+4][1])**2 + (self.lmList[i][2] - self.lmList[i+4][2])**2)
            b = math.sqrt((self.lmList[0][1] - self.lmList[i+4][1])**2 + (self.lmList[0][2] - self.lmList[i+4][2])**2)
            c = math.sqrt((self.lmList[i][1] - self.lmList[0][1])**2 + (self.lmList[i][2] - self.lmList[0][2])**2)
            #s = (a+b+c)/2
            #ar = math.sqrt(s*(s-a)*(s-b)*(s-c))
            #d =(2*ar)/a
            
            # apply cosine rule here
            angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 100
            returnList.append(int(angle))
        return returnList
    
    def turningDirection(self):
        if((self.lmList[8][1] - self.lmList[0][1]) > 45):
           # print(self.lmList[8][1] - self.lmList[0][1])
            return turnList[1]
        elif((self.lmList[0][1] - self.lmList[16][1]) > 45):
            #print(self.lmList[0][1] - self.lmList[16][1])
            return turnList[0]
        else:
            return turnList[2]
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
            
        