import cv2
import HandTrackingModule as htm
import HandOperation as op

top, right, bottom, left = 10, 300, 250, 590
maximemangle = [60, 15, 13, 20]
turnList = ["left", "right", "gohead"]

cap = cv2.VideoCapture(0)

detector = htm.handDetector(detectionCon=1)

font = cv2.FONT_HERSHEY_SIMPLEX
result = 0
while True:
    ret, img = cap.read()
    # flipping the image horizontally (around the y-axis) 
    img = cv2.flip(img,1)
    img = cv2.rectangle(img, (left, top), (right, bottom), (0,255,0), 2)
    roi = img[top:bottom, right:left]
    
    roi = detector.findHands(roi)
    
    lmList = detector.findPosition(roi, draw=False)
    #print(lmList)
    
    if len(lmList) != 0:
        operation = op.handDetector(lmList)
        
        fingers = []
        #check hand distance
        isToClose = operation.findhandIstoClose()
        if(isToClose == True):
            cv2.putText(img,'Hand is too close',(0,50), font, 1, (0,0,255), 2, cv2.LINE_AA)
        isSoFar = operation.findhandIstoFar()
        if( isSoFar == True):
            cv2.putText(img,'Get closer',(0,50), font, 1, (0,0,255), 2, cv2.LINE_AA)
        isStop = operation.findStop()
        if( isStop == True):
            cv2.putText(img,'Stop',(0,80), font, 1, (0,0,255), 2, cv2.LINE_AA)
        else:
            angleResult = operation.calculateAngle()
            #print(angleResult)
            if(angleResult[0] > maximemangle[0] and angleResult[1] > maximemangle[1] 
              # and angleResult[2] > maximemangle[2] 
               and angleResult[3] > maximemangle[3]):
                cv2.putText(img,'Reverse',(0,80), font, 1, (0,0,255), 2, cv2.LINE_AA)
            else:
                if(angleResult[0] > maximemangle[0] and angleResult[1] < maximemangle[1] 
               and angleResult[2] < maximemangle[2] and angleResult[3] < maximemangle[3]):
                    cv2.putText(img,'Slow down',(0,80), font, 1, (0,0,255), 2, cv2.LINE_AA)
                    direction =  operation.turningDirection()
                    if(direction == turnList[0]):
                        cv2.putText(img,'left',(0,110), font, 1, (0,0,255), 2, cv2.LINE_AA)
                    elif(direction == turnList[1]):
                        cv2.putText(img,'Right',(0,110), font, 1, (0,0,255), 2, cv2.LINE_AA)
                    elif(direction == turnList[2]):
                        cv2.putText(img,'Go head',(0,110), font, 1, (0,0,255), 2, cv2.LINE_AA)
                else:
                    direction =  operation.turningDirection()
                    if(direction == turnList[0]):
                        cv2.putText(img,'left',(0,80), font, 1, (0,0,255), 2, cv2.LINE_AA)
                    elif(direction == turnList[1]):
                        cv2.putText(img,'Right',(0,80), font, 1, (0,0,255), 2, cv2.LINE_AA)
                    elif(direction == turnList[2]):
                        cv2.putText(img,'Go head',(0,80), font, 1, (0,0,255), 2, cv2.LINE_AA)
            #elif(angleResult[0] < maximemangle[0] and angleResult[1] < maximemangle[1] 
             #  and angleResult[2] < maximemangle[2] and angleResult[3] < maximemangle[3]):
              #  cv2.putText(img,'Go head',(0,80), font, 1, (0,0,255), 2, cv2.LINE_AA)
            
            #elif():
                
                
            
            #for i in range(4):
             #    if( angleResult[i] > maximemangle[i]):
              #      print(str(i) + ' angle ok')
                
                
            #cv2.putText(img,'Go head',(0,80), font, 1, (0,0,255), 2, cv2.LINE_AA)
        
         
    cv2.imshow("Image", img)
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #print(range(defects.shape[0]))
        break

cap.release()
cv2.destroyAllWindows()





