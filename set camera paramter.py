import cv2
cap=cv2.VideoCapture(0)
cap.set(3,1024)
cap.set(4,1024)
print(cap.get(3))
print(cap.get(4))
print(cap.isOpened)
while True:
    ret,frame=cap.read()
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1)&0XFF==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
