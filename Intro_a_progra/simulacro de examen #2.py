#           simulacro de examen hecho el día 6/5/2025 | Alexander Wing Rojas

 #                                  INCOMPLETO
'''
def maximas_secuencias(lista):
    maxima_secuencia = []
    secuencia_actual = []
    varias_secuencias_maximas = []
    for i in lista:
        if secuencia_actual == []:
            secuencia_actual = [i]
        elif i > secuencia_actual[-1]:
            secuencia_actual = secuencia_actual + [i]
        else:
            if i == secuencia_actual[-1] or i < secuencia_actual[-1]:
                secuencia_actual = []
                secuencia_actual = [i]
        if len(secuencia_actual) > len(maxima_secuencia):
            maxima_secuencia = secuencia_actual
        else:
            if len(secuencia_actual) == len(maxima_secuencia):
                varias_secuencias_maximas = [maxima_secuencia] + [secuencia_actual]
            if len(secuencia_actual) > varias_secuencias_maximas[-1]:
                varias_secuencias_maximas = [maxima_secuencia] + [secuencia_actual]
                

    return maxima_secuencia

print(maximas_secuencias([1, 2, 3, 0, 1, 2, 3, 4, 0, 1, 2, 3, 55]))
'''
'''
matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]
'''



def suma_fila(fila):
    result = 0
    for x in fila:
        result += x
        
    return result

def suma_columna(fila):
    result = 0
    for fila[0] in fila:
        result += fila[0]
    return result
        
def suma_diagonal(matriz):
    result = 0

    for w in range(len(matriz)):
        result += matriz[w][w]
    return result

def invertir_matriz(matriz):
    nueva_matriz = []
    for fila in matriz:
        for i in fila:
            

def suma_diagonal_inversa(matriz):
    result = 0
    for w in range(len(matriz)):
        result += matriz[w][w]

print(es_magica([
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]))
def es_magica(matriz):
    