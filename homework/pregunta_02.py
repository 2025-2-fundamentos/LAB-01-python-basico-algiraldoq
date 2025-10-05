"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
import os

nombre_archivo = "files\input\data.csv"

def pregunta_02():
    if not os.path.exists(nombre_archivo):
        return f"Error: No se pudo encontrar el archivo '{nombre_archivo}'. Por favor, verifica la ruta."

    conteo_letras = {}

    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as file:

        reader = csv.reader(file, delimiter='\t')

        for fila in reader:
            if fila:
                letra = fila[0].strip()
                
                if len(letra) == 1 and letra.isalpha():
                    conteo_letras[letra] = conteo_letras.get(letra, 0) + 1
        
    lista_tuplas = list(conteo_letras.items())

    lista_tuplas_ordenada = sorted(lista_tuplas, key=lambda item: item[0])

    return lista_tuplas_ordenada

if __name__ == "__main__":
    resultado = pregunta_02()
    print("Rta/")
    print(resultado)
