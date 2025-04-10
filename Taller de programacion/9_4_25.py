def contar_lineas(): #cuenta las lineas del prueba.txt
    try:
        with open("prueba.txt", "r") as f:
            contador = 0
            for w in f:
                contador+=1
            return contador
    except FileNotFoundError:
        return False
print(contar_lineas())

print(ValueError)