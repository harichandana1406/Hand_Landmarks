import cv2
import time
#import os
import hand_tracking_module as htm


cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


detector=htm.handDetector(detectionCon=0.75)
tipIds=[4,8,12,16,20]
while True:
    success,img=cap.read()
    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)
    #print(lmList)
    if len(lmList) !=0:
        fingers=[]

        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1,5):  #y axis
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
                
        totalFingers=fingers.count(1)
        if(totalFingers==2):
            cv2.putText(img,"Next",(45,375),cv2.FONT_HERSHEY_PLAIN,5,(255,0,0),10)
        elif(totalFingers==1):
            cv2.putText(img,"Remove",(45,375),cv2.FONT_HERSHEY_PLAIN,5,(255,0,0),10)
        elif(totalFingers==0):
            cv2.putText(img,"Done",(45,375),cv2.FONT_HERSHEY_PLAIN,5,(255,0,0),10)
        elif(totalFingers==3):
            cv2.putText(img,"Select",(45,375),cv2.FONT_HERSHEY_PLAIN,5,(255,0,0),10)
        elif(totalFingers==4):
            cv2.putText(img,"Modify",(45,375),cv2.FONT_HERSHEY_PLAIN,5,(255,0,0),10)
        elif(totalFingers==5):
            cv2.putText(img,"Back",(45,375),cv2.FONT_HERSHEY_PLAIN,5,(255,0,0),10)
        else:
            cv2.putText(img,str(totalFingers),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),10)



       # cv2.rectangle(img,(20,225),(170,425),(0,255,0),cv2.FILLED)
        
    

    #cv2.putText(img,f'FPS: {int(fps)}',(400,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("MediaPipe Hands",img)
    cv2.waitKey(1)

    # If the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup the camera and close any open windows
cap.release()
cv2.destroyAllWindows()

