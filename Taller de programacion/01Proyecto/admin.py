import os
from datetime import datetime
from utilidades import limpiar_pantalla

def len_precario(lista): #reemplazo para len()
    contador = 0
    for w in lista: #w de wing muejejej
        contador += 1
    return contador

def shuffle_precario(lista): #reemplazo para random()
    n = len_precario(lista)
    ahora = datetime.now()
    semilla = ahora.second + ahora.microsecond #usa la fecha y tiempo actuales para crear una semilla que servirá para emular la función random()
    for i in range(n-1, 0, -1):
        j = (semilla + i) % n
        lista[i], lista[j] = lista[j], lista[i]
    return lista

def precario_sample(lista, n):
    copia = lista[:]
    shuffle_precario(copia)
    resultado = []
    for i in range(n):
        resultado.append(copia[i])
    return resultado

def autenticar():
    ruta_actual = os.path.dirname(os.path.abspath(__file__)) #verifica la exisencia de la carpeta data y del arcghibov acceso
    ruta_acceso = os.path.join(ruta_actual, "data", "Acceso.txt")
    os.makedirs(os.path.dirname(ruta_acceso), exist_ok=True)
    crear_archivo = False
    if not os.path.exists(ruta_acceso):
        crear_archivo = True
    else:
        if os.path.getsize(ruta_acceso) == 0:
            crear_archivo = True
    if crear_archivo:
        with open(ruta_acceso, "w", encoding='utf-8') as f: #de lo contrario, sino existe, por cualquier motivo, la verdad no quiero perder puntos con fallos de que no se pasen documentos; pues se crea, tampoco es un archivo tan grande
            f.write("admin;admin123") #además se codifica en formato utf-8 para que pueda leer tildes y Ñ's, porque por defecto windows es xenófobo y solo lee inglish
        print("\nSe ha creado el archivo de acceso con credenciales por defecto:")
        print("Usuario: admin")
        print("Contraseña: admin123") #especifica el usuario y contraseña por cualquier cosa, yo se la daré al profe en el README.md
        input("\nPresione Enter para continuar...")
    usuario = input("\nUsuario: ")
    clave = input("Contraseña: ")
    try:
        with open(ruta_acceso, "r", encoding='utf-8') as f:
            contenido = f.read().strip()
            credenciales = contenido.split(';')
            if len_precario(credenciales) == 2:
                u, c = credenciales
                if u == usuario and c == clave:
                    print("\n¡Acceso concedido!")
                    return True
            print("\nCredenciales incorrectas.")
    except Exception as e:
        print(f"\nError al leer el archivo de acceso: {str(e)}")
    return False

def menu_admin():
    """Menú administrativo principal."""
    if not autenticar():
        input("\nAcceso denegado. Presione Enter para continuar...")
        return
    while True:
        limpiar_pantalla()
        print("="*50)
        print(" MENÚ ADMINISTRATIVO ".center(50))
        print("="*50)
        print("\n1. Gestión de Preguntas")
        print("2. Gestión de Juegos")
        print("3. Historial de Juegos")
        print("4. Estadísticas de Juegos")
        print("5. Volver")
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            gestion_preguntas()
        elif opcion == "2":
            gestion_juegos()
        elif opcion == "3":
            menu_historial()
        elif opcion == "4":
            menu_estadisticas()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")

def gestion_preguntas():
    while True:
        limpiar_pantalla()
        print("="*50)
        print(" GESTIÓN DE PREGUNTAS ".center(50))
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
            print("Opción inválida, muy maal.")
            input("Presione Enter para continuar...")

def agregar_pregunta():
    print("\n--- NUEVA PREGUNTA ---")
    pregunta = input("Enunciado de la pregunta: ")
    incorrecta1 = input("Opción incorrecta 1: ")
    incorrecta2 = input("Opción incorrecta 2: ")
    incorrecta3 = input("Opción incorrecta 3: ")
    correcta = input("Correcta (se revolverán, así que solo escriba la opción correcta): ")
    try:
        with open("data/Preguntas.txt", "a", encoding="utf-8") as f:
            id_nuevo = sum(1 for _ in open("data/Preguntas.txt", encoding="utf-8")) + 1
            f.write(f"{id_nuevo},{pregunta},{incorrecta1},{incorrecta2},{incorrecta3},{correcta}\n")
        print("Pregunta agregada, ya puede ir a disfrutarla")
    except:
        print("Error al guardar la pregunta")
    input("\nPresione Enter para continuar...")

def ver_preguntas():
    try:
        with open("data/Preguntas.txt", "r", encoding="utf-8") as f:
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

