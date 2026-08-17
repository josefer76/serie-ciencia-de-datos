#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corpus de idiomas de la serie: núcleo histórico y ampliación publicada.

Este archivo es la fuente única del segundo hilo de datos de la serie, el que
sostiene el proyecto de similitud: Jaccard en el Libro 1, similitud coseno en
el Libro 2, familia de medidas en el Capítulo 10 del Libro 3 y embeddings en
los Libros 8 y 9.

Está dividido en dos partes que conviene no confundir:

1. NÚCLEO HISTÓRICO — `IDIOMAS_LIBRO_1`
   Los cuatro idiomas y los diez conceptos publicados literalmente en el
   Libro 1 (§8.3) y reutilizados en el Libro 2 (§2.5). Se reproducen aquí sin
   una sola modificación, porque de ellos dependen cifras ya publicadas:

       Jaccard  español-portugués = 0.429
       Coseno   español-portugués = 0.600
       Matriz binaria de forma (4, 34)

   La función `verificar_nucleo()` comprueba esas tres cifras. Si alguna vez
   falla, el núcleo se ha tocado y hay resultados publicados que dejan de ser
   ciertos.

2. AMPLIACIÓN — `IDIOMAS_AMPLIADOS`
   Cuatro idiomas más sobre los mismos diez conceptos. La ampliación es
   estrictamente aditiva: no cambia ninguna palabra del núcleo, solo añade
   filas. Existe porque el Capítulo 10 del Libro 3 necesita más de cuatro
   observaciones para que las medidas basadas en covarianza tengan sentido.

Convención ortográfica, heredada del Libro 1: todas las palabras van en
minúscula y sin signos diacríticos («mao» por «mão», «lumiere» por
«lumière»), incluidos los sustantivos alemanes, que en su idioma se
escribirían con mayúscula inicial. La convención es discutible pero se
mantiene por compatibilidad con lo ya publicado.

Uso:
    from generar_corpus import corpus, perfiles_de_letras
    idiomas = corpus()                    # los ocho idiomas
    idiomas = corpus(solo_nucleo=True)    # los cuatro del Libro 1
