'''
PODEROSISIMO SISTEMA DE VACUNACIONN 
POR: ALEXANDER WING ROJAS 
Taller de Programación - Semestre II 2025

    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠝⡄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⡀⠀⠀⠀⠀⣘⡴⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡄⠡⣀⣤⣶⣿⣿⣷⡱⡀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠚⢉⠈⡄⢹⣿⣿⠿⠛⠉⠑⡡⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⢴⢺⡿⠋⢭⠀⡘⡄⠘⡀⢫⠀⠀⠀⠀⠀⠑⠃
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⡀⠁⢣⠐⡈⢆⡱⠜⠊⠑⣀⡆⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣠⢊⣇⠀⠱⣘⡤⠗⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣀⠠⠐⠉⠀⠁⠈⠓⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

'''

##=============================================== AUXILIARES / UTILIDADES ==============================================================

import os #importo os para poder usar "cls" y limpiar la terminal luego de cada print de menus
import datetime #importo datetime para sacar la fecha y usarla en registros de vacunacion
"""
Objetivo: Autenticar al usuario verificando sus credenciales contra el archivo usuarios.txt.
Entrada: ninguna
Salida: True si el usuario y clave son correctos, False si no
Restricción: nada
"""
def autenticar_usuario():
    
    usuario_input = input("Ingrese usuario: ")
    clave_input = input("Ingrese contraseña: ")
    
    try:
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")
                if len(datos) == 2:
                    usuario, clave = datos
                    if usuario_input == usuario and clave_input == clave:
                        print("Autenticación exitosa \ (•◡•) /")
                        return True
        print("Usuario o clave incorrectos ಠ╭╮ಠ")
        return False
    except FileNotFoundError:
        print("Archivo usuarios.txt no encontrado ಠ╭╮ಠ")
        return False


#=============================================== MENU PRINCIPAL ==============================================================

"""
Objetivo: Mostrar el menú principal del sistema de vacunación.
entrada: ninguna
salida: imprime el menú principal en pantalla
restricción: nada
"""
def mostrar_menu():    
    os.system("cls")
    print("===================================")
    print("    ✙ Sistema de Vacunación ✙")
    print("===================================")
    print("1. Administración")
    print("2. Registro de Vacunación")
    print("3. Consultas")
    print("4. Estadísticas")
    print("5. Alerta de Seguimiento")
    print("6. Salir")
    print("===================================")

#=============================================== FUNCIONES 1ISTRACION ==============================================================

"""
Objetivo: Cargar la información de las vacunas desde el archivo vacunas.txt.
entrada: ninguna
salida: retorna una lista de diccionarios con la información de cada vacuna leída desde vacunas.txt
restricción: si el archivo no existe, imprime un mensaje y retorna una lista vacía
"""
def cargar_vacunas(): 
    vacunas = []
    try:
        with open('vacunas.txt', 'r') as archivo:
            for linea in archivo:
                datos = linea.strip().split(';') 
                vacuna = {
                "id": int(datos[0]),
                "nombre": datos[1],
                "dosis": int(datos[2]),
                "edad_minima": int(datos[3])
            }
                vacunas.append(vacuna)
    except FileNotFoundError:
        print("Archivo vacunas.txt no encontrado")
    return vacunas

"""
Objetivo: Guardar la lista de vacunas en el archivo vacunas.txt.
entrada: una lista con todas las vacunas existentes guardadas más recientemente
salida: no retorna nada persé, pero sí reescribe o crea y escribe en el archivo de texto vacunas.txt, cada una de las vacunas en la lista vacunas, y lo da por línea, con ayuda de un salto de linea
restricción: sobrescribe el archivo, por lo que se pierden los datos anteriores
"""
def guardar_vacunas(vacunas):
    with open("vacunas.txt" , "w") as archivo:
        for vacuna in vacunas:
            archivo.write(f"{vacuna['id']};{vacuna['nombre']};{vacuna['dosis']};{vacuna['edad_minima']}\n")

