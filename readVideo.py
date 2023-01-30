import cv2

vid=cv2.VideoCapture(0)
if(vid.isOpened()==False):
    print("Your camera is opened")

height=int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
width=int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
fps=int(vid.get(cv2.CAP_PROP_FPS))
print(height)
print(width)
print(fps)

while(True):
  rate,frame=vid.read()
  cv2.imshow("CameraOpener",frame)
  if(cv2.waitKey(1)==32):
    break

vid.release()