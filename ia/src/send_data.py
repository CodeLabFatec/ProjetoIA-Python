import sqlalchemy 
import pandas as pd

user = 'root'
password = 'fatec'
host = 'localhost'
database = 'api_6sem'

connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
engine = sqlalchemy.create_engine(connection_string)

def send_df_entrada(df):

   df.to_sql("entrada_redzone", engine, index=False, if_exists="append")

def send_df_saida(df):

   df.to_sql("saida_redzone", engine, index=False, if_exists="append")

def consultar_redzone():
    # Consulta os campos 'id' e 'nome' da tabela 'redzone'
    query = "SELECT id, nome FROM redzone"
    df_redzone = pd.read_sql_query(query, engine)
    return df_redzone