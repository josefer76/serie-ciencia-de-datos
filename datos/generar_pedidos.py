# -*- coding: utf-8 -*-
"""Reconstrucción documentada del dataset `pedidos.csv` del Libro 2, Sección 6.4.

El archivo original se generó durante la redacción del Libro 2 y no se conservó,
y aquel volumen no publicó su generador. Este script lo reconstruye reproduciendo
las características documentadas en el manuscrito del Libro 2:

  - 5 060 filas y 7 columnas.
  - 60 filas duplicadas exactas.
  - 7 variantes de escritura de la región sobre 4 regiones reales.
  - Precios unitarios negativos (imposibles en el dominio).
  - 15 pedidos con un número de unidades implausible (> 100).
  - Aproximadamente un 6.5 % de precios faltantes y faltantes en costo_envio.
  - Tras la limpieza documentada quedan unas 4 681 filas (92.5 %).
  - Ticket promedio por categoría del orden de 609 (Ropa) y 1 186 (Hogar).
  - Correlación en torno a 0.71 entre precio_unitario e ingreso.
  - Serie mensual con tendencia creciente y alta volatilidad.

A partir de aquí el hilo del taller queda reproducible: cualquier lector puede
regenerar el archivo y reproducir los resultados de los Capítulos 7 a 11.
"""
import numpy as np
import pandas as pd

SEMILLA = 20260809
N_FILAS_BASE = 5_000
N_DUPLICADOS = 60
DISPERSION_UNIDADES = 0.62

# --- Perfil de cada categoría -------------------------------------------------
# (peso en el número de pedidos, precio medio, dispersión del precio,
#  media de unidades, dispersión de unidades)
CATEGORIAS = {
    "Electrónica": dict(peso=0.28, precio_medio=560.0, precio_sigma=0.55,
                        unidades_media=6.0),
    "Hogar":       dict(peso=0.54, precio_medio=185.0, precio_sigma=0.45,
                        unidades_media=6.6),
    "Ropa":        dict(peso=0.18, precio_medio=33.0, precio_sigma=0.40,
                        unidades_media=18.5),
}
REGIONES_REALES = ["Norte", "Sur", "Este", "Oeste"]
# Variantes de escritura que la limpieza del Libro 2 normaliza a 4 regiones.
VARIANTES_REGION = {
    "Norte": ["Norte", "norte", " Norte"],
    "Sur": ["Sur", "SUR"],
    "Este": ["Este"],
    "Oeste": ["Oeste"],

}


def generar(semilla=SEMILLA):
    """Genera el dataset de pedidos con los problemas de calidad documentados."""
    generador = np.random.default_rng(semilla)

    categorias = list(CATEGORIAS)
    pesos = np.array([CATEGORIAS[c]["peso"] for c in categorias])
    asignadas = generador.choice(categorias, size=N_FILAS_BASE, p=pesos / pesos.sum())

    # Fechas sobre 24 meses, con tendencia creciente en el volumen de pedidos.
    calendario = pd.date_range("2023-01-01", "2024-12-31", freq="D")
    peso_temporal = np.linspace(0.88, 1.14, len(calendario))
    peso_temporal = peso_temporal / peso_temporal.sum()
    fechas = generador.choice(calendario, size=N_FILAS_BASE, p=peso_temporal)

    precios = np.empty(N_FILAS_BASE)
    unidades = np.empty(N_FILAS_BASE, dtype=int)
    for categoria in categorias:
        perfil = CATEGORIAS[categoria]
        seleccion = asignadas == categoria
        cuantos = int(seleccion.sum())
        precios[seleccion] = generador.lognormal(
            np.log(perfil["precio_medio"]) - perfil["precio_sigma"] ** 2 / 2,
            perfil["precio_sigma"], cuantos)
        # La dispersión adicional de las unidades es lo que sitúa la
        # correlación entre precio e ingreso en el 0.71 documentado.
        factor = generador.lognormal(-DISPERSION_UNIDADES ** 2 / 2,
                                     DISPERSION_UNIDADES, cuantos)
        unidades[seleccion] = np.minimum(1 + generador.poisson(
            np.maximum((perfil["unidades_media"] - 1) * factor, 0.1)), 100)

    regiones = generador.choice(REGIONES_REALES, size=N_FILAS_BASE,
                                p=[0.30, 0.26, 0.24, 0.20])
    regiones_escritas = np.array([
        generador.choice(VARIANTES_REGION[region]) for region in regiones])

    costo_envio = np.round(generador.uniform(3.0, 45.0, N_FILAS_BASE), 2)

    datos = pd.DataFrame({
        "pedido_id": np.arange(1, N_FILAS_BASE + 1),
        "fecha": fechas,
        "region": regiones_escritas,
        "categoria": asignadas,
        "unidades": unidades,
        "precio_unitario": np.round(precios, 2),
        "costo_envio": costo_envio,
    })

    # --- Problemas de calidad documentados en el Libro 2 ---------------------
    # 1. Quince pedidos con unidades implausibles.
    implausibles = generador.choice(N_FILAS_BASE, 15, replace=False)
    datos.loc[implausibles, "unidades"] = generador.integers(150, 900, 15)

    # 2. Precios negativos: error de signo en la carga.
    negativos = generador.choice(
        np.setdiff1d(np.arange(N_FILAS_BASE), implausibles), 48, replace=False)
    datos.loc[negativos, "precio_unitario"] *= -1

    # 3. Precios faltantes (6.5 % del total final).
    faltantes_precio = generador.choice(
        np.setdiff1d(np.arange(N_FILAS_BASE),
                     np.concatenate([implausibles, negativos])),
        330, replace=False)
    datos.loc[faltantes_precio, "precio_unitario"] = np.nan

    # 4. Faltantes en el costo de envío (variable secundaria).
    faltantes_envio = generador.choice(N_FILAS_BASE, 190, replace=False)
    datos.loc[faltantes_envio, "costo_envio"] = np.nan

    # 5. Sesenta filas duplicadas exactas, por un error de carga.
    duplicadas = datos.sample(N_DUPLICADOS, random_state=7)
    datos = pd.concat([datos, duplicadas], ignore_index=True)
    datos = datos.sample(frac=1.0, random_state=13).reset_index(drop=True)

    return datos


