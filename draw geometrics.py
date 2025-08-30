import cv2
import numpy as np
img=np.zeros([512,512,3],np.uint8)
img=cv2.line(img,(0,0),(200,200),(255,255,255),5)
img=cv2.arrowedLine(img,(512,512),(400,400),(0,255,0),5)
img=cv2.rectangle(img,(512,0),(100,100),(0,255,0),5)
img=cv2.circle(img,(200,200),50,(255,255,0),7)
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,'hello',(100,100),font,4,(0,255,0))
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1) #draw ellipse




cv2.imshow('img',img)
#print(img)
cv2.waitKey(5000)