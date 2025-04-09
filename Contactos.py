'''
                        TAREA #1 - Agenda telefónica 
Ingeniería en Computación
Taller de Programación
Semestre 1, 2025
Profesor: Ing. Cristian Campos Agüero 

por: Alexander Wing Rojas

'''

def contar(texto): # func para contar caracteres sin usar el malvado len
    contador = 0
    for _ in texto:
        contador += 1
    return contador

def contar_lineas(): # cuenta cuanatas líneas hay en el archivo de contactos, lo cual indica cuántos hay registrados
    try:
        with open("Contactos.txt", "r") as f:
            contador = 0
            for _ in f:
                contador += 1
            return contador
    except FileNotFoundError:
        return 0 # si el archivo no existe, retorna 0 (poues no hay contactos aún)

def cargar_contactos(): # defcargarcontactos carga todos los contactos desde el archivo y los organiza como diccionarios en una lista
    contactos = []
    try:
        with open("Contactos.txt", "r") as archivo:
            for linea in archivo:
                campos = linea.strip().split("|") # divide la línea por cada campo separado por un caraceter de "|"
                contactos.append({
                    "cedula": campos[0],
                    "nombre": campos[1],
                    "apellidos": campos[2],
                    "sexo": campos[3],
                    "telefono": campos[4],
                    "fecha": campos[5]
                }) #se crea un diccionar por contacto y se agrega a la list
    except FileNotFoundError:
        pass # si no existe el archivo, deay simplemente no hace nada
    return contactos

# guarda la lista de contactos en un archivo de texto plano, uno por línea
def guardar_contactos(contactos):
    with open("Contactos.txt", "w") as archivo:
        for c in contactos:
            # cada campo del contacto se separa con uan "|"" y se guarda como una línea
            linea = f"{c['cedula']}|{c['nombre']}|{c['apellidos']}|{c['sexo']}|{c['telefono']}|{c['fecha']}\n"
            archivo.write(linea)


def cedula_valida(cedula): #para ver si una cédula tiene 9 dígitos y todos son digitos 
    return contar(cedula) == 9 and cedula.isdigit()

# verifica que el número telefónico tenga exactamente 8 numeros o digitos
def telefono_valido(telefono):
    return contar(telefono) == 8 and telefono.isdigit()

# el sexo solo puede ser "H" o "M" según lo que el prof puso
def sexo_valido(sexo):
    return sexo in ("H", "M") # + no admite otras letras que no sean esas

# revisa que la fecha tenga el formato correcto con 3 partes separadas por "/"
def fecha_valida(fecha):
    partes = fecha.split("/")  # divide usando el slash
    if contar(partes[0]) == 2 and contar(partes[1]) == 2 and contar(partes[2]) == 4:
        return True
    return False  # y si algo no cumple, se retorna falso

# agrega un nuevo contacto a la lista si todos los datos resuktan validos
def agregar_contacto():
    while True:
        cedula = input("Cédula (9 dígitos): ")
        if not cedula_valida(cedula):
            print("Cédula inválida. Intente de nuevo.")
            continue
        contactos = cargar_contactos()
        duplicado = False
        for c in contactos:
            if c["cedula"] == cedula:
                print("Cédula ya existe. Intente con otra.")
                duplicado = True
                break
        if duplicado:
            continue
        break  # si está bien y no duplicada, salimos del bucle

    nombre = input("Nombre (Sin apellidos): ")
    apellidos = input("Apellidos: ")

    while True:
        sexo = input("Sexo (H/M): ")
        if sexo_valido(sexo):
            break
        else:
            print("Sexo inválido. Solo se permite H o M.")

    while True:
        telefono = input("Teléfono (8 dígitos): ")
        if telefono_valido(telefono):
            break
        else:
            print("Teléfono inválido. Debe tener 8 dígitos numéricos.")

    while True:
        fecha = input("Fecha de nacimiento (DD/MM/YYYY): ")
        if fecha_valida(fecha):
            break
        else:
            print("Fecha inválida. Formato correcto: DD/MM/YYYY.")

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


# busca y elimina un contacto por su cédula si el usuario confirma
def borrar_contacto():
    cedula = input("Ingrese cédula a borrar: ")
    if not cedula_valida(cedula):
        print("Cédula inválida.")  # revisa estructura primero
        return
    contactos = cargar_contactos()
    nuevos = []  # lista temporal para contactos no eliminados
    encontrado = False  # como el profe dijo en uan clase, esta es una bandera para saber si se halló
    for c in contactos:
        if c["cedula"] == cedula:
            confirm = input(f"¿Está seguro que quiere borrar a {c['nombre']}? (s/n): ")
            if confirm.lower() == 's':
                encontrado = True  # se encontró y quiere borrarlo
                continue  # se salta añadirlo a la lista nueva
        nuevos.append(c)
    if encontrado:
        guardar_contactos(nuevos)
        print("Contacto borrado.")
    else:
        print("Contacto no encontrado.")  # pudo ser por error en la cédula

