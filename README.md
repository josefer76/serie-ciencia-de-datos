# Serie Ciencia de Datos

Código, datos y cuadernos de la serie de libros de ciencia de datos en español de
**José Fernando Meza**.

Los libros se venden por separado. Este repositorio contiene el material de prácticas:
el código de cada capítulo, listo para ejecutarse, y los conjuntos de datos que usan
los ejemplos.

## Tomo 1 — Introducción al Data Science y Programación con Python

Un cuaderno por capítulo. Se abren en Google Colab con un clic, sin instalar nada.

| Capítulo | Título | |
|---|---|---|
| 1 | ¿Qué es el Data Science? Panorama, evolución y roles | [Abrir en Colab](https://colab.research.google.com/github/josefer76/serie-ciencia-de-datos/blob/main/libro1/notebooks/Cap01.ipynb) |
| 2 | Metodología CRISP-DM y ejemplos del mundo real | [Abrir en Colab](https://colab.research.google.com/github/josefer76/serie-ciencia-de-datos/blob/main/libro1/notebooks/Cap02.ipynb) |
| 3 | Entorno de trabajo: Python, Google Colab y primeros pasos | [Abrir en Colab](https://colab.research.google.com/github/josefer76/serie-ciencia-de-datos/blob/main/libro1/notebooks/Cap03.ipynb) |
| 4 | Operadores, expresiones y lógica de control | [Abrir en Colab](https://colab.research.google.com/github/josefer76/serie-ciencia-de-datos/blob/main/libro1/notebooks/Cap04.ipynb) |
| 5 | Estructuras de control: bucles y flujo avanzado | [Abrir en Colab](https://colab.research.google.com/github/josefer76/serie-ciencia-de-datos/blob/main/libro1/notebooks/Cap05.ipynb) |
| 6 | Estructuras de datos: listas, tuplas, sets y diccionarios | [Abrir en Colab](https://colab.research.google.com/github/josefer76/serie-ciencia-de-datos/blob/main/libro1/notebooks/Cap06.ipynb) |
| 7 | Funciones, manejo de errores y módulos | [Abrir en Colab](https://colab.research.google.com/github/josefer76/serie-ciencia-de-datos/blob/main/libro1/notebooks/Cap07.ipynb) |
| 8 | Taller integrador: Python aplicado a Data Science | [Abrir en Colab](https://colab.research.google.com/github/josefer76/serie-ciencia-de-datos/blob/main/libro1/notebooks/Cap08.ipynb) |

Los capítulos 1 y 2 son conceptuales y no contienen código ejecutable; sus cuadernos
existen para mantener la correspondencia con el libro.

Ejecute las celdas en orden: algunas dependen de variables definidas antes. Las celdas
que usan `input()` esperan que usted escriba un valor.

## Tomo 2 — Herramientas Python para Data Science: NumPy, Pandas y Visualización

Un cuaderno por capítulo, con las soluciones de los ejercicios de ese capítulo. Se abren en Google Colab con un clic, sin instalar nada en su ordenador.

| Capítulo | Título | |
|---|---|---|
| 1 | NumPy I: el array, la vectorización y el fin de los bucles | [Abrir en Colab](https://colab.research.google.com/github/josefer76/serie-ciencia-de-datos/blob/main/libro2/notebooks/Cap01.ipynb) |
| 2 | NumPy II: broadcasting, agregaciones, máscaras y aleatoriedad | [Abrir en Colab](https://colab.research.google.com/github/josefer76/serie-ciencia-de-datos/blob/main/libro2/notebooks/Cap02.ipynb) |
| 3 | Pandas I: Series, DataFrames, carga y selección | [Abrir en Colab](https://colab.research.google.com/github/josefer76/serie-ciencia-de-datos/blob/main/libro2/notebooks/Cap03.ipynb) |
| 4 | Pandas II: limpieza, transformación, agrupación y combinación | [Abrir en Colab](https://colab.research.google.com/github/josefer76/serie-ciencia-de-datos/blob/main/libro2/notebooks/Cap04.ipynb) |
| 5 | Visualización con Matplotlib y Seaborn | [Abrir en Colab](https://colab.research.google.com/github/josefer76/serie-ciencia-de-datos/blob/main/libro2/notebooks/Cap05.ipynb) |
| 6 | EDA asistido y taller integrador | [Abrir en Colab](https://colab.research.google.com/github/josefer76/serie-ciencia-de-datos/blob/main/libro2/notebooks/Cap06.ipynb) |

La primera celda de los cuadernos de los capítulos 3 a 6 instala pandas 2.3.3 —y, en el capítulo 6, también ydata-profiling 4.18.4—, las versiones con las que se verificó el libro. Ejecútela antes que las demás. pip mostrará en rojo un aviso de conflicto con el paquete google-colab: no es un fallo y no hace falta reiniciar la sesión.

Ejecute las celdas en orden: algunas dependen de variables definidas antes. Las salidas que publica el libro aparecen como texto, con el rótulo «Salida en el libro», debajo del código que las produce.

Los datos del tomo están en `libro2/datos/`. Los cuadernos los leen directamente de GitHub; no hace falta descargarlos.

| Archivo | Dónde se usa |
|---|---|
| `anscombe.csv` | Capítulo 5, sección 5.6 (cuarteto de Anscombe). |
| `correlacion_cap5.csv` | Capítulo 5, sección 5.6 (Pearson y Spearman). |
| `ventas_cap5.csv` | Capítulo 5, secciones 5.2, 5.4, 5.5 y 5.6. |
| `pedidos_taller.csv` | Capítulo 6, secciones 6.2 y 6.4, y ejercicio Ex-L2-C6-01. |
| `ventas_limpias_c4.csv` | Ejercicio Ex-L2-C4-02. |

Para trabajar en su propio equipo, use Python 3.13 y ejecute `pip install -r libro2/requirements.txt`: el archivo fija las versiones exactas del libro. Para abrir los cuadernos necesitará además Jupyter. `libro2/entorno_verificacion_2026-10-19.txt` es el registro completo del entorno con el que se verificó.

## Datos

`datos/` contiene los generadores del conjunto de datos que recorre toda la serie y el
archivo ya generado.

| Archivo | Qué es |
|---|---|
| `pedidos.csv` | Conjunto de datos troncal de la serie. |
| `generar_pedidos.py` | Lo genera. Semilla fija `20260809`. |
| `generar_corpus.py` | Corpus de idiomas usado en los tomos 1 y 2. |
| `corpus_ampliado.py` | Ampliación del corpus para el tomo 3. |

Las semillas están fijadas: ejecutar los generadores reproduce exactamente las mismas
cifras que aparecen publicadas en los libros.

## Licencia

El **código** de este repositorio se publica bajo licencia MIT (véase `LICENSE`): puede
usarlo, modificarlo y reutilizarlo, incluso con fines comerciales, conservando el aviso
de autoría.

El **texto de los libros** no está cubierto por esa licencia y conserva todos los
derechos reservados.
