"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
import os
nombre_archivo = "files\input\data.csv"

def pregunta_03():
    if not os.path.exists(nombre_archivo):
        return f"Error: No se pudo encontrar el archivo '{nombre_archivo}'. Por favor, verifica la ruta."

    suma_por_letra = {}
    
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as file:
        
        reader = csv.reader(file, delimiter='\t')
        
        for fila in reader:
            if len(fila) >= 2:
                letra = fila[0].strip()  
                valor_str = fila[1].strip() 
                
                if letra and valor_str and letra.isalpha():
                    try:
                        valor_numerico = float(valor_str)
                        
                        suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor_numerico
                        
                    except ValueError:
                        pass 
            
    lista_tuplas = list(suma_por_letra.items())
    
    lista_tuplas_ordenada = sorted(lista_tuplas, key=lambda item: item[0])
    
    resultado_final = [(letra, int(round(suma))) for letra, suma in lista_tuplas_ordenada]
    
    return resultado_final


