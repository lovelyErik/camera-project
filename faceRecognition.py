import cv2 

img=cv2.imread("a.jpg")


white=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cat=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faceCascade=cat.detectMultiScale(white)

for (x,y,w,h) in faceCascade:
    cv2.rectangle(img,(x,y),(x+w,y+h),(136, 8, 8),2)
cv2.imshow("ok",img)
cv2.waitKey(0)