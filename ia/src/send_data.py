import sqlalchemy 
import pandas as pd

user = 'root'
password = 'thales'
host = 'localhost'
database = 'api_6sem'

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
   if x % 2 == 0:
      return "C:/Users/Thales Kerber/OneDrive/Área de Trabalho/Projeto Integrador 6º/ProjetoIA/ProjetoIA-Python/ia/src/video-lado.mp4"
   else:
      return "C:/Users/Thales Kerber/OneDrive/Área de Trabalho/Projeto Integrador 6º/ProjetoIA/ProjetoIA-Python/ia/src/video.mp4"
   
def getArea(x):
   return [(436, 370), (413, 372), (627, 443), (650, 438)]

def getArea2(x):
   return [(389, 374), (360, 379), (576, 451), (607, 443)]