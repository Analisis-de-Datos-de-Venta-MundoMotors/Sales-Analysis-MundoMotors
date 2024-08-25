import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    # Ejemplo de limpieza de datos
    df.dropna(inplace=True)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    return df