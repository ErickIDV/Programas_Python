# Carga de Librerias 
import pandas as pd
import numpy as np
import argparse

# Crear un objeto de Parsing
parser = argparse.ArgumentParser(description="Generar un histograma de una distribucion normal")
parser.add_argument("media", help="Media de la distribucion normal")
parser.add_argument("desv", help="Desviacion estandar de la distribucion normal")
parser.add_argument("--n", default=100, type=int, help="Número de datos a generar")

args = parser.parse_args()

# Definición de parametros
n = int(args.n)
media = float(args.media)
desv = float(args.desv)

# Crear valores aleatorios
datos = np.random.normal(size=n, loc=media, scale=desv)
datos = datos.round(0).astype(int)

# Eliminar valores extremos 
datos_trim = []
for i in range(len(datos)):
    if datos[i] <= abs(media) + 2 * desv or datos[i] >= abs(media) - 2 * desv:
        datos_trim.append(datos[i])

# Transformar datos en un DataFrame 
datos_trim = pd.DataFrame(datos_trim)
datos_trim.columns = ['Datos']
hist_data = datos_trim.groupby(datos_trim['Datos']).size()

# Resumir informacion 
for i in range(len(hist_data)):
    if hist_data.index[i] >= 0:
        s = "+"
    else:
        s = ""
    print(
        s,
        hist_data.index[i],
        " " * (1 + len(str(np.max([np.max(hist_data.index), 
                                   abs(np.min(hist_data.index))]))) - 
               len(str(abs(hist_data.index[i])))),
        "*" * round(100 * hist_data.iloc[i] / len(datos_trim)),
        sep=""
    )