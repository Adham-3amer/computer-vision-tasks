import cv2, numpy as np
img1=np.zeros((400,400,3),np.uint8)
cv2.rectangle(img1,(0,0),(100,100),(255,255,255),-1)
img2 = np.ones((400,400,3), np.uint8) * 255
cv2.rectangle(img2,(200,0),(300,400),(0,0,0),-1)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
#bitand=cv2.bitwise_and(img2,img1)
#cv2.imshow('bitand',bitand)
#bitor=cv2.bitwise_or(img2,img1)
#cv2.imshow('bitor',bitor)
bitxor=cv2.bitwise_xor(img2,img1)
cv2.imshow('bitxor',bitxor)


cv2.waitKey(0)
cv2.destroyAllWindows()