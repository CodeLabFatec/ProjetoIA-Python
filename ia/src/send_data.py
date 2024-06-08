import sqlalchemy 
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database = os.getenv("DB_DATABASE")

connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
engine = sqlalchemy.create_engine(connection_string)

def send_df_entrada(df):

   df.to_sql("entrada_redzone", engine, index=False, if_exists="append")

def send_df_saida(df):

   df.to_sql("saida_redzone", engine, index=False, if_exists="append")

def consultar_redzone():
    query = "SELECT id, nome FROM redzone where status = true"
    df_redzone = pd.read_sql_query(query, engine)

    df_redzone['video_path'] = df_redzone['id'].apply(lambda x: getVideo(x))
    df_redzone['area1'] = df_redzone['id'].apply(lambda x: getArea(x))
    df_redzone['area2'] = df_redzone['id'].apply(lambda x: getArea2(x))

    return df_redzone

def getVideo(x):
   if x % 4 == 0:
      return "../videos/video.mp4"
   if x % 3 == 0:
      return "../videos/video-lado.mp4"
   if x % 2 == 0:
      return "../videos/video-novo.mp4"
   else:
      return "../videos/video-sementrar.mp4"
   
def getArea(x):
   if x % 4 == 0:
      return [(436, 370), (413, 372), (627, 443), (650, 438)]
   if x % 3 == 0:
      return [(436, 370), (413, 372), (627, 443), (650, 438)]
   if x % 2 == 0:
      return [(362, 385), (337, 374), (452, 339), (495, 348)]
   else:
      return [(362, 385), (337, 374), (452, 339), (495, 348)]

def getArea2(x):
   if x % 4 == 0:
      return [(389, 374), (360, 379), (576, 451), (607, 443)]
   if x % 3 == 0:
      return [(389, 374), (360, 379), (576, 451), (607, 443)]
   if x % 2 == 0:
      return [(375, 399), (421, 421), (525, 370), (491, 356)]
   else:
      return [(375, 399), (421, 421), (525, 370), (491, 356)]