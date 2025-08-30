import cv2,datetime
cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.isOpened)
while(True):
    ret,frame=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_COMPLEX
        text='width'+str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))+'hight'+str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        datet=str(datetime.datetime.now())
        frame=cv2.putText(frame,text,(10,50),font,1,(0,0,255),5)
        frame=cv2.putText(frame,datet,(10,50),font,1,(0,0,0),5)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1)&0XFF==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