"""
Objetivo: Agregar una nueva vacuna a la lista y almacenarla en el archivo.
entrada: lista de vacunas, nombre de la vacuna, cantidad de dosis, edad mínima
salida: agrega una nueva vacuna a la lista y la guarda en el archivo vacunas.txt, imprime mensaje de éxito
restricción: el id de la vacuna se asigna automáticamente como el siguiente número entero
"""
def agregar_vacunas(vacunas, nombre, dosis, edad_minima):
    id_vacuna = len(vacunas) + 1
    vacuna = {
        "id": id_vacuna,
        "nombre": nombre,
        "dosis": dosis,
        "edad_minima": edad_minima
    }
    vacunas.append(vacuna)
    guardar_vacunas(vacunas)
    print(f"La vacuna '{nombre}' añadida exitosamente \ (•◡•) /")

"""
Objetivo: Eliminar una vacuna de la lista y actualizar el archivo.
entrada: lista de vacunas, id de la vacuna a eliminar
salida: elimina la vacuna de la lista y actualiza el archivo vacunas.txt, imprime mensaje de éxito o error
restricción: solo elimina si encuentra el id, si no existe muestra mensaje de error
"""
def eliminar_vacuna(vacunas, id_vacuna):
    vacuna_eliminar = None
    for vacuna in vacunas:
        if vacuna['id'] == id_vacuna:
            vacuna_eliminar = vacuna
            break
    if vacuna_eliminar:
        vacunas.remove(vacuna_eliminar)
        guardar_vacunas(vacunas)
        print(f"Vacuna con ID {id_vacuna} eliminada exitosamente \ (•◡•) /")
    else:
        print(f"No se encontró una vacuna con el ID {id_vacuna}")

"""
Objetivo: Mostrar todas las vacunas disponibles en pantalla.
entrada: lista de vacunas
salida: imprime en pantalla la información de todas las vacunas disponibles
restricción: si la lista está vacía, no imprime nada
"""
def mostrar_vacunas(vacunas):
    print("Lista de vacunas disponibles:")
    for vacuna in vacunas:
        print(f"ID: {vacuna['id']} - Nombre: {vacuna['nombre']} - Dosis: {vacuna['dosis']} - Edad mínima: {vacuna['edad_minima']}")

"""
Objetivo: Permitir la administración de vacunas (agregar, eliminar, mostrar).
entrada: lista de vacunas
salida: permite al usuario agregar, eliminar o mostrar vacunas, o volver al menú principal
restricción: el menú se repite hasta que el usuario elija salir
"""
def menu_administracion(vacunas):
    while True: 
        os.system("cls")
        print('\n Menu Administración')
        print("1. Agregar Vacuna")
        print("2. Eliminar Vacuna")
        print("3. Mostrar Vacuna")
        print("4. Volver al Menú Principal")
        opcion = input("Favor seleccionar una de las opciones. Digite el número:  ")
        if opcion == "1":
            nombre = input("Ingrese el nombre de la vacuna a agregar: ")
            dosis = int(input("Ingrese la dosis requerida (1 o 2): "))
            edad_minima = int(input("Ingrese la edad mínima recomendada para la vacuna en cuestión: "))
            agregar_vacunas(vacunas, nombre, dosis, edad_minima)
        elif opcion == "2":
            id_vacuna = int(input("Ingrese el ID de la vacuna a eliminar: "))
            eliminar_vacuna(vacunas, id_vacuna)
        elif opcion == "3":
            mostrar_vacunas(vacunas)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo ಠ╭╮ಠ")

#=============================================== FUNCIONES REGISTRO ==============================================================

