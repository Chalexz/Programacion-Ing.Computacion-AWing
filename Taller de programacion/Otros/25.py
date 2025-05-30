"de decimal a hexadecimal"

"""
e: num entero decimal
s: string como num hexadecimal
r:
"""

'''
def decimal_hexa(num):
    hexa_final = ""
    hexa = {
        0:"0",
        1:"1",
        2:"2",
        3:"3",
        4:"4",
        5:"5",
        6:"6",
        7:"7",
        8:"8",
        9:"9",
        10:"A",
        11:"B",
        12:"C",
        14:"E",
        15:"F",
    }
    if num in hexa:
        return hexa[num]
    elif:
        
        cociente = num // 16
        residuo = num % 16
'''

"Hexadecimal a Decimal"

"""
e: string tipo texto
s: entero
r: no debe de estar vacío
"""

def convertir_hexa_decimal(string):
    invertido = ""
    resultado = 0
    potencia = 0
    for i in string:
        invertido = i + invertido
    hexa = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}
    for i in invertido:
        if i in hexa: 
            decimal = hexa[i]
            resultado += decimal * (16 ** potencia)
            potencia += 1
    return resultado
print(convertir_hexa_decimal("28E"))

def bin_a_dec(bin):
    