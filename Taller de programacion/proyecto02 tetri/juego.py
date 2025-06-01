from tablero import crear_tablero, imprimir_tablero

from tetrominos import obtener_tetrominos

from movimientos import colocar_pieza, puede_colocar, eliminar_lineas_completas, rotar_pieza

from precario_utils import len_precario, random_precario, range_precario

def iniciar_juego():
    print("Bienvenudo a TetrisKInter")

    tablero = crear_tablero()
    piezas = obtener_tetrominos()
    puntos = 0

    juego_activo = True
    while juego_activo:
        pieza = random_precario(piezas)
        fila = 1
        col = 4

        if not puede_colocar(tablero, pieza, fila, col):
            print("Quéee maaaloooo, perdió. Una pieza tocó el cielo")
            juego_activo = False
            break

        colocar_pieza(tablero, pieza, fila, col)
        imprimir_tablero(tablero)

        movimiento = ""
        while movimiento != "colocar":
            print("Mover con a=izq, d=der, s=abajo, w=rotar, x=colocar")
            movimiento = input("Movimiento: ")

            i = 0
            while i < len_precario(pieza):
                j = 0
                while j < len_precario(pieza[0]):
                    
                    if pieza[i][j] == 1:
                        tablero[fila + i][col + j] = "0"
                    j = j + 1

                i = i + 1

            if movimiento == "a":
                if puede_colocar(tablero, pieza, fila, col - 1):
                    col = col - 1
                    
            elif movimiento == "d":
                if puede_colocar(tablero, pieza, fila, col + 1):
                    col = col + 1
            elif movimiento == "s":
                if puede_colocar(tablero, pieza, fila + 1, col):
                    fila = fila + 1
            elif movimiento == "w":
                rotada = rotar_pieza(pieza)

                if puede_colocar(tablero, rotada, fila, col):
                    pieza = rotada

            elif movimiento == "x":
                break

            colocar_pieza(tablero, pieza, fila, col)
            imprimir_tablero(tablero)

        tablero, ganados = eliminar_lineas_completas(tablero)
        puntos = puntos + ganados
        
        print("Puntos:", puntos)