"""
Objetivo: Cargar los registros de vacunación desde el archivo registros.txt.
entrada: ninguna
salida: retorna una lista de diccionarios con los registros de vacunación leídos desde registros.txt
restricción: si el archivo no existe, imprime un mensaje y retorna una lista vacía
"""
def cargar_registros(): 
    registros = []
    try:
        with open("registros.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")
                registro = {
                    "cedula": datos[0],
                    "nombre": datos[1],
                    "edad": int(datos[2]),
                    "sexo": datos[3],
                    "id_vacuna": int(datos[4]),
                    "fecha": datos[5],
                    "dosis": int(datos[6])
                }

                registros.append(registro)
    except FileNotFoundError:
        print("Archivo registros.txt no encontrado ಠ╭╮ಠ")
    return registros

"""
Objetivo: Guardar un registro de vacunación en el archivo registros.txt.
entrada: un diccionario con los datos de un registro de vacunación
salida: agrega el registro al archivo registros.txt
restricción: el archivo se abre en modo append, por lo que solo agrega al final
"""
def guardar_registro(registro):
    with open("registros.txt", "a") as archivo:  # "a" para añadir al final
        archivo.write(f"{registro['cedula']};{registro['nombre']};{registro['edad']};{registro['sexo']};{registro['id_vacuna']};{registro['fecha']};{registro['dosis']}\n")

"""
Objetivo: Registrar una nueva vacunación solicitando los datos al usuario.
entrada: lista de vacunas y lista de registros de vacunación
salida: solicita datos al usuario, crea y guarda un registro de vacunación
restricción: valida que los datos ingresados sean correctos y que no se repita una dosis para la misma persona y vacuna
"""
def registrar_vacunacion(vacunas, registros):
    os.system("cls")
    print("=== Registro de Vacunación ===")

    # Cédula
    while True:
        cedula = input("Ingrese la cédula (9 dígitos): ")
        if len(cedula) == 9 and cedula.isdigit():
            break
        else:
            print("Cédula inválida. DEBE tener 9 dígitos.")

    #Nombre
    nombre = input("Ingrese el nombre completo: ")

    # edad
    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            if edad > 0:
                break
            else:
                print("La edad debe ser mayor a 0.  ಠ╭╮ಠ")
        except ValueError:
            print("Ingrese un número válido")

    # Sexo
    while True:
        sexo = input("Ingrese el sexo (M/F): ").upper() #modifica los "m" o "f" para forzar que sea M o F
        if sexo in ["M", "F"]:
            break
        else:
            print("Sexo inválido. Ingrese sí o sí 'M' o 'F'. ಠ╭╮ಠ")

    # Mostrar vacunas disponibles
    mostrar_vacunas(vacunas)

    # Vacuna aplicada
    while True:
        try:
            id_vacuna = int(input("Ingrese el ID de la vacuna aplicada: "))
            vacuna_elegida = None
            for v in vacunas:
                if v["id"] == id_vacuna:
                    vacuna_elegida = v
                    break
            if vacuna_elegida:
                if edad >= vacuna_elegida["edad_minima"]:
                    break
                else:
                    print(f"La edad mínima para esta vacuna es {vacuna_elegida['edad_minima']}")
            else:
                print("ID de vacuna inválido.")
        except ValueError:
            print("Ingrese un número válido.")

    # Dosis
    while True:
        try:
            dosis = int(input(f"Ingrese número de dosis aplicadas (max {vacuna_elegida['dosis']}): "))
            if 1 <= dosis <= vacuna_elegida["dosis"]:
                # Validar que no se repita una dosis de la misma vacuna
                existe = False
                for r in registros:
                    if r["cedula"] == cedula and r["id_vacuna"] == id_vacuna and r["dosis"] == dosis:
                        existe = True
                        break
                if not existe:
                    break
                else:
                    print("Esta dosis ya fue registrada para esta persona ಠ╭╮ಠ")
            else:
                print(f"Dosis inválida. Debe estar entre 1 y {vacuna_elegida['dosis']}.")
        except ValueError:
            print("Ingrese un número válido ಠ╭╮ಠ")

    # Fecha automática
    fecha = datetime.date.today().isoformat()

    # Crear registro
    registro = {
        "cedula": cedula,
        "nombre": nombre,
        "edad": edad,
        "sexo": sexo,
        "id_vacuna": id_vacuna,
        "fecha": fecha,
        "dosis": dosis
    }

    # Guardar registro
    guardar_registro(registro)
    registros.append(registro)
    print(f"\nRegistro de vacunación de {nombre} agregado correctamente \ (•◡•) /")
    input("\nPresione Enter para continuar...")

