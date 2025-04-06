'''
                        TAREA #1 - Agenda telefónica 
Ingeniería en Computación
Taller de Programación
Semestre 1, 2025
Profesor: Ing. Cristian Campos Agüero 

por: Alexander Wing Rojas

'''

def contar_caracteres(texto):
    contador = 0
    for _ in texto:
        contador += 1
    return contador

def contar_lineas():
    try:
        with open("Contactos.txt", "r") as f:
            contador = 0
            for _ in f:
                contador += 1
            return contador
    except FileNotFoundError:
        return 0

def cargar_contactos():
    contactos = []
    try:
        with open("Contactos.txt", "r") as archivo:
            for linea in archivo:
                campos = linea.strip().split("|")
                contactos.append({
                    "cedula": campos[0],
                    "nombre": campos[1],
                    "apellidos": campos[2],
                    "sexo": campos[3],
                    "telefono": campos[4],
                    "fecha": campos[5]
                })
    except FileNotFoundError:
        pass
    return contactos

def guardar_contactos(contactos):
    with open("Contactos.txt", "w") as archivo:
        for c in contactos:
            linea = f"{c['cedula']}|{c['nombre']}|{c['apellidos']}|{c['sexo']}|{c['telefono']}|{c['fecha']}\n"
            archivo.write(linea)

def cedula_valida(cedula):
    return contar_caracteres(cedula) == 9 and cedula.isdigit()

def telefono_valido(telefono):
    return contar_caracteres(telefono) == 8 and telefono.isdigit()

def sexo_valido(sexo):
    return sexo in ("H", "M")

def fecha_valida(fecha):
    partes = fecha.split("/")
    if contar_caracteres(partes[0]) == 2 and contar_caracteres(partes[1]) == 2 and contar_caracteres(partes[2]) == 4:
        return True
    return False

def agregar_contacto():
    cedula = input("Cédula (9 dígitos): ")
    if not cedula_valida(cedula):
        print("Cédula inválida.")
        return
    contactos = cargar_contactos()
    for c in contactos:
        if c["cedula"] == cedula:
            print("Cédula ya existe.")
            return
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    sexo = input("Sexo (H/M): ")
    if not sexo_valido(sexo):
        print("Sexo inválido.")
        return
    telefono = input("Teléfono (8 dígitos): ")
    if not telefono_valido(telefono):
        print("Teléfono inválido.")
        return
    fecha = input("Fecha de nacimiento (DD/MM/YYYY): ")
    if not fecha_valida(fecha):
        print("Fecha inválida.")
        return
    contactos.append({
        "cedula": cedula,
        "nombre": nombre,
        "apellidos": apellidos,
        "sexo": sexo,
        "telefono": telefono,
        "fecha": fecha
    })
    guardar_contactos(contactos)
    print("Contacto agregado.")

def borrar_contacto():
    cedula = input("Ingrese cédula a borrar: ")
    if not cedula_valida(cedula):
        print("Cédula inválida.")
        return
    contactos = cargar_contactos()
    nuevos = []
    encontrado = False
    for c in contactos:
        if c["cedula"] == cedula:
            confirm = input(f"¿Está seguro que quiere borrar a {c['nombre']}? (s/n): ")
            if confirm.lower() == 's':
                encontrado = True
                continue
        nuevos.append(c)
    if encontrado:
        guardar_contactos(nuevos)
        print("Contacto borrado.")
    else:
        print("Contacto no encontrado.")

def modificar_contacto():
    cedula = input("Ingrese cédula a modificar: ")
    if not cedula_valida(cedula):
        print("Cédula inválida.")
        return
    contactos = cargar_contactos()
    modificado = False
    for c in contactos:
        if c["cedula"] == cedula:
            c["nombre"] = input("Nuevo nombre: ")
            c["apellidos"] = input("Nuevos apellidos: ")
            sexo = input("Nuevo sexo (H/M): ")
            if sexo_valido(sexo):
                c["sexo"] = sexo
            telefono = input("Nuevo teléfono (8 dígitos): ")
            if telefono_valido(telefono):
                c["telefono"] = telefono
            fecha = input("Nueva fecha de nacimiento (DD/MM/YYYY): ")
            if fecha_valida(fecha):
                c["fecha"] = fecha
            modificado = True
            break
    if modificado:
        guardar_contactos(contactos)
        print("Contacto modificado.")
    else:
        print("Contacto no encontrado.")

def ver_contactos():
    contactos = cargar_contactos()
    for c in contactos:
        print(c)

def buscar_nombre():
    nombre = input("Ingrese nombre a buscar: ")
    if nombre.strip() == "":
        print("Nombre vacío.")
        return
    contactos = cargar_contactos()
    for c in contactos:
        if nombre.lower() in c["nombre"].lower():
            print(c)

def buscar_telefono():
    tel = input("Ingrese teléfono a buscar: ")
    if tel.strip() == "":
        print("Teléfono vacío.")
        return
    contactos = cargar_contactos()
    for c in contactos:
        if tel in c["telefono"]:
            print(c)

def total_contactos():
    total = contar_lineas()
    print(f"Total de contactos: {total}")

def menu():
    while True:
        print("\nAGENDA TELEFÓNICA")
        print("1. Registrar contacto")
        print("2. Borrar contacto")
        print("3. Modificar contacto")
        print("4. Ver todos los contactos")
        print("5. Buscar por nombre")
        print("6. Buscar por teléfono")
        print("7. Total de contactos")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            borrar_contacto()
        elif opcion == "3":
            modificar_contacto()
        elif opcion == "4":
            ver_contactos()
        elif opcion == "5":
            buscar_nombre()
        elif opcion == "6":
            buscar_telefono()
        elif opcion == "7":
            total_contactos()
        elif opcion == "9":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

# Ejecutar el menú
menu()
