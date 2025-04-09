'''                                                                             Laboratorio #3 
Manejo de Archivos

El siguiente laboratorio consiste en una serie de ejercicios para practicar el desarrollo de programación en sintaxis de Python, además de evaluación de conceptos vistos 
en clases anteriores. El objetivo de este laboratorio está en el uso de y manipulación archivos y cadenas de texto, recuerde que en cada función que desarrollen agregar 
los comentarios (nombre, parámetros entrada, salida y restricciones), además, se reforzará el uso de los inputs para el manejo de menú.

Hecho por Alexander Wing Rojas el 9/4/25

'''

'''
                                                                        Ejercicio 1. Valor 10 puntos.
Escriba una función llamada totalizar(archivo, valorCol1, valorCol2) que tiene como parámetro de entrada el nombre del archivo, el valor de ambas columnas para totalizar,
el resultado será imprimir su contenido totalizado según categoría especificada, el archivo tendrá una estructura separada por comas, ejemplo:

ENTRADAS: nombre del archivo y valores de columbas
SALIDAS: el contenido totalizado según categoría requerida
RESTRICCIONES: -

#ejemplo: ("ejercicio1.txt", "lunes", "comida")
'''
def totalizar(archivo, valoCol1, valorCol2):
    total = 0
    try:
        with open(archivo, "r") as f:
            for linea in f:
                colum = linea.strip().split(",")
                if colum[0] == valoCol1 and colum[1] == valorCol2:
                    total += float(colum[2])
        return f"Total para {valoCol1} por Concepto de {valorCol2} es: {total}"
    except FileNotFoundError:
        return "El archivo no existe, compa"

'''
                                                                        Ejercicio 2. Valor 10 puntos.

Escriba una función llamada ordenarArchivos(archivo1, archivo2, archivo3) que reciba tres parámetros de entrada, el nombre de un archivo1, archivo2 y el nombre 
del nuevo archivo, este último tendrá el contenido ambos archivos ordenados de mayor a mejor. Evitar funciones built-in. Los datos de cada archivo serán del tipo numérico, 
entero y positivo, además existirá un número por línea. El archivo de salida se debe crear con el nombre del parámetro 3.

ENTRADAS: 
SALIDAS:
RESTRICCIONES:
'''
def len_chino(lista): #len sin licencia
    contador = 0
    for w in lista: 
        contador += 1
    return contador

def ordenarArchivos(archivo1, archivo2, archivo3):
    try:
        numeros = []

        with open(archivo1, "r") as f1:
            for linea in f1:
                if linea.strip():
                    numeros.append(int(linea.strip()))

        with open(archivo2, "r") as f2:
            for linea in f2:
                if linea.strip():
                    numeros.append(int(linea.strip()))

        for i in range(len_chino(numeros)):
            for j in range(i + 1, len_chino(numeros)):
                if numeros[i] < numeros[j]:
                    numeros[i], numeros[j] = numeros[j], numeros[i]

        with open(archivo3, "w") as f3:
            for numero in numeros:
                f3.write(str(numero) + "\n")

        return f"Archivo {archivo3} creado con éxito."
    except FileNotFoundError:
        return "Uno de los archivos de entrada no existe."
    except ValueError:
        return "Error: Uno de los archivos contiene datos no numéricos."
    except Exception as e:
        return f"Error inesperado: {e}"