#=============================================== FUNC. DE CONSULTA ==============================================================

"""
Objetivo: Consultar e imprimir los registros de vacunación asociados a una cédula.
entrada: lista de registros y una cédula a consultar
salida: imprime en pantalla los registros asociados a esa cédula
restricción: si no hay registros para esa cédula, muestra un mensaje
"""
def consultar_por_cedula(registros, cedula):
    encontrados = [r for r in registros if r["cedula"] == cedula]
    if encontrados:
        print(f"\nRegistros para cédula {cedula}:")
        for r in encontrados:
            print(f"{r['nombre']} - Vacuna ID {r['id_vacuna']} - Dosis {r['dosis']} - Fecha {r['fecha']}")
    else:
        print("No se encontraron registros para esa cédula.")
    input("Presione Enter para continuar...")

"""
Objetivo: Consultar e imprimir los registros de vacunación asociados a un id de vacuna.
entrada: lista de registros y un id de vacuna
salida: imprime en pantalla los registros asociados a ese id de vacuna
restricción: si no hay registros para esa vacuna, muestra un mensaje
"""
def consultar_por_vacuna(registros, id_vacuna):
    encontrados = [r for r in registros if r["id_vacuna"] == id_vacuna]
    if encontrados:
        print(f"\nPersonas vacunadas con ID de vacuna {id_vacuna}:")
        for r in encontrados:
            print(f"{r['nombre']} - Cédula {r['cedula']} - Dosis {r['dosis']} - Fecha {r['fecha']}")
    else:
        print("No se encontraron registros para esa vacuna")
    input("Presione Enter para continuar...")

"""
Objetivo: Consultar e imprimir los registros de vacunación dentro de un rango de edad.
entrada: lista de registros, edad mínima y edad máxima
salida: imprime en pantalla los registros de personas dentro del rango de edad
restricción: si no hay registros en ese rango, muestra un mensaje
"""
def consultar_por_rango_edad(registros, edad_min, edad_max):
    encontrados = [r for r in registros if edad_min <= r["edad"] <= edad_max]
    if encontrados:
        print(f"\nPersonas con edades entre {edad_min} y {edad_max}:")
        for r in encontrados:
            print(f"{r['nombre']} - Cédula {r['cedula']} - Vacuna ID {r['id_vacuna']} - Dosis {r['dosis']}")
    else:
        print("No se encontraron registros en ese rango de edad")
    input("Presione Enter para continuar...")

"""
Objetivo: Calcular e imprimir estadísticas generales sobre la vacunación.
entrada: lista de registros y lista de vacunas
salida: imprime estadísticas generales sobre la vacunación
restricción: si no hay datos suficientes, muestra mensajes informativos
"""
def estadisticas_generales(registros, vacunas):
    os.system("cls")
    total_personas = len(set([r["cedula"] for r in registros]))
    print(f"Total de personas vacunadas (únicas): {total_personas}")

    print("\nVacunas aplicadas por tipo:")
    for v in vacunas:
        count = len([r for r in registros if r["id_vacuna"] == v["id"]])
        print(f"{v['nombre']} - {count} aplicaciones")

    print("\nPromedio de edad por vacuna:")
    for v in vacunas:
        edades = [r["edad"] for r in registros if r["id_vacuna"] == v["id"]]
        if edades:
            print(f"{v['nombre']} - {sum(edades)//len(edades)} años promedio")
        else:
            print(f"{v['nombre']} - No hay registros")

    hombres = len([r for r in registros if r["sexo"]=="M"])
    mujeres = len([r for r in registros if r["sexo"]=="F"])
    total = hombres + mujeres
    if total > 0:
        print(f"\nPorcentaje de hombres vacunados: {hombres*100/total:.2f}%")
        print(f"Porcentaje de mujeres vacunados: {mujeres*100/total:.2f}%")
    else:
        print("\nNo hay datos de sexo para calcular porcentaje ಠ╭╮ಠ")

    completos = 0
    for r in registros:
        vacuna = next((v for v in vacunas if v["id"]==r["id_vacuna"]), None)
        if vacuna and r["dosis"] >= vacuna["dosis"]:
            completos += 1
    print(f"\nCantidad de personas que completaron todas las dosis: {completos}")
    input("Presione Enter para continuar...")

