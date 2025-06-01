def len_chino(lista): #copia de len porque ajá
    # e: una lista
    # s: la longitud de la lista
    # r: 
    contador = 0
    for w in lista:
        contador += 1
    return contador

def append_chino(lista, elem): #copia de appedn
    # e: una lista y un elemento para meter
    # s: la lista con el elemento en cuestión al final
    # r: 
    lista += [elem]

def convertir_Hex_a_Dec(matriz):
    # e: una matriz con valores hexadecimales
    # s: una lista con los valores convertidos a decimal
    # r: los valores deben ser válidos en hexa
    res = []
    for fila in matriz:
        if not validar_vector_hexadecimal(fila):
            return "Error: la matriz contiene valores no válidos"
        append_chino(res, hexadecimal_a_decimal(fila))
    return res

def validar_vector_hexadecimal(vector):
    # e: un vector con posibles valores hexadecimales
    # s: verdadero si todos los valores son válidos, falso si no
    # r: 
    hexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for valor in vector:
        if not (es_numero(valor) or valor in hexa):
            return False
    return True

def hexadecimal_a_decimal(vector):
    # e: un vector con valores hexadecimales
    # s: el valor decimal equivalente
    # r: los valores deben ser válidos en hexadecimal
    decimal = 0
    potencia = len_chino(vector) - 1
    for valor in vector:
        decimal += valor_hexadecimal(valor) * potencia_chino(16, potencia)
        potencia -= 1
    return decimal

def valor_hexadecimal(caracter):
    # e: un caracter hexadecimal
    # s: el valor decimal del caracter
    # r: el caracter debe ser válido en hexa
    hexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    decimales = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    if es_numero(caracter):
        return caracter
    for i in range(len_chino(hexa)):
        if hexa[i] == caracter:
            return decimales[i]
    return -1

def potencia_chino(base, exponente):
    # e: una base y un exponente
    # s: el resultado de elevar la base al exponente
    # r:
    resultado = 1
    for w in range(exponente):
        resultado = resultado * base
    return resultado

def es_numero(valor):
    # e: un valor cualquiera
    # s: verdadero si el valor es un número entre 0 y 9
    # r: el valor debe ser un entero
    if isinstance(valor, int):
        return 0 <= valor <= 9
    return False

def matrizDiagonalInversa(matriz):
    # e: una matriz
    # s: una lista con los valores de la diagonal inversa
    # r: matriz debe ser cuadrada
    diagonal_inversa = []
    filas = len_chino(matriz)
    columnas = len_chino(matriz[0])
    for i in range(min(filas, columnas)):
        append_chino(diagonal_inversa, matriz[i][columnas - i - 1])
    return diagonal_inversa

def encontrarNumerosDivisibles(matriz, num):
    # e: una matriz y un número
    # s: una matriz con los valores divisibles por el número, los demás son 0
    # r: todos los vectores de la matriz deben tener el mismo tamaño
    if not validar_matriz(matriz):
        return "Error: existen vectores de diferente tamaño"
    resultado = []
    columnas = len_chino(matriz[0])
    filas = len_chino(matriz)
    for i in range(columnas):
        columna = []
        for j in range(filas):
            if matriz[j][i] % num == 0:
                append_chino(columna, matriz[j][i])
            else:
                append_chino(columna, 0)
        append_chino(resultado, columna)
    return resultado

def validar_matriz(matriz):
    # e: una matriz
    # s: verdadero si todos los vectores tienen el mismo tamaño
    # r: la matriz no debe estar vacía
    longitud = len_chino(matriz[0])
    for fila in matriz:
        if len_chino(fila) != longitud:
            return False
    return True
