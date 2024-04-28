import pandas as pd

def create_df_entrada(timestamps):
    # ids = []
    data = []
    id_redzone = []
    # Hora_entrada = []

    for id, times in timestamps.items():
        # ids.append(id)
        if 'enter' in times:
            data.append(times['enter'].date())
            # Hora_entrada.append(times['enter'].time())
            id_redzone.append(None)
        else:
            data.append(None)
            # Hora_entrada.append(None)
            id_redzone.append(None)

    df_entrada = pd.DataFrame({
        # 'ID': ids,
        'data': data,
        # # 'Hora_entrada': Hora_entrada
        'id_redzone': id_redzone
    })
    print(df_entrada)
    return df_entrada

def create_df_saida(timestamps):
    ids = []
    data = []
    # Hora_saida = []
    id_redzone = []

    for id, times in timestamps.items():
        ids.append(id)
        if 'exit' in times:
            data.append(times['exit'].date())
            # Hora_saida.append(times['exit'].time())
            id_redzone.append(None)
        else:
            data.append(None)
            # Hora_saida.append(None)
            id_redzone.append(None)

    df_saida = pd.DataFrame({
        # 'ID': ids,
        'data': data,
        # 'Hora_saida': Hora_saida
        'id_redzone': id_redzone
    })
    
    print(df_saida)
    return df_saida
