import cv2
import mediapipe as mp

video=cv2.VideoCapture(0)

mpHands=mp.solutions.hands
mpDrawing=mp.solutions.drawing_utils
hands=mpHands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5)
 
def drawing(img,landMark):
    if landMark:
        for marks in landMark:
            mpDrawing.draw_landmarks(img,marks,mpHands.HAND_CONNECTIONS)



while (True):
  ret, img=video.read()
  result=hands.process(img)
  handMarks=result.multi_hand_landmarks
  drawing(img,handMarks)
  cv2.imshow("cam",img)
  if cv2.waitKey(1)==32:
    break
video.release()
cv2.destroyAllWindows()
