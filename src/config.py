"""Rutas del proyecto, resueltas desde la raíz para que no dependan del cwd."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_PATH = DATA_DIR / "Data_company_experiencing_mental_fatigue.csv"
