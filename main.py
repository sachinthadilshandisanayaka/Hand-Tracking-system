import cv2
import time
import os
import HandTrackingModule as htm

top, right, bottom, left = 10, 350, 225, 590

cap = cv2.VideoCapture(0)
#cap.set(3, wCam)
#cap.set(4, hCam)

detector = htm.handDetector(detectionCon=0.75)

#tipIds = [4, 8, 12, 16, 20]

while True:
    ret, img = cap.read()
    img=cv2.flip(img,1)
    img=cv2.rectangle(img, (left, top), (right, bottom), (0,255,0), 2)
    roi = img[top:bottom, right:left]
    roi = detector.findHands(roi)
    lmList = detector.findPosition(roi, draw=False)

    cv2.imshow("Image", img)
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #print(range(defects.shape[0]))
        break

cap.release()
cv2.destroyAllWindows()