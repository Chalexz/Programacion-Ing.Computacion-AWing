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
    cedula = input("Cédula (9 dígitos): ")
    if not cedula_valida(cedula):
        print("Cédula inválida.")  # puede dar error por largo o por letras
        return
    contactos = cargar_contactos()
    for c in contactos:
        if c["cedula"] == cedula:  # no debe haber duplicados
            print("Cédula ya existe.")
            return
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    sexo = input("Sexo (H/M): ")
    if not sexo_valido(sexo):  # si mete otra letra, ya no sirve
        print("Sexo inválido.")
        return
    telefono = input("Teléfono (8 dígitos): ")
    if not telefono_valido(telefono):  # muy corto, largo o letras
        print("Teléfono inválido.")
        return
    fecha = input("Fecha de nacimiento (DD/MM/YYYY): ")
    if not fecha_valida(fecha):
        print("Fecha inválida.")  # por ejemplo si falta una parte
        return
    # si todo salió bien, se agrega a la lista
    contactos.append({
        "cedula": cedula,
        "nombre": nombre,
        "apellidos": apellidos,
        "sexo": sexo,
        "telefono": telefono,
        "fecha": fecha
    })
    guardar_contactos(contactos)
    print("Contacto agregado.")  # mensaje de confirmación de q se agregó el contacto

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

# menú principal que permite elegir opciones hasta que se decida salir
def menu():
    while True:
        print("\n" + "="*50)
        print("\nAGENDA TELEFÓNICA")
        print("1. Registrar contacto")
        print("2. Borrar contacto")
        print("3. Modificar contacto")
        print("4. Ver todos los contactos")
        print("5. Buscar por nombre")
        print("6. Buscar por teléfono")
        print("7. Total de contactos")
        print("9. Salir")
        print("\n" + "="*50)  # una super forma que vi de meterle enriquecimiento visual en vez de hacer un "print("\n======================\n")"
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
            print("Saliendo...")  # termina el bucle del menú
            break
        else:
            print("Opción no válida.")  # si elige algo fuera del menú, lo avisa

# ejecuta la func menu para comenzar 
menu()