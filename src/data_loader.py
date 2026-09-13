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
    """Lee el CSV tal cual viene, sin tocar nombres ni tipos."""
    # el archivo está en latin-1; la última columna llega sin nombre
    return pd.read_csv(path, encoding="latin-1")


def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    """Renombra las columnas y convierte cada una a un tipo compacto."""
    # los nombres nuevos se asignan por posición, así no dependen de la codificación original
    df.columns = COLUMNS

    # fechas en dd/mm/yy del origen, quedan como datetime aaaa-mm-dd
    df["Fecha_Contrato"] = pd.to_datetime(df["Fecha_Contrato"], format="%d/%m/%y")

    # único por fila
    df["Empleado_Clave"] = df["Empleado_Clave"].astype("string")

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
    """Elimina la columna Sueldo, que no entra en el análisis."""
    return df.drop(columns=["Sueldo"])


def show_nulls(df: pd.DataFrame) -> None:
    """Muestra la cantidad de nulos por columna."""
    print("\nNulos por columna:")
    print(df.isna().sum())
