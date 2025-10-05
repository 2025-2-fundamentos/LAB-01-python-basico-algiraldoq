"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
import os
nombre_archivo = "files\input\data.csv"

def pregunta_12():
    if not os.path.exists(nombre_archivo):
        return {} 

    suma_col5_por_letra_col1 = {}
    
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as file:
        
        reader = csv.reader(file, delimiter='\t')
        
        for fila in reader:
            if len(fila) >= 5:
                letra = fila[0].strip()          
                diccionario_str = fila[4].strip()
                
                suma_registro = 0
                
                if diccionario_str:
                    pares_clave_valor = diccionario_str.split(',')
                    
                    for par in pares_clave_valor:
                        partes = par.strip().split(':')
                        
                        if len(partes) == 2:
                            valor_str = partes[1].strip()
                            
                            try:
                                suma_registro += int(valor_str)
                            except ValueError:
                                continue
                
                if letra.isalpha():
                    suma_col5_por_letra_col1[letra] = suma_col5_por_letra_col1.get(letra, 0) + suma_registro
                            
    resultado_ordenado_lista = sorted(suma_col5_por_letra_col1.items(), key=lambda item: item[0])
    resultado_ordenado_dict = dict(resultado_ordenado_lista)
    
    return resultado_ordenado_dict

respuesta = pregunta_12()

print("Rta/")
print(respuesta)
