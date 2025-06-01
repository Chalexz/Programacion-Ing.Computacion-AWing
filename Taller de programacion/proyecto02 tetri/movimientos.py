from precario_utils import len_precario, range_precario

def puede_colocar(tablero, pieza, fila_inicio, col_inicio):
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
    alto = len_precario(pieza)
    ancho = len_precario(pieza[0])
    for i in range_precario(0, alto):
        for j in range_precario(0, ancho):
            if pieza[i][j] != "0":
                tablero[fila_inicio + i][col_inicio + j] = pieza[i][j]

def eliminar_lineas_completas(tablero):
    nuevas_filas = []
    puntos = 0
    
    filas = len_precario(tablero)
    columnas = len_precario(tablero[0])
    i = filas - 2
    while i > 0:
        fila = tablero[i]
        if fila[0] == "+" and fila[len_precario(fila)-1] == "+":
            solo_pared = True
            for k in range_precario(1, len_precario(fila)-1):
                if fila[k] != "+":
                    solo_pared = False
            if solo_pared:
                i -= 1
                continue
            llena = True


            for k in range_precario(1, len_precario(fila)-1):
                if fila[k] == "0" or fila[k] == "+":
                    llena = False
            if llena:
                puntos += 100
                j = i
                while j > 1:
                    k = 1
                    while k < columnas - 1:
                        tablero[j][k] = tablero[j-1][k]
                        k = k + 1
                    j = j - 1
                k = 1
                while k < columnas - 1:
                    tablero[1][k] = "0"
                    k = k + 1
                continue
        i -= 1
    return tablero, puntos

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