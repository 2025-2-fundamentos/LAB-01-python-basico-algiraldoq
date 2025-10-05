"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
import os
nombre_archivo = "files\input\data.csv"


def pregunta_10():
    if not os.path.exists(nombre_archivo):
        return f"Error: No se pudo encontrar el archivo '{nombre_archivo}'. Por favor, verifica la ruta."

    resultado = []
    
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as file:
        
        reader = csv.reader(file, delimiter='\t')
        
        for fila in reader:
            if len(fila) >= 5:
                letra = fila[0].strip()     
                columna4_str = fila[3].strip() 
                columna5_str = fila[4].strip()
                
                cantidad_col4 = 0
                if columna4_str:
                    cantidad_col4 = len(columna4_str.split(','))
                
                cantidad_col5 = 0
                if columna5_str:
                    cantidad_col5 = len(columna5_str.split(','))

                resultado.append((letra, cantidad_col4, cantidad_col5))
            
    return resultado
