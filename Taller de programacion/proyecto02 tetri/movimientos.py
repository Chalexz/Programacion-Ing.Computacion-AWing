from precario_utils import len_precario, range_precario

def puede_colocar(tablero, pieza, fila_inicio, col_inicio):
    """
    Revisa si se puede poner la pieza en el tablero en la posición dada.
    Entradas: tablero, pieza, fila_inicio, col_inicio
    Salida: True si se puede, False si no
    Restricciones: No usar funciones avanzadas
    """
    alto = len_precario(pieza)
    ancho = len_precario(pieza[0])
    filas_tablero = len_precario(tablero)
    columnas_tablero = len_precario(tablero[0])

    for i in range_precario(0, alto):
        for j in range_precario(0, ancho):
            if pieza[i][j] != "0":
                fila_real = fila_inicio + i
                col_real = col_inicio + j
                if fila_real < 0 or fila_real >= filas_tablero:
                    return False
                if col_real < 0 or col_real >= columnas_tablero:
                    return False
                if tablero[fila_real][col_real] != "0":
                    return False
    return True

def colocar_pieza(tablero, pieza, fila_inicio, col_inicio):
    """
    Coloca la pieza en el tablero en la posición dada.
    """
    alto = len_precario(pieza)
    ancho = len_precario(pieza[0])
    for i in range_precario(0, alto):
        for j in range_precario(0, ancho):
            if pieza[i][j] != "0":
                tablero[fila_inicio + i][col_inicio + j] = pieza[i][j]

def eliminar_lineas_completas(tablero):
    """
    Si una fila empieza y termina con '+' y NO tiene ningún '0' en el medio,
    entonces esa fila está llena y debe ser limpiada (solo los bordes quedan '+').
    Devuelve (nuevo_tablero, puntos).
    """
    nuevas_filas = []
    puntos = 0
    for fila in tablero:
        if fila[0] == "+" and fila[len_precario(fila)-1] == "+":
            llena = True
            for k in range_precario(1, len_precario(fila)-1):
                if fila[k] == "0":
                    llena = False
            if llena:
                nueva = []
                for k in range_precario(0, len_precario(fila)):
                    if k == 0 or k == len_precario(fila)-1:
                        nueva += ["+"]

def rotar_pieza(pieza):
    filas = len_precario(pieza)
    columnas = len_precario(pieza[0])
    nueva = []
    for j in range_precario(0, columnas):
        fila = []
        for i in range_precario(0, filas):
            fila += [pieza[filas - 1 - i][j]]
        nueva += [fila]
    return nueva