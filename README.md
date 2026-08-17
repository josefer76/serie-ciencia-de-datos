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