def gestion_juegos():
    print("\n--- GESTIÓN DE JUEGOS ---")
    try:
        with open("data/Preguntas.txt", "r", encoding="utf-8") as f:
            preguntas = [linea.strip().split(',') for linea in f if linea.strip()]
    except FileNotFoundError:
        print("No hay preguntas disponibles")
        input("Presione Enter para continuar...")
        return
    if len_precario(preguntas) < 15:
        print("No hay suficientes preguntas para crear un juego (mínimo serían 15).")
        input("Presione Enter para continuar...")
        return
    preguntas_juego = precario_sample(preguntas, 15)
    nombre_archivo = "ListaPreguntas01.txt"
    try:
        with open("data/IndiceJuegos.txt", "r", encoding="utf-8") as f:
            existentes = [linea.strip() for linea in f if linea.strip()]
        idx = len_precario(existentes) + 1
        nombre_archivo = f"ListaPreguntas{idx:02d}.txt"
    except FileNotFoundError:
        pass
    fecha = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    with open(f"data/{nombre_archivo}", "w", encoding="utf-8") as f:
        f.write(f"1,{fecha},{hora}\n")
        for p in preguntas_juego:
            f.write(",".join(p)+"\n")
    with open("data/IndiceJuegos.txt", "a", encoding="utf-8") as f:
        f.write(nombre_archivo+"\n")
    print(f"Juego guardado como {nombre_archivo}, vaya gane plata!!")
    input("Presione Enter para continuar...")

def menu_historial():
    while True:
        limpiar_pantalla()
        print("="*50)
        print(" HISTORIAL DE JUEGOS ".center(50))
        print("="*50)
        print("\n1. Ver todo el historial")
        print("2. Filtrar por fecha")
        print("3. Filtrar por nombre")
        print("4. Filtrar por premio")
        print("5. Volver")
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            mostrar_historial()
        elif opcion == "2":
            filtro_fecha()
        elif opcion == "3":
            filtro_nombre()
        elif opcion == "4":
            filtro_premio()
        elif opcion == "5":
            break
        else:
            print("Opción inválidaa")
            input("Presione Enter para continuar...")

def mostrar_historial():
    try:
        with open("data/HistorialJuegos.txt", "r", encoding="utf-8") as f:
            print("\n--- HISTORIAL DE JUEGOS ---")
            for linea in f:
                print(linea.strip())
    except FileNotFoundError:
        print("No hay historial disponible.")
    input("\nPresione Enter para continuar...")

def filtro_fecha():
    fecha_ini = input("Fecha inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
    try:
        with open("data/HistorialJuegos.txt", "r", encoding="utf-8") as f:
            print("\n--- FILTRO POR FECHA ---")
            for linea in f:
                datos = linea.strip().split(',')
                if len_precario(datos) >= 8:
                    fecha = datos[6]
                    if fecha_ini <= fecha <= fecha_fin:
                        print(linea.strip())
    except FileNotFoundError:
        print("No hay historial disponible.")
    input("\nPresione Enter para continuar...")

def filtro_nombre():
    nombre = input("Nombre o parte: ").lower()
    try:
        with open("data/HistorialJuegos.txt", "r", encoding="utf-8") as f:
            print("\n--- FILTRO POR NOMBRE ---")
            for linea in f:
                datos = linea.strip().split(',')
                if len_precario(datos) >= 2 and nombre in datos[1].lower():
                    print(linea.strip())
    except FileNotFoundError:
        print("No hay historial disponible.")
    input("\nPresione Enter para continuar...")

def filtro_premio():
    premio = input("Premio exacto (número): ")
    try:
        with open("data/HistorialJuegos.txt", "r", encoding="utf-8") as f:
            print("\n--- FILTRO POR PREMIO ---")
            for linea in f:
                datos = linea.strip().split(',')
                if len_precario(datos) >= 5 and datos[4] == premio:
                    print(linea.strip())
    except FileNotFoundError:
        print("No hay historial disponible.")
    input("\nPresione Enter para continuar...")

def menu_estadisticas():
    """Muestra estadísticas de los juegos."""
    total = 0
    ganados = 0
    perdidos = 0
    suma_premios = 0
    max_premio = 0
    min_premio = None
    try:
        with open("data/HistorialJuegos.txt", "r", encoding="utf-8") as f:
            for linea in f:
                total += 1
                datos = linea.strip().split(',')
                if len_precario(datos) >= 5:
                    aciertos = int(datos[3])
                    premio = int(datos[4])
                    suma_premios += premio
                    if premio > max_premio:
                        max_premio = premio
                    if premio != 0 and (min_premio is None or premio < min_premio):
                        min_premio = premio
                    if aciertos == 15:
                        ganados += 1
                    elif aciertos == 0:
                        perdidos += 1
    except FileNotFoundError:
        print("No hay historial disponible")
        input("Presione Enter para continuar...")
        return
    while True:
        limpiar_pantalla()
        print("="*50)
        print(" ESTADÍSTICAS DE JUEGOS ".center(50))
        print("="*50)
        print(f"\n1. Total de juegos: {total}")
        print(f"2. Total de juegos ganados: {ganados}")
        print(f"3. Total de juegos perdidos: {perdidos}")
        print(f"4. Suma de premios entregados: {suma_premios}")
        print(f"5. Monto máximo obtenido como premio: {max_premio}")
        print(f"6. Monto mínimo obtenido como premio diferente a CERO: {min_premio if min_premio is not None else 0}")
        print("7. Volver")
        opcion = input("\nSeleccione una opción: ")
        if opcion == "7":
            break
##