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

    lista += [elemento]
    return lista

'''
e: lista a la que se le quiere quitar el último elemento
s: el elemento eliminado (o None si está vacía)
r:
'''
def precario_pop(lista):

    if len_precario(lista) == 0:
        return None
    ultimo = lista[len_precario(lista)-1]
    nueva = []
    i = 0
    while i < len_precario(lista)-1:
        nueva += [lista[i]]
        i = i + 1
    i = 0
    while i < len_precario(nueva):
        lista[i] = nueva[i]
        i = i + 1
    while len_precario(lista) > len_precario(nueva):
        del lista[-1]
    return ultimo