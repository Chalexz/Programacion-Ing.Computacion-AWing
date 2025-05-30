# archivo.py
# Guardar y cargar el tablero desde archivo .txt

def guardar_tablero(nombre_archivo, tablero):
    archivo = open(nombre_archivo, "w")
    for fila in tablero:
        linea = ""
        for celda in fila:
            linea += str(celda)
        archivo.write(linea + "\\n")
    archivo.close()

def cargar_tablero(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    tablero = []
    for linea in lineas:
        fila = []
        for caracter in linea.strip():
            fila += [caracter]
        tablero += [fila]
    archivo.close()
    return tablero
