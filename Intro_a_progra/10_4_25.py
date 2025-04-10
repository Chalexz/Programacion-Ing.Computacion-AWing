"""import os

def madafokin_Len(lista):
    contador = 0
    for w in lista: 
        contador += 1
    return contador

def imprimir(matriz):
    os.system("clear")
    for fila in matriz:
        for columna in fila:
            print(columna, end=" ")
        print()

def imprimir_v2(matriz):
    os.system("clear")
    for i in range(madafokin_Len(matriz)):
        for j in (range(madafokin_Len(matriz[i]))):
            print(i,',',j, end = "   ")
        print()

'''
dada una matriz retorne la sumatoria de todos los ejemplos de la matriz 
ENTRADA: MATRIZ
SALIDA: MATRIZ 
S: NUMERO
'''

def sumatoria(matriz):
    os.system("clear")
    for fila in matriz:
        for valor in fila:
            res += valor
    return res
        
print(sumatoria(generador_de_matriz(23)))
 

"""
import os
'''
Dada una matriz, retorne una lista con los elementos pares de esa matriz
'''

def generador_de_matriz(largo):
    matriz = []
    contador = 1
    for i in range(largo):
        fila = []
        for j in range(largo):
            fila.append(contador)
            contador += 1
        matriz.append(fila)
    return matriz

#pares(m1) >>> [2,4,6,8,10,12]
def pares(matriz):
    os.system("clear")
    lista_pares = []
    for linea in matriz:
        for valor in linea:
            if valor % 2== 0:
                lista_pares += [valor]
    return lista_pares

print (pares(generador_de_matriz(4)))

def diagonal(matriz):
    i = 1
    lista_diagonal = []
    for linea in matriz:
            lista_diagonal += [linea[i]]
            i += 1
    return lista_diagonal
print(diagonal(generador_de_matriz(3)))
