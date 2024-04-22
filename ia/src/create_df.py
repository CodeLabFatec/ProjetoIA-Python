import pandas as pd

def create_dataframe(timestamps, redzone_number):
    ids = []
    Data_entrada = []
    Hora_entrada = []
    Data_saida = []
    Hora_saida = []
    Redzone_number = []
    

    for id, times in timestamps.items():
        ids.append(id)
        if 'enter' in times:
            Data_entrada.append(times['enter'].date())
            Hora_entrada.append(times['enter'].time())
        else:
            Data_entrada.append(None)
            Hora_entrada.append(None)
        if 'exit' in times:
            Data_saida.append(times['exit'].date())
            Hora_saida.append(times['exit'].time())
        else:
            Data_saida.append(None)
            Hora_saida.append(None)
        Redzone_number.append(redzone_number)

    # Redzone_number = [redzone_number] * len(ids)

    df = pd.DataFrame({
        'ID': ids,
        'Data_entrada': Data_entrada,
        'Hora_entrada': Hora_entrada,
        'Data_saida': Data_saida,
        'Hora_saida': Hora_saida,
        'Redzone_number': Redzone_number
    })

    print(df)

    return df