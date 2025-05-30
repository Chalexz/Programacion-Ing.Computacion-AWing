# tablero.py

from precario_utils import range_precario

def crear_tablero():
    filas = 22
    columnas = 12
    tablero = []
    for i in range_precario(0, filas):
        fila = []
        for j in range_precario(0, columnas):
            if i == 0 or i == filas - 1 or j == 0 or j == columnas - 1:
                fila += ["+"]
            else:
                fila += ["0"]
        tablero += [fila]
    return tablero

def imprimir_tablero(tablero):
    for fila in tablero:
        txt = ""
        for celda in fila:
            txt += str(celda) + " "
        print(txt)
