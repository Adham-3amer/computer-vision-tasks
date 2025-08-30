import cv2
import numpy as np
def click_event(event,x,y,fligs,parameter):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),13,(255,0,0),-1)
        points.append((x,y))
        if len(points)>2:
            cv2.line(img,points[-1],points[-2],(0,255,0),5)
        cv2.imshow('img',img)
img=np.zeros((512,512,3),np.uint8)
points=[]
cv2.namedWindow("img")
cv2.setMouseCallback('img',click_event)
while True:
    cv2.imshow("img", img)
    if cv2.waitKey(20) & 0xFF == 27: 
        break

cv2.destroyAllWindows()