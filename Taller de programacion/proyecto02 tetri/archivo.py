from precario_utils import len_precario 


def guardar_tablero(nombre_archivo, tablero):

    archivo = open(nombre_archivo, "w")
    i = 0
    while i < len_precario(tablero):
        fila = tablero[i]
        linea = ""
        j = 0


        while j < len_precario(fila):
            linea = linea + str(fila[j])
            j = j + 1
        archivo.write(linea + "\n")
        i = i + 1

    archivo.close()

def cargar_tablero(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    
    lineas = archivo.readlines()
    tablero = []
    i = 0
    while i < len_precario(lineas):
        linea = lineas[i]

        fila = []
        j = 0
        while j < len_precario(linea.strip()):
            fila += [linea.strip()[j]]
            j = j + 1
        tablero += [fila]
        i = i + 1
    archivo.close()
    return tablero