#=============================================== FUNCIONES ALERTA DE SEGUIMIENTO ==============================================================

"""
Objetivo: Mostrar las personas que deben recibir la siguiente dosis de vacuna.
entrada: lista de registros y lista de vacunas
salida: imprime las personas que deben recibir la siguiente dosis
restricción: solo considera vacunas con más de una dosis y personas que no han completado el esquema
"""
def alerta_seguimiento(registros, vacunas):
    os.system("cls")
    hoy = datetime.date.today()
    seguimiento = []
    for r in registros:
        vacuna = next((v for v in vacunas if v["id"]==r["id_vacuna"]), None)
        if vacuna and vacuna["dosis"]>1:
            fecha = datetime.date.fromisoformat(r["fecha"])
            if (hoy - fecha).days >= 90 and r["dosis"] < vacuna["dosis"]:
                seguimiento.append(r)
    if seguimiento:
        print("Personas que deben recibir la siguiente dosis:")
        for s in seguimiento:
            print(f"{s['nombre']} - Cédula {s['cedula']} - Vacuna ID {s['id_vacuna']} - Dosis actual {s['dosis']}")
    else:
        print("No hay personas pendientes de dosis")
    input("Presione Enter para continuar...")

"""
Objetivo: Ejecutar el flujo principal del sistema de vacunación.
entrada: ninguna
salida: ejecuta el flujo principal del sistema de vacunación
restricción: el ciclo principal se repite hasta que el usuario elige salir
"""
def main():
    vacunas = cargar_vacunas()
    registros = cargar_registros()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ") 

        if opcion == "1":
            if autenticar_usuario():
                menu_administracion(vacunas)
            else:
                input("No puede acceder a Administración ಠ╭╮ಠ. Presione Enter para continuar...")
        elif opcion == "2":
            registrar_vacunacion(vacunas, registros)
        elif opcion == "3":
            os.system("cls")
            print("=== Consultas ===")
            print("1. Por Cédula")
            print("2. Por Vacuna")
            print("3. Por Rango de Edad")
            print("4. Volver")
            op = input("Seleccione una opción: ")
            if op=="1":
                ced = input("Ingrese la cédula a consultar: ")
                consultar_por_cedula(registros, ced)
            elif op=="2":
                vid = int(input("Ingrese el ID de la vacuna a consultar: "))
                consultar_por_vacuna(registros, vid)
            elif op=="3":
                emin = int(input("Edad mínima: "))
                emax = int(input("Edad máxima: "))
                consultar_por_rango_edad(registros, emin, emax)
        elif opcion == "4":
            estadisticas_generales(registros, vacunas)
        elif opcion == "5":
            alerta_seguimiento(registros, vacunas)
        elif opcion == "6":
            print("Saliendo del sistema... (ง ͠° ͟ل͜ ͡°)ง")
            guardar_vacunas(vacunas)
            break
        else:
            print("Opción no válida, intente de nuevo (▀̿Ĺ̯▀̿ ̿)")

if __name__ == "__main__":
    main()
