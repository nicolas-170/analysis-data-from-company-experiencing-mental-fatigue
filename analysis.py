"""Análisis general del dataset. La carga vive en src/data_loader.py."""

import pandas as pd

from src.data_loader import load_data

# Permite mostrar todas las columnas
pd.set_option("display.max_columns", None)
# Permite mostrar todas las filas segun el ancho de la pantalla
pd.set_option("display.width", 200)

if __name__ == "__main__":
    # Carga el dataset
    df = load_data()
    
