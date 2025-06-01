# precario_utils.py

import time

def len_precario(lista):
    contador = 0
    for _ in lista:
        contador += 1
    return contador

def range_precario(inicio, fin):
    lista = []
    actual = inicio
    while actual < fin:
        lista += [actual]
        actual += 1
    return lista

def copiar_matriz(matriz):
    copia = []
    for fila in matriz:
        nueva = []
        for val in fila:
            nueva += [val]
        copia += [nueva]
    return copia

def random_precario(lista): #entiendo que sí se puede usar .time porque de alguna forma había que hacer un random pseudoaleatorio casero
    total = len_precario(lista)
    semilla = int(time.time() * 1000) % 10000
    posicion = semilla % total
    return lista[posicion]

def append_precario(lista, elemento):
    """
    Agrega un elemento al final de una lista (versión precaria de append).
    """
    lista += [elemento]
    return lista