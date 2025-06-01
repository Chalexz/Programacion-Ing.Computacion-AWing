# ranking basico con archivo

from precario_utils import len_precario

def guardar_ranking(nombre, puntos):
    """
    Guarda el nombre y puntos en el archivo ranking.txt
    """

    f = open("ranking.txt", "a")
    linea = nombre + "," + str(puntos) + "\n"
    f.write(linea)
    f.close()

def cargar_ranking():
    """
    Carga el ranking desde el archivo.
    """

    archivo = open("ranking.txt", "r")
    lineas = archivo.readlines()
    archivo.close()
    data = []
    i = 0
    while i < len_precario(lineas):
        l = lineas[i]
        partes = l.strip().split(",")
        nombre = partes[0]
        puntos = int(partes[1])
        data += [[nombre, puntos]]
        i = i + 1
    return data


def mostrar_ranking():
    """
    Muestra el ranking top 10.
    """

    top = cargar_ranking()
    i = 0
    while i < len_precario(top):
        j = i + 1
        while j < len_precario(top):
            if top[j][1] > top[i][1]:
                temp = top[i]
                top[i] = top[j]
                top[j] = temp
            j = j + 1
        i = i + 1

    print("====== LOS 10 MÁS SAICOS ======")
    n = 0
    while n < 10 and n < len_precario(top):
        jugador = top[n]
        print("#" + str(n+1), "-", jugador[0], ":", jugador[1], "puntos")
        n = n + 1
