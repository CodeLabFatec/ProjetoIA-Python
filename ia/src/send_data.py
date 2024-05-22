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
    query = "SELECT id, nome FROM redzone"
    df_redzone = pd.read_sql_query(query, engine)

    df_redzone['video_path'] = df_redzone['id'].apply(lambda x: getVideo(x))
    df_redzone['area1'] = df_redzone['id'].apply(lambda x: getArea(x))
    df_redzone['area2'] = df_redzone['id'].apply(lambda x: getArea2(x))

    return df_redzone

def getVideo(x):
   # use essa função para selecionar os vídeos que queira utilizar... a lógica atual está para
   # quando o ID da redzone selecionada for PAR o vídeo novo será executado, quando for IMPAR o vídeo
   # novo sem entrar será executado.
   if x % 2 == 0:
      return "C:/Users/Thales Kerber/OneDrive/Área de Trabalho/Projeto Integrador 6º/ProjetoIA/ProjetoIA-Python/ia/src/video-novo.mp4"
   else:
      return "C:/Users/Thales Kerber/OneDrive/Área de Trabalho/Projeto Integrador 6º/ProjetoIA/ProjetoIA-Python/ia/src/video-sementrar.mp4"
   
def getArea(x):
    return [(362, 385), (337, 374), (452, 339), (495, 348)] # vídeo novo SEM entrada (video-sementrar.mp4)
   # return [(463, 359), (482, 348), (553, 396), (554, 413)] vídeo novo com a entrada (video-novo.mp4)
   # return [(436, 370), (413, 372), (627, 443), (650, 438)] vídeos antigos (video.mp4 e video-lado.mp4)

def getArea2(x):
    return [(375, 399), (421, 421), (525, 370), (491, 356)] # vídeo novo SEM entrada (video-sementrar.mp4)
   # return [(425, 367), (401, 379), (558, 446), (547, 425)] vídeo novo com a entrada (video-novo.mp4)
   # return [(389, 374), (360, 379), (576, 451), (607, 443)] vídeos antigos (video.mp4 e video-lado.mp4)