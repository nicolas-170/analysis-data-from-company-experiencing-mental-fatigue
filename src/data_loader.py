"""Carga del CSV: nombres de columnas y tipos de dato viven aquí porque solo se usan al leer."""

import pandas as pd

from src.config import RAW_DATA_PATH

# los encabezados originales tienen una codificación errónea y última columna sin nombre, 
# por lo que se reemplazaran
COLUMNS = [
    "employee_id",
    "join_date",
    "gender",
    "company_type",
    "wfh_setup",
    "designation",
    "resource_allocation",
    "mental_fatigue_score",
    "salary",
]

# columnas de texto con pocos valores distintos 
# se usará category ya que hay pocas etiquetas repetidas
CATEGORICAL_COLUMNS = ["gender", "company_type"]

# designation es una escala de jerarquía
# se usará category ordenada para poder comparar y ordenar
DESIGNATION_ORDER = ["Worker", "Assistant", "Executive", "Manager", "Director", "President"]

# columnas numéricas al tipo más pequeño que las soporta
# rangos: 1-10, 0-10, 0-10000
NUMERIC_DTYPES = {
    "resource_allocation": "Int16",
    "mental_fatigue_score": "float32",
    "salary": "Int32",
}


def load_data(path=RAW_DATA_PATH) -> pd.DataFrame:
    """Lee el CSV, renombra las columnas y convierte cada una a un tipo compacto."""
    # lectura con los nombres nuevos;
    # fechas en dd/mm/yy y archivo en latin-1
    df = pd.read_csv(
        path,
        encoding="latin-1",
        header=0,
        names=COLUMNS,
        parse_dates=["join_date"],
        date_format="%d/%m/%y",
        dtype={
            "employee_id": "string",  # único por fila
            **{col: "category" for col in CATEGORICAL_COLUMNS},
            **NUMERIC_DTYPES,
        },
    )

    # bandera Yes/No se convierte a booleano
    # 1 byte en vez de guardar la etiqueta, da un manejo mas eficiente
    df["wfh_setup"] = df["wfh_setup"].map({"Yes": True, "No": False}).astype("bool")

    # se aplica el orden de jerarquía a designation
    df["designation"] = pd.Categorical(
        df["designation"], categories=DESIGNATION_ORDER, ordered=True
    )

    return df