"""

from __future__ import annotations

import numpy as np

# Los diez conceptos, en el orden en que se presentaron en el Libro 1.
CONCEPTOS = ["casa", "sol", "luna", "agua", "noche",
             "mano", "libro", "flor", "mar", "luz"]

# --------------------------------------------------------------------------
# 1. Núcleo histórico: copiado literalmente del Libro 1, §8.3.
# --------------------------------------------------------------------------
IDIOMAS_LIBRO_1 = {
    "Español":   {"casa", "sol", "luna", "agua", "noche",
                  "mano", "libro", "flor", "mar", "luz"},
    "Inglés":    {"house", "sun", "moon", "water", "night",
                  "hand", "book", "flower", "sea", "light"},
    "Portugués": {"casa", "sol", "lua", "agua", "noite",
                  "mao", "livro", "flor", "mar", "luz"},
    "Francés":   {"maison", "soleil", "lune", "eau", "nuit",
                  "main", "livre", "fleur", "mer", "lumiere"},
}

# --------------------------------------------------------------------------
# 2. Ampliación aditiva para el Capítulo 10 del Libro 3.
# --------------------------------------------------------------------------
IDIOMAS_AMPLIADOS = {
    "Italiano":   {"casa", "sole", "luna", "acqua", "notte",
                   "mano", "libro", "fiore", "mare", "luce"},
    "Catalán":    {"casa", "sol", "lluna", "aigua", "nit",
                   "ma", "llibre", "flor", "mar", "llum"},
    "Alemán":     {"haus", "sonne", "mond", "wasser", "nacht",
                   "hand", "buch", "blume", "meer", "licht"},
    "Neerlandés": {"huis", "zon", "maan", "water", "nacht",
                   "hand", "boek", "bloem", "zee", "licht"},
}

# El mismo contenido, ordenado por concepto: hace falta para construir los
# perfiles de letras sin depender del orden arbitrario de un conjunto.
PALABRAS_POR_CONCEPTO = {
    "Español":    ["casa", "sol", "luna", "agua", "noche",
                   "mano", "libro", "flor", "mar", "luz"],
    "Inglés":     ["house", "sun", "moon", "water", "night",
                   "hand", "book", "flower", "sea", "light"],
    "Portugués":  ["casa", "sol", "lua", "agua", "noite",
                   "mao", "livro", "flor", "mar", "luz"],
    "Francés":    ["maison", "soleil", "lune", "eau", "nuit",
                   "main", "livre", "fleur", "mer", "lumiere"],
    "Italiano":   ["casa", "sole", "luna", "acqua", "notte",
                   "mano", "libro", "fiore", "mare", "luce"],
    "Catalán":    ["casa", "sol", "lluna", "aigua", "nit",
                   "ma", "llibre", "flor", "mar", "llum"],
    "Alemán":     ["haus", "sonne", "mond", "wasser", "nacht",
                   "hand", "buch", "blume", "meer", "licht"],
    "Neerlandés": ["huis", "zon", "maan", "water", "nacht",
                   "hand", "boek", "bloem", "zee", "licht"],
}

ALFABETO = "abcdefghijklmnopqrstuvwxyz"


# --------------------------------------------------------------------------
# Representaciones
# --------------------------------------------------------------------------

def corpus(solo_nucleo: bool = False) -> dict[str, set[str]]:
    """Devuelve el corpus como diccionario de conjuntos de palabras."""
    if solo_nucleo:
        return {nombre: set(palabras)
                for nombre, palabras in IDIOMAS_LIBRO_1.items()}
    completo = dict(IDIOMAS_LIBRO_1)
    completo.update(IDIOMAS_AMPLIADOS)
    return {nombre: set(palabras) for nombre, palabras in completo.items()}


def vocabulario(idiomas: dict[str, set[str]]) -> list[str]:
    """Vocabulario conjunto ordenado: define los ejes del espacio vectorial."""
    return sorted(set().union(*idiomas.values()))


def matriz_binaria(idiomas: dict[str, set[str]]) -> np.ndarray:
    """Una fila por idioma, un uno por palabra presente en el vocabulario."""
    ejes = vocabulario(idiomas)
    return np.array([[1 if palabra in idiomas[nombre] else 0 for palabra in ejes]
                     for nombre in idiomas], dtype=float)


def perfiles_de_letras(nombres: list[str] | None = None) -> tuple[np.ndarray, list[str]]:
    """Frecuencia relativa de cada letra del alfabeto latino por idioma.

    Se calcula sobre la lista de palabras publicada, no sobre un texto
    externo: cualquiera puede recomputarla exactamente. La muestra es
    deliberadamente pequeña —diez palabras por idioma— y el Capítulo 10 del
    Libro 3 discute qué consecuencias tiene eso sobre las divergencias.
    """
    nombres = nombres or list(PALABRAS_POR_CONCEPTO)
    filas = []
    for nombre in nombres:
        texto = "".join(PALABRAS_POR_CONCEPTO[nombre])
        cuentas = np.array([texto.count(letra) for letra in ALFABETO],
                           dtype=float)
        filas.append(cuentas / cuentas.sum())
    return np.array(filas), list(ALFABETO)


def indice_jaccard(conjunto_a: set[str], conjunto_b: set[str]) -> float:
    """Tamaño de la intersección dividido entre el tamaño de la unión."""
    return len(conjunto_a & conjunto_b) / len(conjunto_a | conjunto_b)


# --------------------------------------------------------------------------
# Autocomprobación del núcleo
# --------------------------------------------------------------------------

def verificar_nucleo(verboso: bool = True) -> bool:
    """Comprueba las tres cifras que los Libros 1 y 2 ya dieron por buenas."""
    nucleo = corpus(solo_nucleo=True)
    ejes = vocabulario(nucleo)
    binaria = matriz_binaria(nucleo)
    unitaria = binaria / np.linalg.norm(binaria, axis=1, keepdims=True)
    coseno = unitaria @ unitaria.T
    nombres = list(nucleo)
    i, j = nombres.index("Español"), nombres.index("Portugués")

    comprobaciones = [
        ("forma de la matriz binaria", binaria.shape, (4, 34)),
        ("Jaccard español-portugués",
         round(indice_jaccard(nucleo["Español"], nucleo["Portugués"]), 3), 0.429),
        ("coseno español-portugués", round(float(coseno[i, j]), 3), 0.600),
    ]
    todo_bien = all(obtenido == esperado for _, obtenido, esperado in comprobaciones)
    if verboso:
        print(f"Vocabulario conjunto del núcleo: {len(ejes)} palabras")
        for etiqueta, obtenido, esperado in comprobaciones:
            marca = "ok" if obtenido == esperado else "FALLA"
            print(f"  {etiqueta:32} {obtenido!s:>10}  "
                  f"(publicado {esperado})  {marca}")
    return todo_bien


if __name__ == "__main__":
    print("Núcleo histórico (Libros 1 y 2)")
    correcto = verificar_nucleo()

    ampliado = corpus()
    print(f"\nCorpus ampliado: {len(ampliado)} idiomas, "
          f"{len(vocabulario(ampliado))} palabras distintas")
    perfiles, letras = perfiles_de_letras()
    print(f"Perfiles de letras: {perfiles.shape[0]} idiomas × "
          f"{perfiles.shape[1]} letras")
    print(f"Cada perfil suma 1: "
          f"{np.allclose(perfiles.sum(axis=1), 1.0)}")

    if not correcto:
        raise SystemExit("El núcleo histórico no reproduce lo publicado.")
