import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    roi=frame[:1080,:1920]
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowblue=np.array([40,50,50])
    upblue=np.array([70,255,255])
    mask=cv2.inRange(hsv,lowblue,upblue)
    contour,Heirachy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    counter=0
    for cn in contour:
        area=cv2.contourArea(cn)
        if area<1000 or area>35000:
            continue
        ellipse=cv2.fitEllipse(cn)
        cv2.ellipse(roi,ellipse,(255,0,0),4)
        counter+=1
    cv2.putText(roi,str(counter),(10,150),cv2.FONT_HERSHEY_SIMPLEX,3,[0,0,255],3,cv2.LINE_AA)
    cv2.imshow('mask',roi)
    cv2.waitKey(1)