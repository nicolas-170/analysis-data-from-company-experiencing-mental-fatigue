"""Carga del CSV: nombres de columnas y tipos de dato viven aquí porque solo se usan al leer."""

import pandas as pd

from src.config import RAW_DATA_PATH

# los encabezados originales tienen una codificación errónea y última columna sin nombre, 
# por lo que se reemplazaran
COLUMNS = [
    "Empleado_Clave",
    "Fecha_Contrato",
    "Genero_Empleado",
    "Tipo_Empresa",
    "Trabajo_Remoto",
    "Cargo",
    "Asignacion_Horas",
    "Fatiga_mental",
    "Sueldo",
]

# columnas de texto con pocos valores distintos 
# se usará category ya que hay pocas etiquetas repetidas
CATEGORICAL_COLUMNS = ["Genero_Empleado", "Tipo_Empresa"]

# designation es una escala de jerarquía
# se usará category ordenada para poder comparar y ordenar
CARGO_ORDER = ["Worker", "Assistant", "Executive", "Manager", "Director", "President"]

# columnas numéricas al tipo más pequeño que las soporta
# rangos: 1-10, 0-10, 0-10000
NUMERIC_DTYPES = {
    "Asignacion_Horas": "Int16",
    "Fatiga_mental": "float32",
    "Sueldo": "Int32",
}


def load_data(path=RAW_DATA_PATH) -> pd.DataFrame:
    # Lee el CSV
    # el encoding latin-1 se usa para evitar errores con los caracteres especiales de los nombres de las columnas
    return pd.read_csv(path, encoding="utf-8")


def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    # Se asignan los nombres a las columnas
    df.columns = COLUMNS

    # Se convierten las fechas a datetime
    df["Fecha_Contrato"] = pd.to_datetime(df["Fecha_Contrato"], format="%d/%m/%y")

    # Se convierte la columna Empleado_Clave a string
    df["Empleado_Clave"] = df["Empleado_Clave"].astype("string")

    # Se convierten las columnas categóricas a category
    for column in CATEGORICAL_COLUMNS:
        df[column] = df[column].astype("category")

    for column, dtype in NUMERIC_DTYPES.items():
        df[column] = df[column].astype(dtype)

    # bandera Yes/No se convierte a booleano, da un manejo mas eficiente
    df["Trabajo_Remoto"] = df["Trabajo_Remoto"].map({"Yes": True, "No": False}).astype("bool")

    # se aplica el orden de jerarquía a Cargo
    df["Cargo"] = pd.Categorical(df["Cargo"], categories=CARGO_ORDER, ordered=True)

    return df


def drop_salary(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop(columns=["Sueldo"])

def show_nulls(df: pd.DataFrame) -> None:
    # ancho de la columna más larga, para que los números queden alineados
    width = max(len(str(column)) for column in df.columns)
    null_counts = df.isna().sum()

    print("\nNulos por columna:")
    for column, total in null_counts.items():
        print(f"  {column:<{width}}  {total}")
    print(f"\nTotal de nulos en los datos: {null_counts.sum()}\n")
    
