"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
import os
nombre_archivo = "files\input\data.csv"

def pregunta_09():
    if not os.path.exists(nombre_archivo):
        return {} 

    conteo_claves = {}
    
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as file:
        
        reader = csv.reader(file, delimiter='\t')
        
        for fila in reader:
            if len(fila) >= 5:
                diccionario_str = fila[4].strip()
                
                pares_clave_valor = diccionario_str.split(',')
                
                claves_en_registro = set()
                
                for par in pares_clave_valor:
                    partes = par.strip().split(':')
                    
                    if len(partes) >= 1:
                        clave = partes[0].strip() # Ej: 'jjj'
                        
                        if len(clave) == 3 and clave.isalpha() and clave not in claves_en_registro:
                            conteo_claves[clave] = conteo_claves.get(clave, 0) + 1
                            claves_en_registro.add(clave)
                            
    resultado_ordenado_lista = sorted(conteo_claves.items(), key=lambda item: item[0])
    resultado_ordenado_dict = dict(resultado_ordenado_lista)
    
    return resultado_ordenado_dict

respuesta = pregunta_09()

print("Rta/")
print(respuesta)
