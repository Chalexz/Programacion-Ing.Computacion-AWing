#                   hacer una funcion que corte una matriz 
'''
e: cualquier cosa a la que se le pueda aplicar len()
s: el num de elemnentos de ese algo
r: 
'''
def len_chino(entrada):
    contador = 0
    for w in entrada:
        contador += 1
    return contador
'''
e: lo que sea a lo que se le pueda aplicar .append y el elemento que se le va a añadir al final
s: la lista o cosa que metió en la entrada, con el elemento añadido al final 
r: 
'''
def append_chino(lista, elemento):
    lista += [elemento]
    return lista
'''
e: una lista
s: el largo de la lista
r: 
'''
def largo_lista(lista):
    return len_chino(lista)
'''
e: una matriz
s: un booleano dependiendo si la matriz de input es válida respecto a lo que se pidió
r: 
'''
def es_matriz_valida(matriz): #valida si hay filas en la matriz, valida si la matriz tiene valores enteros o flotantes, valida si es cuadrada 

    if not isinstance(matriz, list):
        return False
    filas = len_chino(matriz)
    if filas == 0:
        return False
    columnas = len_chino(matriz[0])
    for fila in matriz:
        if len_chino(fila) != columnas:
            return False
        for valor in fila:
            if not (isinstance(valor, int) or isinstance(valor, float)):
                return False
    return True

def cortarMatriz(matriz, fila, columna):
    if not es_matriz_valida(matriz):
        return "Error: matriz inválida"
    
    total_filas = len_chino(matriz)
    total_columnas = len_chino(matriz[0])

    if not (isinstance(fila, int) and isinstance(columna, int)):
        return "Error: los valores de fila y columna deben ser enteros"

    if fila < 0 or columna < 0:
        return "Error: los valores de fila y columna deben ser mayores a -1"

    if fila > total_filas or columna > total_columnas:
        return "Error: los valores de la nueva matriz exceden las dimensiones actuales"
    
    nueva_matriz = []
    for i in range(fila):
        nueva_fila = []
        for j in range(columna):
            nueva_fila = append_chino(nueva_fila, matriz[i][j])
        nueva_matriz = append_chino(nueva_matriz, nueva_fila)
    return nueva_matriz


matriz = [
    [2, 4, 6, 8, 10],
    [1, 3, 5, 7, 9],
    [4, 8, 12, 16, 20],
    [0, 0, 0, 0, 0],
    [5, 10, 5, 10, 5]
]


test_1 = cortarMatriz(matriz, 2, 3)
test_2 = cortarMatriz(matriz, 2, 2)
test_3 = cortarMatriz(matriz, 5, 5)
test_4 = cortarMatriz(matriz, 8, 5)

print(test_1)
