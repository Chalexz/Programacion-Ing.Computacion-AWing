# juego.py

from tablero import crear_tablero, imprimir_tablero
from tetrominos import obtener_tetrominos
from movimientos import colocar_pieza, puede_colocar, eliminar_lineas_completas, rotar_pieza
from precario_utils import len_precario

def iniciar_juego():
    tablero = crear_tablero()
    piezas = obtener_tetrominos()
    pieza_actual = piezas[4]  # T por ejemplo
    fila = 1
    columna = 4
    if puede_colocar(tablero, pieza_actual, fila, columna):
        colocar_pieza(tablero, pieza_actual, fila, columna)
    else:
        print("¡Juego terminado!")

    imprimir_tablero(tablero)
    tablero, puntos = eliminar_lineas_completas(tablero)
    print("Puntos obtenidos:", puntos)
