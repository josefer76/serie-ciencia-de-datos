# -*- coding: utf-8 -*-
"""Ampliación ADITIVA del corpus de idiomas, para [Ex-L3-C10-03].

Regla de oro de esta ampliación: el núcleo histórico de los Libros 1 y 2 no
se toca. `generar_corpus.py` sigue siendo la fuente de verdad de los cuatro
idiomas originales y de sus diez conceptos, y este módulo solo AÑADE. La
comprobación `verificar_nucleo()` debe seguir pasando después de importar
esto, y se ejecuta al final del fichero para dejarlo por escrito.

Sobre las lagunas. El corpus no está completo a propósito. Para algunas
parejas idioma-concepto no existe una única palabra corriente y neutra
—compiten dos formas de uso igual de frecuente— y en esos casos se deja el
hueco en lugar de elegir una al azar. Un hueco declarado es un dato; una
elección arbitraria no documentada es una invención. Esas lagunas son,
además, lo que hace que los conjuntos dejen de tener todos el mismo tamaño,
que es la condición que el ejercicio necesita.
"""
import sys

sys.path.insert(0, "/sessions/relaxed-keen-babbage/mnt/Curso_ciencia_de_datos/datos")
import generar_corpus                                     # noqa: E402

# Los veinte conceptos que se añaden a los diez del núcleo.
CONCEPTOS_NUEVOS = [
    "pan", "leche", "fuego", "tierra", "aire", "verde", "rojo", "blanco",
    "negro", "madre", "padre", "hijo", "gato", "perro", "árbol", "piedra",
    "río", "camino", "tiempo", "nombre",
]
CONCEPTOS_AMPLIADOS = generar_corpus.CONCEPTOS + CONCEPTOS_NUEVOS

# Las lagunas declaradas: parejas (idioma, concepto) sin entrada, con su
# motivo. Ninguna se deja en blanco por descuido.
LAGUNAS = {
    ("Alemán", "río"): "compiten Fluss y Strom sin una neutra clara",
    ("Alemán", "camino"): "compiten Weg y Straße según el sentido",
    ("Sueco", "camino"): "compiten väg y stig según el sentido",
    ("Sueco", "mar"): "hav y sjö se reparten el uso",
    ("Danés", "mar"): "hav y sø se reparten el uso",
    ("Neerlandés", "camino"): "compiten weg y pad",
    ("Rumano", "árbol"): "compiten copac y pom según el tipo",
    ("Gallego", "camino"): "compiten camiño y carreiro",
}

# Las palabras nuevas de los ocho idiomas que ya estaban, para los veinte
# conceptos nuevos. El orden es el de CONCEPTOS_NUEVOS.
NUEVAS_EN_IDIOMAS_EXISTENTES = {
    "Español": ["pan", "leche", "fuego", "tierra", "aire", "verde", "rojo",
                "blanco", "negro", "madre", "padre", "hijo", "gato", "perro",
                "árbol", "piedra", "río", "camino", "tiempo", "nombre"],
    "Inglés": ["bread", "milk", "fire", "earth", "air", "green", "red",
               "white", "black", "mother", "father", "son", "cat", "dog",
               "tree", "stone", "river", "road", "time", "name"],
    "Portugués": ["pão", "leite", "fogo", "terra", "ar", "verde", "vermelho",
                  "branco", "preto", "mãe", "pai", "filho", "gato", "cão",
                  "árvore", "pedra", "rio", "caminho", "tempo", "nome"],
    "Francés": ["pain", "lait", "feu", "terre", "air", "vert", "rouge",
                "blanc", "noir", "mère", "père", "fils", "chat", "chien",
                "arbre", "pierre", "rivière", "chemin", "temps", "nom"],
    "Italiano": ["pane", "latte", "fuoco", "terra", "aria", "verde", "rosso",
                 "bianco", "nero", "madre", "padre", "figlio", "gatto",
                 "cane", "albero", "pietra", "fiume", "cammino", "tempo",
                 "nome"],
    "Catalán": ["pa", "llet", "foc", "terra", "aire", "verd", "vermell",
                "blanc", "negre", "mare", "pare", "fill", "gat", "gos",
                "arbre", "pedra", "riu", "camí", "temps", "nom"],
    "Alemán": ["Brot", "Milch", "Feuer", "Erde", "Luft", "grün", "rot",
               "weiß", "schwarz", "Mutter", "Vater", "Sohn", "Katze", "Hund",
               "Baum", "Stein", None, None, "Zeit", "Name"],
    "Neerlandés": ["brood", "melk", "vuur", "aarde", "lucht", "groen", "rood",
                   "wit", "zwart", "moeder", "vader", "zoon", "kat", "hond",
                   "boom", "steen", "rivier", None, "tijd", "naam"],
}

