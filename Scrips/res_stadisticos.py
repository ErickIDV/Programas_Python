#carga las librerias necesarias
import pandas as pd
import argparse 

#crear un parser y definir un parametro que corresponde al nombre de un archivo 
parser = argparse.ArgumentParser()
parser.add_argument("file",type=str)

#leer el archivo csv y guardarlo en un dataframe
args = parser.parse_args() 
file = args.file

#cargar el archivo csv en un dataframe
datos = pd.read_csv(file, header=None)

serie = datos.iloc[:,0] #extraer la primera columna del dataframe

n = serie.count() #contar el número de elementos en la serie
prom = serie.mean() #calcular la media de la serie
med = serie.median() #calcular la mediana de la serie
q1 = serie.quantile(0.25) #calcular el primer cuartil de la serie
q3 = serie.quantile(0.75) #calcular el tercer cuartil de la serie
iqr = q3 - q1 #calcular el rango intercuartil de la serie

resumen = pd.DataFrame({
    'n': [n],
    'prom': [prom],
    'med': [med],
    'q1': [q1],
    'q3': [q3],
    'iqr': [iqr]
}, index=['Resumen']) #crear un dataframe con los resultados

print(resumen) #imprimir el dataframe con los resultados

#"https://raw.githubusercontent.com/jsaraujott/datos/main/datos.csv"