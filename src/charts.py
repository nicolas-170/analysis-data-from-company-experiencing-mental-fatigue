"""Gráficos del análisis. Cada función arma una figura y la guarda en reports/figures."""

import matplotlib.pyplot as plt
import pandas as pd

from src.config import FIGURES_DIR

# un solo color por gráfico: la identidad ya la dan las etiquetas del eje
COLOR = "#4a6fa5"


def save_figure(filename: str) -> None:
    """Guarda la figura actual en reports/figures y la cierra."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    plt.savefig(FIGURES_DIR / filename, dpi=150, bbox_inches="tight")
    plt.show()
    plt.close()


def plot_salary_by_gender(df: pd.DataFrame) -> None:
    """Gráfico de barras: sueldo promedio por género del empleado."""
    # promedio de sueldo agrupado por género
    salary_by_gender = df.groupby("Genero_Empleado", observed=True)["Sueldo"].mean()

    plt.figure(figsize=(7, 5))
    plt.bar(salary_by_gender.index.astype(str), salary_by_gender.values, color=COLOR, width=0.55)
    plt.title("Sueldo promedio por género del empleado")
    plt.xlabel("Género del empleado")
    plt.ylabel("Sueldo promedio")

    save_figure("sueldo_por_genero.png")


def plot_salary_vs_fatigue(df: pd.DataFrame) -> None:
    """Gráfico de dispersión: sueldo del empleado frente a su fatiga mental."""
    plt.figure(figsize=(7, 5))
    # son 12k puntos: alpha baja y marcador chico para ver la densidad
    plt.scatter(df["Fatiga_mental"], df["Sueldo"], s=10, alpha=0.2, color=COLOR)
    plt.title("Sueldo frente a puntuación de fatiga mental")
    plt.xlabel("Puntuación de fatiga mental")
    plt.ylabel("Sueldo")

    save_figure("sueldo_vs_fatiga.png")
