"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
import os
nombre_archivo = "files\input\data.csv"


def pregunta_06():
    if not os.path.exists(nombre_archivo):
        return f"Error: No se pudo encontrar el archivo '{nombre_archivo}'. Por favor, verifica la ruta."

    min_max_por_clave = {}

    MIN_INICIAL = float('inf')
    MAX_INICIAL = -float('inf')

    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as file:
        
        reader = csv.reader(file, delimiter='\t')
        
        for fila in reader:
            if len(fila) >= 5:
                diccionario_str = fila[4].strip()
                
                pares_clave_valor = diccionario_str.split(',')
                
                for par in pares_clave_valor:
                    partes = par.strip().split(':')
                    
                    if len(partes) == 2:
                        clave = partes[0].strip() 
                        valor_str = partes[1].strip() 
                        
                        try:
                            valor_numerico = int(valor_str)
                            
                            if clave not in min_max_por_clave:
                                min_max_por_clave[clave] = {'min': MIN_INICIAL, 'max': MAX_INICIAL}
                                
                            if valor_numerico < min_max_por_clave[clave]['min']:
                                min_max_por_clave[clave]['min'] = valor_numerico
                                
                            if valor_numerico > min_max_por_clave[clave]['max']:
                                min_max_por_clave[clave]['max'] = valor_numerico
                                
                        except ValueError:
                            continue 
            
    resultado = []
    
    for clave, valores in min_max_por_clave.items():
        if valores['min'] != MIN_INICIAL and valores['max'] != MAX_INICIAL:
            resultado.append((clave, valores['min'], valores['max']))
            
    resultado_ordenado = sorted(resultado, key=lambda item: item[0])
    
    return resultado_ordenado

