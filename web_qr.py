import cv2
import pyzbar.pyzbar as pyzbar
import numpy as np

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

while True:
    _,frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    cv2.rectangle(frame,(450,380),(150,100),(0,0,0), 3)
    # cv2.rectangle(frame,(430,350),(170,140),(0,0,0),1)
    cv2.rectangle(frame,(440,360),(160,125),(0,0,0),2)
    for obj in decodedObjects:
        data = str(obj.data).strip("b'")
        data2 = data.strip("''")
        cv2.putText(frame,data2.strip('""'),(20,40),font,1,(255,0,0),1)
        print(data2.strip('""'))
        print(_)
    cv2.imshow("Frame",frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
