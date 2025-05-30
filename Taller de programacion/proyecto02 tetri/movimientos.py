# movimientos.py

from precario_utils import len_precario, range_precario

def puede_colocar(tablero, pieza, fila_inicio, col_inicio):
    alto = len_precario(pieza)
    ancho = len_precario(pieza[0])
    for i in range_precario(0, alto):
        for j in range_precario(0, ancho):
            if pieza[i][j] == 1:
                if tablero[fila_inicio + i][col_inicio + j] != "0":
                    return False
    return True

def colocar_pieza(tablero, pieza, fila_inicio, col_inicio):
    alto = len_precario(pieza)
    ancho = len_precario(pieza[0])
    for i in range_precario(0, alto):
        for j in range_precario(0, ancho):
            if pieza[i][j] == 1:
                tablero[fila_inicio + i][col_inicio + j] = "1"

def eliminar_lineas_completas(tablero):
    nuevas_filas = []
    puntos = 0
    for fila in tablero:
        if fila[0] == "+":
            nuevas_filas += [fila]
        else:
            llenos = 0
            for celda in fila:
                if celda == "1":
                    llenos += 1
            if llenos == 10:
                nueva = ["+"]
                for _ in range_precario(0, 10):
                    nueva += ["0"]
                nueva += ["+"]
                nuevas_filas = [nueva] + nuevas_filas
                puntos += 100
            else:
                nuevas_filas += [fila]
    return nuevas_filas, puntos

def rotar_pieza(pieza):
    filas = len_precario(pieza)
    columnas = len_precario(pieza[0])
    nueva = []
    for j in range_precario(0, columnas):
        fila = []
        for i in range_precario(0, filas):
            fila = [pieza[filas - i - 1][j]] + fila
        nueva += [fila]
    return nueva
