"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
import os
nombre_archivo = "files\input\data.csv"


def pregunta_08():
    if not os.path.exists(nombre_archivo):
        return f"Error: No se pudo encontrar el archivo '{nombre_archivo}'. Por favor, verifica la ruta."

    letras_unicas_por_valor = {}
    
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as file:
        
        reader = csv.reader(file, delimiter='\t')
        
        for fila in reader:
            if len(fila) >= 2:
                letra = fila[0].strip()     
                valor_str = fila[1].strip() 
                
                if letra and valor_str and letra.isalpha():
                    try:
                        valor_numerico = int(valor_str)
                        
                        if valor_numerico not in letras_unicas_por_valor:
                            letras_unicas_por_valor[valor_numerico] = set()
                            
                        letras_unicas_por_valor[valor_numerico].add(letra)
                        
                    except ValueError:
                        pass
            
    resultado = []
    for valor, set_letras in letras_unicas_por_valor.items():
        lista_letras = list(set_letras)
        lista_letras.sort()
        
        resultado.append((valor, lista_letras))
        
    resultado_ordenado = sorted(resultado, key=lambda item: item[0])
    
    return resultado_ordenado

