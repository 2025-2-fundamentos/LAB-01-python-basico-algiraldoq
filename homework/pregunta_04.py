"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
import os
nombre_archivo = "files/input/data.csv"


def pregunta_04():
    if not os.path.exists(nombre_archivo):
        return f"Error: No se pudo encontrar el archivo '{nombre_archivo}'. Por favor, verifica la ruta."

    conteo_meses = {}
    
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as file:
        
        reader = csv.reader(file, delimiter='\t')
        
        for fila in reader:
            if len(fila) >= 3:
                fecha_str = fila[2].strip() 
                
                if len(fecha_str) >= 7 and fecha_str[4] == '-' and fecha_str[7] == '-':
                    mes = fecha_str[5:7] 
                    
                    if mes.isdigit():
                        conteo_meses[mes] = conteo_meses.get(mes, 0) + 1
                        
    lista_tuplas = list(conteo_meses.items())
    
    lista_tuplas_ordenada = sorted(lista_tuplas, key=lambda item: item[0])
    
    return lista_tuplas_ordenada

