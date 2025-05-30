'''
e: filas y columnas
s: retorna una matriz de asientos vacíos
r: filas y columnas > 0
'''
def crear_matriz_asientos(filas, columnas):
    return [[" " for _ in range(columnas)] for _ in range(filas)]

'''
e: matriz de asientos
s: retorna la cantidad de asientos ocupados
r: matriz válida
'''
def contar_asientos_ocupados(matriz):
    ocupados = 0
    for fila in matriz:
        for asiento in fila:
            if asiento == "X":
                ocupados += 1
    return ocupados

'''
e: matriz de asientos
s: retorna la cantidad de asientos libres
r: matriz válida
'''
def contar_asientos_libres(matriz):
    libres = 0
    for fila in matriz:
        for asiento in fila:
            if asiento == " ":
                libres += 1
    return libres

'''
e: matriz de asientos
s: retorna el total de asientos
r: matriz válida
'''
def total_asientos(matriz):
    return len(matriz) * len(matriz[0]) if matriz else 0

