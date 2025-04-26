import os

def autenticar():
    intentos = 3
    while intentos > 0:
        usuario = input("Usuario: ")
        clave = input("Contraseña: ")
        
        try:
            with open("data/Acceso.txt", "r") as f:
                for linea in f:
                    if linea.strip():
                        u, c = linea.strip().split(';')
                        if u == usuario and c == clave:
                            return True
        except FileNotFoundError:
            print("Error: Archivo de acceso no encontrado")
            return False
        
        intentos -= 1
        print(f"Credenciales incorrectas. Intentos restantes: {intentos}")
    return False

def menu_admin():
    if not autenticar():
        input("\nAcceso denegado. Presione Enter para continuar...")
        return
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*50)
        print(" MENÚ ADMINISTRATIVO ".center(50))
        print("="*50)
        print("\n1. Agregar pregunta")
        print("2. Ver preguntas")
        print("3. Volver")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            agregar_pregunta()
        elif opcion == "2":
            ver_preguntas()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")

def agregar_pregunta():
    print("\n--- NUEVA PREGUNTA ---")
    pregunta = input("Pregunta: ")
    opciones = [input(f"Opción incorrecta {i+1}: ") for i in range(3)]
    correcta = input("Respuesta correcta (1-4): ")
    
    try:
        with open("data/Preguntas.txt", "a") as f:
            id_nuevo = sum(1 for _ in open("data/Preguntas.txt")) + 1
            f.write(f"{id_nuevo},{pregunta},{','.join(opciones)},{correcta}\n")
        print("¡Pregunta agregada!")
    except:
        print("Error al guardar la pregunta")
    input("\nPresione Enter para continuar...")

def ver_preguntas():
    try:
        with open("data/Preguntas.txt", "r") as f:
            print("\n--- PREGUNTAS ---")
            for linea in f:
                if linea.strip():
                    datos = linea.strip().split(',')
                    print(f"\nID: {datos[0]}")
                    print(f"Pregunta: {datos[1]}")
                    for i in range(3):
                        print(f"Opción {i+1}: {datos[i+2]}")
                    print(f"Correcta: Opción {datos[5]}")
    except FileNotFoundError:
        print("No hay preguntas registradas")
    input("\nPresione Enter para continuar...")