import pandas as pd

def create_df_entrada(timestamps, redzone_id):
    data = []
    id_redzone = []

    for id, times in timestamps.items():
        if 'enter' in times:
            data.append(times['enter'])
            id_redzone.append(redzone_id)
        else:
            data.append(None)
            id_redzone.append(None)

    df_entrada = pd.DataFrame({
        'data': data,
        'id_redzone': id_redzone
    })
    return df_entrada

def create_df_saida(timestamps, redzone_id):
    ids = []
    data = []
    id_redzone = []

    for id, times in timestamps.items():
        ids.append(id)
        if 'exit' in times:
            data.append(times['exit'])
            id_redzone.append(redzone_id)
        else:
            data.append(None)
            id_redzone.append(None)

    df_saida = pd.DataFrame({
        'data': data,
        'id_redzone': id_redzone
    })
    return df_saida
