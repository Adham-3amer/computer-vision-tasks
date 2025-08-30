import cv2, numpy as np
def nothing(x):
    print(x)
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('img')
cv2.createTrackbar('B','img',0,255,nothing)
cv2.createTrackbar('G','img',0,255,nothing)
cv2.createTrackbar('R','img',0,255,nothing)
switch='0:off\n 1:on'
cv2.createTrackbar('switch','img',0,1,nothing)
while(1):
    cv2.imshow('img',img)
    k=cv2.waitKey(1)
    if k==27:
        break
    b=cv2.getTrackbarPos('B','img')
    g=cv2.getTrackbarPos('G','img')
    r=cv2.getTrackbarPos('R','img')
    switch=cv2.getTrackbarPos('switch','img')
    if switch==0:
        img[:]=0
    else:
        img[:]=[b,g,r]
cv2.destroyAllWindows()