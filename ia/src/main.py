from datetime import datetime
from ultralytics import YOLO
import cv2
import pandas as pd
import numpy as np

from send_data import send_df_entrada, send_df_saida, consultar_redzone
from tracker import *
from create_df import create_df_entrada
from create_df import create_df_saida

# Para utilizar o modelo do yolo, basta deixar vazio o parâmetro abaixo, para deixar o nosso modelo treinado,
# copie o path (caminho) do arquivo 'best.pt' que está dentro de /ia/src desse repositório.
model=YOLO('C:/Workspace/ProjetoIA-Python/ia/src/best.pt')

selected_redzone_id = 0
selected_redzone = None
df_redzone = consultar_redzone()

while selected_redzone_id == 0:        
    print("Selecione uma redzone entre as disponíveis abaixo:")
    id_nome_df = df_redzone.loc[:, ['id', 'nome']]
    
    for index, row in id_nome_df.iterrows():
        print("ID:", row['id'], "Nome:", row['nome'])

    redzone_id = int(input("Qual redzone você gostaria de analisar? "))

    if redzone_id in df_redzone['id'].values:
        redzone_data = df_redzone.loc[df_redzone['id'] == redzone_id]

        selected_redzone = redzone_data
        selected_redzone_id = redzone_id
    else:
        print(f"A redzone com o ID {redzone_id} não está definida.")

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        
cv2.waitKey(1000)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap = cv2.VideoCapture(selected_redzone["video_path"].values[0])

area1 = selected_redzone["area1"].values[0]
area2 = selected_redzone["area2"].values[0]

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

# Obtenha a taxa de quadros do vídeo
fps = 90

# Calcule o tempo de espera em milissegundos
wait_time = int(1000 / fps)


while selected_redzone_id != 0: 
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
                df = create_df_entrada(timestamps, selected_redzone_id)
                send_df_entrada(df)
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
                df = create_df_saida(timestamps, selected_redzone_id)
                send_df_saida(df)
                exiting.clear()
                ppl_exiting.clear()
                timestamps.clear()
    
    cv2.polylines(frame,[np.array(area1,np.int32)],True,(255,0,0),2)
    cv2.polylines(frame,[np.array(area2,np.int32)],True,(255,0,0),2)

    entrou = (len(ppl_entering2))
    saiu = (len(ppl_exiting2))
    dentro = (len(ppl_entering2)) - (len(ppl_exiting2))

    cv2.putText(frame, str(entrou), (60, 80), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, str(saiu), (60, 140), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame, str(dentro), (60, 200), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("RGB", frame)
    if cv2.waitKey(0)&0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()