import cv2, numpy as np
def nothing(x):
    print(x)
cv2.namedWindow('tracking')
cv2.createTrackbar('lh','tracking',0,255,nothing)
cv2.createTrackbar('ls','tracking',0,255,nothing)
cv2.createTrackbar('lv','tracking',0,255,nothing)
cv2.createTrackbar('uh','tracking',255,255,nothing)
cv2.createTrackbar('us','tracking',255,255,nothing)
cv2.createTrackbar('uv','tracking',255,255,nothing)
while(1):
    img=cv2.imread('x.png')
    img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lh=cv2.getTrackbarPos('lh','tracking')
    ls=cv2.getTrackbarPos('ls','tracking')
    lv=cv2.getTrackbarPos('lv','tracking')
    uh=cv2.getTrackbarPos('uh','tracking')
    us=cv2.getTrackbarPos('us','tracking')
    uv=cv2.getTrackbarPos('uv','tracking')
    l_b=np.array([lh,ls,lv])
    u_b = np.array([uh, us, uv])
    mask=cv2.inRange(img_hsv,l_b,u_b)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('res',res)
    cv2.imshow('mask',mask)
    cv2.imshow('img',img)
    key = cv2.waitKey(1)         

    if key == 27:        

        break       
cv2.destroyAllWindows() #colse window

