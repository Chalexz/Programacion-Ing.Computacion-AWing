def convertDecBin(num):
    if not isinstance(num, int):
        return 'Error: num debe ser Entero'
    if num < 0:
        return 'Error: num debe ser mayor o igual a CERO'
    
    if num == 0:
        return 0
    
    binario = 0
    potencia = 1  # Para construir el número binario dígito a dígito
    
    while num > 0:
        residuo = num % 2
        binario = binario + residuo * potencia
        num = num // 2
        potencia = potencia * 10
    
    return binario

def decimal_a_octal(num):
    if not isinstance(num, int) or num < 0:
        return "Error: Debe ser un entero positivo"
    
    if num == 0:
        return "0"
    
    octal = ""
    while num > 0:
        residuo = num % 8
        octal = str(residuo) + octal
        num = num // 8
    return octal

def decimal_a_hexadecimal(num):
    if not isinstance(num, int) or num < 0:
        return "Error: Debe ser un entero positivo"
    
    if num == 0:
        return "0"
    
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while num > 0:
        residuo = num % 16
        hexadecimal = hex_digits[residuo] + hexadecimal
        num = num // 16
    return hexadecimal

def decimal_a_base(num, base):
    if not isinstance(num, int) or num < 0 or base < 2 or base > 16:
        return "Error: Parámetros inválidos"
    
    if num == 0:
        return "0"
    
    digits = "0123456789ABCDEF"
    resultado = ""
    while num > 0:
        residuo = num % base
        resultado = digits[residuo] + resultado
        num = num // base
    return resultado