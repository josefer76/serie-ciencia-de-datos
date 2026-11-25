"""Genera pedidos_tienda.csv: datos sintéticos de la tienda de Doña Marta.

Libro 1, Capítulo 8 (taller integrador). Los datos no pertenecen a ninguna
empresa ni persona: los crea este programa con una semilla fija, de modo que
cualquiera que lo ejecute obtiene exactamente el mismo archivo.

Además de los pedidos normales, el programa introduce a propósito los
problemas típicos de los datos reales, para practicar su limpieza:
  - pedidos anotados dos veces (mismo código),
  - ciudades escritas de varias formas,
  - precios en formato colombiano ("$ 45.000"), vacíos, negativos o con texto,
  - cantidades imposibles (0) o muy raras (250).
"""
import csv
import random

SEMILLA = 20261125
NUMERO_PEDIDOS = 60

PRODUCTOS = {
    # producto: (categoria, precio en pesos)
    "camisa": ("ropa", 45000),
    "jean": ("ropa", 120000),
    "chaqueta": ("ropa", 230000),
    "medias": ("ropa", 15000),
    "gorra": ("ropa", 35000),
    "sarten": ("hogar", 89000),
    "olla": ("hogar", 75000),
    "toalla": ("hogar", 32000),
    "cojin": ("hogar", 28000),
    "audifonos": ("electronica", 150000),
    "cargador": ("electronica", 45000),
    "parlante": ("electronica", 210000),
}
PROBABILIDAD_DEVOLUCION = {"ropa": 0.25, "hogar": 0.05, "electronica": 0.10}
CIUDADES = ["bogota", "medellin", "cali", "cartagena", "barranquilla"]
CLIENTES = ["ana", "luis", "marta", "pedro", "sofia", "carlos", "diana",
            "jorge", "lucia", "andres", "paula", "felipe"]
FORMAS_DE_ESCRIBIR = {
    "bogota": ["Bogotá", " BOGOTA", "bogota "],
    "medellin": ["Medellín", "MEDELLIN", "medellín "],
    "cali": ["Cali", " CALI"],
    "cartagena": ["Cartagena", "CARTAGENA "],
    "barranquilla": ["Barranquilla", "barranquilla"],
}


def generar_pedidos():
    """Devuelve la lista de pedidos (diccionarios de textos) con errores."""
    generador = random.Random(SEMILLA)
    pedidos = []
    for numero in range(1, NUMERO_PEDIDOS + 1):
        producto = generador.choice(list(PRODUCTOS))
        categoria, precio = PRODUCTOS[producto]
        ciudad = generador.choice(CIUDADES)
        mes = generador.randint(1, 6)
        dia = generador.randint(1, 28)
        devuelto = generador.random() < PROBABILIDAD_DEVOLUCION[categoria]
        precio_texto = (f"$ {precio:,}".replace(",", ".")
                        if generador.random() < 0.5 else str(precio))
        pedidos.append({
            "codigo": f"P{numero:03d}",
            "fecha": f"2026-{mes:02d}-{dia:02d}",
            "cliente": generador.choice(CLIENTES),
            "ciudad": generador.choice(FORMAS_DE_ESCRIBIR[ciudad]),
            "categoria": categoria,
            "producto": producto,
            "precio": precio_texto,
            "cantidad": str(generador.randint(1, 4)),
            "devuelto": "si" if devuelto else "no",
        })

    # Errores de digitación en algunos pedidos.
    pedidos[6]["precio"] = ""
    pedidos[17]["precio"] = "-45000"
    pedidos[29]["precio"] = "consultar"
    pedidos[41]["precio"] = ""
    pedidos[52]["precio"] = "-89000"
    pedidos[11]["cantidad"] = "0"
    pedidos[36]["cantidad"] = "250"

    # Pedidos anotados dos veces al exportar.
    for posicion in [3, 15, 27, 44]:
        pedidos.append(dict(pedidos[posicion]))
    generador.shuffle(pedidos)
    return pedidos


def main():
    """Escribe pedidos_tienda.csv en la carpeta actual."""
    pedidos = generar_pedidos()
    with open("pedidos_tienda.csv", "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=list(pedidos[0]))
        escritor.writeheader()
        escritor.writerows(pedidos)
    print(f"Escritas {len(pedidos)} filas en pedidos_tienda.csv")


if __name__ == "__main__":
    main()
