# archivo.py

def guardar_tablero(nombre_archivo, tablero):
    """
    Guarda el tablero en un archivo de texto.
    """
    archivo = open(nombre_archivo, "w")
    i = 0
    while i < len(tablero):
        fila = tablero[i]
        linea = ""
        j = 0
        while j < len(fila):
            linea = linea + str(fila[j])
            j = j + 1
        archivo.write(linea + "\n")
        i = i + 1
    archivo.close()

def cargar_tablero(nombre_archivo):
    """
    Carga el tablero desde un archivo de texto.
    """
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    tablero = []
    i = 0
    while i < len(lineas):
        linea = lineas[i]
        fila = []
        j = 0
        while j < len(linea.strip()):
            fila += [linea.strip()[j]]
            j = j + 1
        tablero += [fila]
        i = i + 1
    archivo.close()
    return tablero
