# precario_utils.py

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
