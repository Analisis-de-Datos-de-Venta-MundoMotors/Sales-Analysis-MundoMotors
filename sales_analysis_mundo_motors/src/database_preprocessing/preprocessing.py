import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    print(df.columns)  # Imprime las columnas para verificar el nombre exacto

    # Limpiar datos: eliminar filas con valores nulos
    df.dropna(inplace=True)

    # Convertir la columna 'Date' a tipo datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y', errors='coerce')
    
    # Manejar cualquier valor NaT resultante de la conversión fallida
    df.dropna(subset=['Date'], inplace=True)

    return df