# permite modificar un contacto existente, cambiando solo lo que se desee
def modificar_contacto():
    cedula = input("Ingrese cédula a modificar: ")
    if not cedula_valida(cedula):
        print("Cédula inválida.")
        return
    contactos = cargar_contactos()
    modificado = False
    for c in contactos:
        if c["cedula"] == cedula:
            # cada campo se puede modificar individualmente
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
            modificado = True  # se marcó como que sí se modificó
            break
    if modificado:
        guardar_contactos(contactos)
        print("Contacto modificado.")
    else:
        print("Contacto no encontrado.")  # quizás escribio mal la cédula

# muestra todos los contactos del archivo uno por uno
def ver_contactos():
    contactos = cargar_contactos()
    for c in contactos:
        print(c)  # imprime el diccionario como está

# permite buscar contactos por nombre, no importa si está incompleto
def buscar_nombre():
    nombre = input("Ingrese nombre a buscar: ")
    if nombre.strip() == "":
        print("Nombre vacío.")  # no deja buscar si no pone nada
        return
    contactos = cargar_contactos()
    for c in contactos:
        if nombre.lower() in c["nombre"].lower():  # compara sin mayusculas
            print(c)

# busca contactos por num telefunico exacto o parcial
def buscar_telefono():
    tel = input("Ingrese teléfono a buscar: ")
    if tel.strip() == "":
        print("Teléfono vacío.")
        return
    contactos = cargar_contactos()
    for c in contactos:
        if tel in c["telefono"]:  # busca coincidencias exactas o parciales
            print(c)

# cuenta y muestra el total de líneas del archivo, lo cual representa contactos
def total_contactos():
    total = contar_lineas()
    print(f"Total de contactos: {total}")  # si no hay archivo, muestra 0

def limpiar_pantalla(): #ayuda demasiado a mantener el orden y comprensión de lo uqe está psaando en la terminal1
    import os
    os.system("cls" if os.name == "nt" else "clear")

def menu_registro():
    while True:
        limpiar_pantalla()
        print("\n" + "=" * 50)
        print("Registro de Contacto")
        print("=" * 50)
        print("11. Registrar contacto")
        print("12. Borrar contacto")
        print("13. Modificar contacto")
        print("14. Ver todos los contactos")
        print("15. Retornar")
        print("=" * 50)
        opcion = input("Digite una opción: ")
        if opcion == "11":
            limpiar_pantalla()
            agregar_contacto()
        elif opcion == "12":
            limpiar_pantalla()
            borrar_contacto()
        elif opcion == "13":
            limpiar_pantalla()
            modificar_contacto()
        elif opcion == "14":
            limpiar_pantalla()
            ver_contactos()
            input("\nPresione Enter para continuar...")
        elif opcion == "15":
            break
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")

def menu_busqueda():
    while True:
        limpiar_pantalla()
        print("\n" + "=" * 50)
        print("Búsquedas")
        print("=" * 50)
        print("21. Buscar por nombre")
        print("22. Buscar por teléfono")
        print("23. Retornar")
        print("=" * 50)
        opcion = input("Digite una opción: ")
        if opcion == "21":
            limpiar_pantalla()
            buscar_nombre()
            input("\nPresione Enter para continuar...")
        elif opcion == "22":
            limpiar_pantalla()
            buscar_telefono()
            input("\nPresione Enter para continuar...")
        elif opcion == "23":
            break
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")
# menú principal que permite elegir opciones hasta que se decida salir
def menu():
    while True:
        limpiar_pantalla()
        print("\n" + "="*50)
        print("\n - BIENVENIDO(A) A AGENDA ALEXFÓNICA -")
        print("\n" + "="*50)
        print("1: Registro de Contacto")
        print("2: Búsquedas")
        print("3: Total contactos")
        print("9: Salir")
        print("="*50)  # una super forma que vi de meterle enriquecimiento visual en vez de hacer un "print("\n======================\n")"
        opcion = input("Ingrese la opción deseada: ")
        if opcion == "1":
            menu_registro()
        elif opcion == "2":
            menu_busqueda()
        elif opcion == "3":
            limpiar_pantalla()
            total_contactos()
            input("\nPresione Enter para continuar...")
        elif opcion == "9":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")
# ejecuta la func menu para comenzar 
menu()