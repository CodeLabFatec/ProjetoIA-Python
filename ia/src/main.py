from datetime import datetime
from ultralytics import YOLO
import cv2
import pandas as pd
import numpy as np

from tracker import *
from create_df import create_dataframe
from send_data import send_data

model=YOLO('yolov8s.pt')

cap = None
area1 = None
area2 = None


def redzone(redzone_number):
    global cap, area1, area2 

    redzones = {
        305: {"video_path": "video-lado.mp4", "area1": [(436, 370), (413, 372), (627, 443), (650, 438)],
              "area2": [(389, 374), (360, 379), (576, 451), (607, 443)]},
              
        307: {"video_path": "video.mp4", "area1": [(436, 370), (413, 372), (627, 443), (650, 438)],
              "area2": [(389, 374), (360, 379), (576, 451), (607, 443)]}
    }
    
    if redzone_number not in redzones:
        print(f"A redzone {redzone_number} não está definida.")
        return

    redzone_data = redzones[redzone_number]
    video_path = redzone_data["video_path"]
    area1 = redzone_data["area1"]
    area2 = redzone_data["area2"]

    cap = cv2.VideoCapture(video_path)
    return redzone_number

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

redzone_number = redzone(307)

class_list = model.names

count=0
tracker = Tracker()
lista_id = []
bbox_id = tracker.update(lista_id)
entering = {}
ppl_entering = set()
ppl_entering2 = set()

exiting = {}
ppl_exiting = set()
ppl_exiting2 = set()

timestamps = {}
while True:    
    ret,frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 2 != 0:
        continue
    frame=cv2.resize(frame,(1020,500))
    results=model.predict(frame)
    a=results[0].boxes.data
    px=pd.DataFrame(a).astype("float")
    lista_id.clear()
             
    for index,row in px.iterrows():
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]
        
        if 'person' in c:
           lista_id.append([x1, y1, x2, y2])
    bbox_id = tracker.update(lista_id)
    for i, bbox in enumerate(bbox_id):
        x3, y3, x4, y4, id = bbox
        results = cv2.pointPolygonTest(np.array(area2, np.int32), (x4, y4), False)
        if results >= 0:
            entering[id] = (x4, y4)
            cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 2)
        if id in entering:
            results_area1 = cv2.pointPolygonTest(np.array(area1, np.int32), (x4, y4), False)
            if results_area1 >= 0:
                cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 255, 0), 2)
                cv2.circle(frame, (x4, y4), 4, (255, 0, 255), -1)
                cv2.putText(frame, str(id), (x3, y3), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                ppl_entering.add(id)
                ppl_entering2.add(id)
                timestamps[id] = {'enter': datetime.now()}
                df = create_dataframe(timestamps, redzone_number)
                send_data(df)
                entering.clear()
                ppl_entering.clear()
                timestamps.clear()

      
        
        results_exiting = cv2.pointPolygonTest(np.array(area1, np.int32), (x4, y4), False)
        if results_exiting >= 0:
            exiting[id] = (x4, y4)
            cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 255, 0), 2)


        if id in exiting:
            results_area2 = cv2.pointPolygonTest(np.array(area2, np.int32), (x4, y4), False)
            if results_area2 >= 0:
                cv2.rectangle(frame, (x3, y3), (x4, y4), (255, 0, 0), 2)
                cv2.circle(frame, (x4, y4), 4, (255, 0, 255), -1)
                cv2.putText(frame, str(id), (x3, y3), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                ppl_exiting.add(id)
                ppl_exiting2.add(id)
                timestamps[id] = {'exit': datetime.now()}
                df = create_dataframe(timestamps, redzone_number)
                send_data(df)
                exiting.clear()
                ppl_exiting.clear()
                timestamps.clear()


    
    cv2.polylines(frame,[np.array(area1,np.int32)],True,(255,0,0),2)
    cv2.polylines(frame,[np.array(area2,np.int32)],True,(255,0,0),2)

    entrou = (len(ppl_entering2))
    saiu = (len(ppl_exiting2))
    dentro = (len(ppl_entering2)) - (len(ppl_exiting2))
    limite = 3

    cv2.putText(frame, str(entrou), (60, 80), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, str(saiu), (60, 140), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame, str(dentro), (60, 200), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)
    if dentro > limite:
        cv2.putText(frame, str("LIMITE ATINGIDO"), (40, 260), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("RGB", frame)
    if cv2.waitKey(4)&0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()