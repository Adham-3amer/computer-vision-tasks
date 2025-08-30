import cv2
img=cv2.imread('1.jpeg',0)
cv2.imshow('img',img)
print(img)
k=cv2.waitKey(0)
if k=='27':
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('adham.jpg',img)
    cv2.destroyAllWindows()
cv2.destroyAllWindows()