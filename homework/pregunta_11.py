"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
import os
nombre_archivo = "files/input/data.csv"

def pregunta_11():
    if not os.path.exists(nombre_archivo):
        return {} 

    suma_por_letra_col4 = {}
    
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as file:
        
        reader = csv.reader(file, delimiter='\t')
        
        for fila in reader:
            if len(fila) >= 4:
                valor_str = fila[1].strip()      
                letras_str = fila[3].strip()    
                
                try:
                    valor_numerico = int(valor_str)
                except ValueError:
                    continue
                
                if letras_str:
                    letras = letras_str.split(',')
                    
                    for letra in letras:
                        letra_limpia = letra.strip()
                        
                        if letra_limpia.isalpha():
                            suma_por_letra_col4[letra_limpia] = suma_por_letra_col4.get(letra_limpia, 0) + valor_numerico
                            
    resultado_ordenado_lista = sorted(suma_por_letra_col4.items(), key=lambda item: item[0])
    resultado_ordenado_dict = dict(resultado_ordenado_lista)
    
    return resultado_ordenado_dict

