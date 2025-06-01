from precario_utils import range_precario

def crear_tablero():
    tablero = []


    filas = 22

    columnas = 12

    f = 0
    while f < filas:
        fila = []
        c = 0
        while c < columnas:
            if f == 0 or f == filas - 1 or c == 0 or c == columnas - 1:
                fila += ["+"]
            elif (f == 6 and (c == 5 or c == 6)):
                fila += ["+"]
            elif f == filas - 2:
                # Penúltima fila: solo '0' o '+' (bordes)
                if c == 0 or c == columnas - 1:
                    fila += ["+"]
                else:
                    fila += ["0"]
            else:
                fila += ["0"]
            c = c + 1
        tablero += [fila]
        f = f + 1
    return tablero






def imprimir_tablero(tablero):
    i = 0
    while i < range_precario(0, len(tablero)):
        fila = tablero[i]
        txt = ""
        j = 0


        while j < range_precario(0, len(fila)):
            txt = txt + str(fila[j]) + " "
            j = j + 1
        print(txt)

        i = i + 1
