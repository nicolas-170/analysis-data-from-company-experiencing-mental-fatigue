# Análisis de datos de una empresa con fatiga mental

Hecho por: **Nicolas Parada Cuervo**

Proyecto en Python que carga una encuesta de empleados, limpia y tipifica los datos,
revisa valores nulos y genera dos gráficos sobre la relación entre sueldo, género y
fatiga mental.

## Contenido del CSV

Archivo: `data/employee_survey.csv` — 12.249 registros, 9 columnas.
Los encabezados originales vienen con una codificación errónea, por lo que se
reemplazan al cargar por nombres internos:

| Columna original | Nombre usado | Descripción |
|---|---|---|
| ID del empleado | `Empleado_Clave` | Identificador del empleado (texto) |
| Fecha de incorporación | `Fecha_Contrato` | Fecha de contratación (`dd/mm/aa` → `datetime`) |
| Género | `Genero_Empleado` | Female / Male (categórica) |
| Tipo de trabajo | `Tipo_Empresa` | Service / Product (categórica) |
| Configuración de su forma de trabajo | `Trabajo_Remoto` | Yes/No convertido a booleano |
| Designación | `Cargo` | Jerarquía ordenada: Worker → Assistant → Executive → Manager → Director → President |
| Asignación de horas | `Asignacion_Horas` | Horas asignadas (1–10) |
| Puntuación de fatiga mental | `Fatiga_mental` | Puntuación de 0 a 10 |
| sueldo | `Sueldo` | Sueldo del empleado (0–10000) |

Los tipos se asignan al más compacto posible (`Int16`, `float32`, `Int32`, `category`)
para reducir el uso de memoria.

## Puntos que se realizan

1. Cargar el dataset desde `data/employee_survey.csv`.
2. Renombrar las columnas y convertir cada una a su tipo de dato adecuado.
3. Detectar y reportar los elementos nulos por columna y el total.
4. Gráfico de barras: sueldo promedio por género del empleado.
5. Gráfico de dispersión: sueldo del empleado frente a su puntuación de fatiga mental.
6. Eliminar la columna `Sueldo` y mostrar el resultado.

Los gráficos se generan **antes** de eliminar `Sueldo`, ya que esa columna es
necesaria para ambos. Las imágenes se guardan en `reports/figures/`
(`sueldo_por_genero.png` y `sueldo_vs_fatiga.png`).

## Estructura del proyecto

```
analysis.py            # script principal, ejecuta los pasos en orden
src/config.py          # rutas del proyecto
src/data_loader.py     # carga, tipificación, nulos y eliminación de Sueldo
src/charts.py          # generación y guardado de los gráficos
data/                  # dataset de entrada
reports/figures/       # gráficos generados
```

## Requisitos

- Python 3.10 o superior (probado en 3.13)
- pandas
- matplotlib

## Cómo ejecutarlo

Desde la raíz del proyecto:

```bash
# 1. Crear y activar un entorno virtual
python -m venv .venv
.venv\Scripts\activate        # Windows (PowerShell/CMD)
# source .venv/bin/activate   # Linux / macOS

# 2. Instalar las dependencias
pip install pandas matplotlib

# 3. Ejecutar el análisis
python analysis.py
```

El script imprime en consola las columnas del dataset, el conteo de nulos y las
primeras filas sin la columna `Sueldo`; además abre cada gráfico en una ventana y
lo guarda en `reports/figures/`.

> Debe ejecutarse desde la raíz del proyecto para que `import src...` funcione.
