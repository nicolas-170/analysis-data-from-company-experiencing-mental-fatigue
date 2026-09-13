"""Rutas del proyecto, resueltas desde la raíz para que no dependan del cwd."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_PATH = DATA_DIR / "employee_survey.csv"

FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"