# Los cuatro idiomas nuevos, con los treinta conceptos.
IDIOMAS_NUEVOS = {
    "Rumano": ["casă", "soare", "lună", "apă", "noapte", "mână", "carte",
               "floare", "mare", "lumină",
               "pâine", "lapte", "foc", "pământ", "aer", "verde", "roșu",
               "alb", "negru", "mamă", "tată", "fiu", "pisică", "câine",
               None, "piatră", "râu", "drum", "timp", "nume"],
    "Gallego": ["casa", "sol", "lúa", "auga", "noite", "man", "libro",
                "flor", "mar", "luz",
                "pan", "leite", "lume", "terra", "aire", "verde", "vermello",
                "branco", "negro", "nai", "pai", "fillo", "gato", "can",
                "árbore", "pedra", "río", None, "tempo", "nome"],
    "Sueco": ["hus", "sol", "måne", "vatten", "natt", "hand", "bok",
              "blomma", None, "ljus",
              "bröd", "mjölk", "eld", "jord", "luft", "grön", "röd", "vit",
              "svart", "mor", "far", "son", "katt", "hund", "träd", "sten",
              "flod", None, "tid", "namn"],
    "Danés": ["hus", "sol", "måne", "vand", "nat", "hånd", "bog", "blomst",
              None, "lys",
              "brød", "mælk", "ild", "jord", "luft", "grøn", "rød", "hvid",
              "sort", "mor", "far", "søn", "kat", "hund", "træ", "sten",
              "flod", "vej", "tid", "navn"],
}


def corpus_ampliado():
    """Devuelve el corpus completo como diccionario de conjuntos.

    Los cuatro idiomas del núcleo conservan sus diez palabras originales
    tal y como las devuelve `generar_corpus`, y se les añaden las nuevas.
    Ni una sola palabra histórica se reescribe aquí.
    """
    base = generar_corpus.corpus()          # ocho idiomas, diez conceptos
    completo = {}
    for nombre, palabras in base.items():
        nuevas = NUEVAS_EN_IDIOMAS_EXISTENTES.get(nombre, [])
        completo[nombre] = set(palabras) | {p for p in nuevas if p}
    for nombre, palabras in IDIOMAS_NUEVOS.items():
        completo[nombre] = {p for p in palabras if p}
    return completo


def tabla_de_conceptos():
    """Matriz idioma x concepto con la palabra o None si hay laguna."""
    base = generar_corpus.corpus()
    filas = {}
    for nombre in base:
        if nombre in IDIOMAS_NUEVOS:
            continue
        originales = generar_corpus.IDIOMAS_LIBRO_1.get(
            nombre, generar_corpus.IDIOMAS_AMPLIADOS.get(nombre))
        filas[nombre] = list(originales) + \
            NUEVAS_EN_IDIOMAS_EXISTENTES.get(nombre, [None] * 20)
    for nombre, palabras in IDIOMAS_NUEVOS.items():
        filas[nombre] = list(palabras)
    return filas


if __name__ == "__main__":
    print("Comprobación de que el núcleo histórico sigue intacto:")
    generar_corpus.verificar_nucleo()
    corpus = corpus_ampliado()
    print(f"\nIdiomas: {len(corpus)}   conceptos: {len(CONCEPTOS_AMPLIADOS)}")
    for nombre, palabras in corpus.items():
        print(f"  {nombre:>12}: {len(palabras):>3} palabras distintas")
    print(f"\nLagunas declaradas: {len(LAGUNAS)}")
