import pyodbc 

def send_data(df):

    conn = pyodbc.connect('DRIVER={MySQL ODBC 8.3 Unicode Driver}; Database=api_6sem; UID=root; PWD=fatec')

    cursor = conn.cursor()

    str(df.columns).replace("'","")

    for index, linha in df.iterrows():
        
        cursor.execute("Insert into registros(Data_entrada, Hora_entrada, Data_saida, Hora_saida)values(?, ?, ?, ?)",
                       linha.Data_entrada, linha.Hora_entrada, linha.Data_saida, linha.Hora_saida)
    cursor.commit()
    cursor.close()