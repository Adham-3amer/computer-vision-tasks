import cv2,numpy
events=[i for i in dir(cv2) if "EVENT" in i]
print(events)
def click_events(events,x,y,flags,parameter):
    if events==cv2.EVENT_LBUTTONDOWN:
        print(x,'',y)
        font=cv2.FONT_HERSHEY_COMPLEX
        str1=str(x)+str(y)
        cv2.putText(img, str1, (x, y), font, 0.5, (0, 0, 0), 2)
        cv2.imshow('img',img)
    if events==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        str2=str(blue)+','+str(green)+','+str(red)
        font=cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img, str2, (x, y), font, 0.5, (0, 0, 0), 2)
        cv2.imshow('img',img)
    
img = cv2.imread('22.jpeg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_events)

cv2.waitKey(0)
cv2.destroyAllWindows()