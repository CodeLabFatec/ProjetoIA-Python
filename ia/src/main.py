from datetime import datetime
from ultralytics import YOLO
import cv2

from tracker import *
from redzone_305 import redzone305

model=YOLO('yolov8s.pt')

area1=[(436,370),(413,372),(627,443),(650,438)]
area2=[(389,374),(360,379),(576,451),(607,443)]

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap1 = cv2.VideoCapture("video-lado.mp4")
cap2 = cv2.VideoCapture("video.mp4")

class_list = model.names

count=0
tracker = Tracker()

timestamps = {}
while True:    
    ret1, frame1 = cap1.read()
    # ret2, frame2 = cap2.read()
    if not ret1:
        break
    count += 1
    if count % 2 != 0:
        continue

    frame1 = cv2.resize(frame1, (1020, 500))
    # frame2 = cv2.resize(frame2, (1020, 500))

    frame1 = redzone305(frame1, model, area1, area2, tracker, class_list)
    # frame2 = redzone305(frame2, model, area1, area2, tracker, class_list)

    cv2.imshow("RGB1", frame1)
    # cv2.imshow("RGB2", frame2)

    if cv2.waitKey(2) & 0xFF == 27:
        break

    cap1.release()
    # cap2.release()
    cv2.destroyAllWindows()