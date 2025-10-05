"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
import os
nombre_archivo = "files/input/data.csv"


def pregunta_01():

    if not os.path.exists(nombre_archivo):
        return f"Error: No se pudo encontrar el archivo '{nombre_archivo}'. Por favor, verifica la ruta."

    suma_total = 0
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as file:
        
        reader = csv.reader(file, delimiter='\t')
        
        for fila in reader:
            if len(fila) > 1:
                try:
                    valor = fila[1].strip()
                    suma_total += float(valor) 
                except ValueError:
                    print(f"Advertencia: El valor '{fila[1]}' en la segunda columna no es numérico y fue omitido.")
                except IndexError:
                    continue

    return suma_total


