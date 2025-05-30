from auxi import contar_asientos_ocupados, contar_asientos_libres, crear_matriz_asientos

'''
e: id de sala y lista de salas
s: retorna la sala con ese id o None si no existe
r: salas debe ser una lista de salas con id en la posición 4
'''
def buscar_sala_por_id(sala_id, salas):
    for sala in salas:
        if sala[4] == sala_id:
            return sala
    return None

'''
e: sala, fila y columna
s: reserva el asiento si está libre, retorna True si lo logra
r: asiento debe existir
'''
def reservar_asiento(sala, fila, columna):
    matriz = sala[2]
    if matriz[fila][columna] == " ":
        matriz[fila][columna] = "X"
        sala[3] += 1
        return True
    return False

'''
e: sala, fila y columna
s: cancela la reserva si está ocupado, retorna True si lo logra
r: asiento debe existir
'''
def cancelar_asiento(sala, fila, columna):
    matriz = sala[2]
    if matriz[fila][columna] == "X":
        matriz[fila][columna] = " "
        sala[3] -= 1
        return True
    return False

'''
e: sala y cantidad de asientos
s: reserva cantidad de asientos consecutivos en cualquier fila, retorna tupla con info o None
r: cantidad > 0
'''
def reservar_consecutivos(sala, cantidad):
    matriz = sala[2]
    for i, fila in enumerate(matriz):
        consecutivos = 0
        inicio = 0
        for j, asiento in enumerate(fila):
            if asiento == " ":
                if consecutivos == 0:
                    inicio = j
                consecutivos += 1
                if consecutivos == cantidad:
                    for k in range(inicio, inicio + cantidad):
                        fila[k] = "X"
                    sala[3] += cantidad
                    return (i, inicio, inicio + cantidad - 1)
            else:
                consecutivos = 0
    return None

'''
e: sala y porcentaje (1-100)
s: reserva aleatoriamente el porcentaje de asientos en la sala, retorna cuántos reservó
r: porcentaje entre 1 y 100
'''
def simular_venta_masiva(sala, porcentaje):
    matriz = sala[2]
    total = len(matriz) * len(matriz[0])
    objetivo = int((porcentaje / 100) * total)
    ocupados = contar_asientos_ocupados(matriz)
    a_reservar = max(0, objetivo - ocupados)
    libres = []
    for i, fila in enumerate(matriz):
        for j, asiento in enumerate(fila):
            if asiento == " ":
                libres.append((i, j))
    import random
    random.shuffle(libres)
    for idx in range(min(a_reservar, len(libres))):
        i, j = libres[idx]
        matriz[i][j] = "X"
    sala[3] = contar_asientos_ocupados(matriz)
    return min(a_reservar, len(libres))

'''
e: sala
s: reinicia todos los asientos a libres y el contador de vendidos
r: sala debe tener matriz de asientos
'''
def reiniciar_sala(sala):
    filas = len(sala[2])
    columnas = len(sala[2][0])
    sala[2] = crear_matriz_asientos(filas, columnas)
    sala[3] = 0

'''
e: sala, fila y cantidad
s: reserva cantidad de asientos consecutivos en una fila específica, retorna tupla o None
r: fila válida, cantidad > 0
'''
def reservar_consecutivos_en_fila(sala, fila, cantidad):
    matriz = sala[2]
    if fila < 0 or fila >= len(matriz):
        return None
    fila_asientos = matriz[fila]
    consecutivos = 0
    inicio = 0
    for j, asiento in enumerate(fila_asientos):
        if asiento == " ":
            if consecutivos == 0:
                inicio = j
            consecutivos += 1
            if consecutivos == cantidad:
                for k in range(inicio, inicio + cantidad):
                    fila_asientos[k] = "X"
                sala[3] += cantidad
                return (inicio, inicio + cantidad - 1)
        else:
            consecutivos = 0
    return None

