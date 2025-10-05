"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
import os
nombre_archivo = "files\input\data.csv"


def pregunta_05():
    if not os.path.exists(nombre_archivo):
        return f"Error: No se pudo encontrar el archivo '{nombre_archivo}'. Por favor, verifica la ruta."

    min_max_por_letra = {}
    
    MIN_INICIAL = float('inf')
    MAX_INICIAL = -float('inf')

    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as file:
        
        reader = csv.reader(file, delimiter='\t')
        
        for fila in reader:
            if len(fila) >= 2:
                letra = fila[0].strip()     
                valor_str = fila[1].strip() 
                
                if letra and valor_str and letra.isalpha():
                    try:
                        valor_numerico = int(valor_str)
                        
                        if letra not in min_max_por_letra:
                            min_max_por_letra[letra] = {'min': MIN_INICIAL, 'max': MAX_INICIAL}
                            
                        if valor_numerico < min_max_por_letra[letra]['min']:
                            min_max_por_letra[letra]['min'] = valor_numerico
                            
                        if valor_numerico > min_max_por_letra[letra]['max']:
                            min_max_por_letra[letra]['max'] = valor_numerico
                            
                    except ValueError:
                        pass
            
    resultado = []
    
    for letra, valores in min_max_por_letra.items():
        if valores['min'] != MIN_INICIAL and valores['max'] != MAX_INICIAL:
            resultado.append((letra, valores['max'], valores['min']))
            
    resultado_ordenado = sorted(resultado, key=lambda item: item[0])
    
    return resultado_ordenado

respuesta = pregunta_05()

print("Rta/")
print(respuesta)
