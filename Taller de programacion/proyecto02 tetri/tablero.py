# tablero.py

from precario_utils import range_precario

def crear_tablero():
    """
    Crea el tablero con bordes y obstáculo central.
    """

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

            # Obstáculo central (como en el ejemplo del enunciado)
            elif (f == 6 and (c == 5 or c == 6)):
                fila += ["+"]

            else:
                fila += ["0"]
            c = c + 1
        tablero += [fila]
        f = f + 1
    return tablero



def imprimir_tablero(tablero):
    """
    Imprime el tablero en consola.
    """

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
