import pandas as pd
import pyodbc 

from main import df


conn = pyodbc.connect('DRIVER={MySQL ODBC 8.3 Unicode Driver}; Database=db_ia_python; UID=root; PWD=fatec') #testei com meu bd local dps mudar para o db do backend

cursor = conn.cursor()

str(df.columns).replace("'","")

for index, linha in df.iterrows():
    
    cursor.execute("Insert into entrada_saida(ids,Data_entrada, Hora_entrada, Data_saida, Hora_saida)values(?, ?, ?, ?, ?)", linha.ID, linha.Data_entrada, linha.Hora_entrada, linha.Data_saida, linha.Hora_saida)
cursor.commit()