def limpiar(datos):
    """Aplica exactamente la limpieza documentada en el Libro 2, Sección 6.4."""
    limpio = datos.copy()
    limpio = limpio.drop_duplicates()
    limpio["region"] = limpio["region"].str.strip().str.lower().str.capitalize()
    limpio.loc[limpio["precio_unitario"] < 0, "precio_unitario"] = np.nan
    limpio = limpio[limpio["unidades"] <= 100]
    limpio = limpio.dropna(subset=["precio_unitario"])
    limpio["costo_envio"] = limpio["costo_envio"].fillna(
        limpio["costo_envio"].median())
    limpio["ingreso"] = limpio["precio_unitario"] * limpio["unidades"]
    return limpio


if __name__ == "__main__":
    crudo = generar()
    crudo.to_csv("pedidos.csv", index=False)

    limpio = limpiar(crudo)
    print(f"Filas en bruto      : {len(crudo)}")
    print(f"Duplicados exactos  : {crudo.duplicated().sum()}")
    print(f"Variantes de región : {crudo['region'].nunique()}")
    print(f"Precios negativos   : {(crudo['precio_unitario'] < 0).sum()}")
    print(f"Unidades > 100      : {(crudo['unidades'] > 100).sum()}")
    print(f"Faltantes precio    : {crudo['precio_unitario'].isna().mean():.2%}")
    print(f"\nFilas tras la limpieza: {len(limpio)} "
          f"({len(limpio) / len(crudo):.1%} del total)")

    print(f"\nTicket promedio por categoría:")
    resumen = limpio.groupby("categoria", observed=True).agg(
        pedidos=("ingreso", "size"),
        ingreso_total=("ingreso", "sum"),
        ticket_promedio=("ingreso", "mean"),
        unidades=("unidades", "sum"))
    resumen["cuota_ingreso"] = resumen["ingreso_total"] / resumen["ingreso_total"].sum()
    resumen["cuota_unidades"] = resumen["unidades"] / resumen["unidades"].sum()
    print(resumen.round(2).to_string())

    print(f"\nTicket promedio por región:")
    print(limpio.groupby("region", observed=True)["ingreso"].mean().round(2).to_string())

    correlacion = limpio["precio_unitario"].corr(limpio["ingreso"])
    print(f"\nCorrelación precio_unitario ~ ingreso: {correlacion:.4f}")

    mensual = limpio.set_index("fecha")["ingreso"].resample("MS").sum()
    print(f"Serie mensual: mínimo {mensual.min():,.0f}   "
          f"máximo {mensual.max():,.0f}   meses {len(mensual)}")
