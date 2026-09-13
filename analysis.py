import sys

import pandas as pd

from src.charts import plot_salary_by_gender, plot_salary_vs_fatigue
from src.data_loader import drop_salary, load_data, prepare_data, show_nulls

# la consola de Windows usa cp1252 y no imprime acentos ni símbolos raros
sys.stdout.reconfigure(encoding="utf-8")

# Permite mostrar todas las columnas
pd.set_option("display.max_columns", None)
# Permite mostrar todas las filas segun el ancho de la pantalla
pd.set_option("display.width", 200)

if __name__ == "__main__":
    # Carga el dataset
    df = load_data()

    # Indicar la instrucción o instrucciones para cambiar los nombres de las columnas que se indican
    df = prepare_data(df)
    print("\nColumnas del dataset:")
    print(list(df.columns))

    # Indicar la instrucción o instrucciones para detectar elementos nulos
    show_nulls(df)

    # NOTA: Los gráficos se realizan antes de eliminar la columna Sueldo, ya que se pide eliminarla

    # Indicar la instrucción o instrucciones para graficar un gráfico de barras
    # que muestre el género del empleado y el sueldo que ganan
    print("\nSe muestra gráfico de barras")
    plot_salary_by_gender(df)

    # Indicar la instrucción o instrucciones para graficar un gráfico de dispersión
    # que muestre el sueldo del empleado versus su puntuación de fatiga mental
    print("\nSe muestra gráfico de dispersión")
    plot_salary_vs_fatigue(df)

    # Indicar la instrucción o instrucciones para eliminar la columna Sueldo
    df = drop_salary(df)
    print("\nSe eliminó la columna Sueldo:")
    print(df.head())

