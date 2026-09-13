"""Análisis general del dataset. La carga vive en src/data_loader.py."""

import pandas as pd

from src.data_loader import drop_salary, load_data, prepare_data, show_nulls

# Permite mostrar todas las columnas
pd.set_option("display.max_columns", None)
# Permite mostrar todas las filas segun el ancho de la pantalla
pd.set_option("display.width", 200)

if __name__ == "__main__":
    # Carga el dataset
    df = load_data()

    # Indicar la instrucción o instrucciones para cambiar los nombres de las columnas que se indican
    df = prepare_data(df)
    print(df.head())
    print(df.dtypes)

    # Indicar la instrucción o instrucciones para eliminar la columna Sueldo
    df = drop_salary(df)
    print(df.head())

    # Indicar la instrucción o instrucciones para detectar elementos nulos
    show_nulls(df)
