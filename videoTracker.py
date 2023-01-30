import cv2 

video=cv2.VideoCapture("bb3.mp4")
tracker=cv2.TrackerCSRT_create()
returned,img=video.read()
boundingBox=cv2.selectROI("tracking",img,False)
tracker.init(img,boundingBox)

print(boundingBox)

def drawbox(img,box):
    x,y,w,h=int(box[0]), int(box[1]), int(box[2]), int(box[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,0),3,1)
    cv2.putText(img,"Tracking..",(75,90),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,0),2)


while (True):
    ret,img=video.read()
    success,box=tracker.update(img)
    if success:
        drawbox(img,box)
    else:
        cv2.putText(img,"Image lost",(75,90),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,0),2)
    cv2.imshow("VideoCapture",img)
    if cv2.waitKey(1)==32:
        break
video.release()
cv2.destroyAllWindows()