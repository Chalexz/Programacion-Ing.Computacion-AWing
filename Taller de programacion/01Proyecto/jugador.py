import time
from datetime import datetime
from utilidades import limpiar_pantalla
from admin import shuffle_precario

def len_precario(lista):
    contador = 0
    for _ in lista:
        contador += 1
    return contador

def cargar_preguntas():
    try:
        with open("data/Preguntas.txt", "r", encoding="utf-8") as archivo:
            preguntas = []
            for linea in archivo:
                datos = linea.strip().split(',')
                if len_precario(datos) >= 7:
                    preguntas.append(datos)
            return preguntas
    except FileNotFoundError:
        print("\nERROR: No hay preguntas disponibles.")
        return []

def buscar_pregunta_no_usada(todas, usadas):
    for preg in todas:
        encontrada = False
        for usada in usadas:
            iguales = True
            for i in range(7):
                if preg[i] != usada[i]:
                    iguales = False
                    break
            if iguales:
                encontrada = True
                break
        if not encontrada:
            return preg
    return None

def mostrar_opciones_5050(p):
    opciones = []
    correcta = int(p[6])
    # Agregar la correcta
    opciones.append((correcta, p[correcta+2]))
    # Buscar la primera incorrecta
    for i in range(1,5):
        if i != correcta:
            opciones.append((i, p[i+2]))
            break
    return opciones

def jugar():
    preguntas = cargar_preguntas()
    if not preguntas:
        input("\nPresione Enter para volver al menú...")
        return

    preguntas = shuffle_precario(preguntas)
    limpiar_pantalla()
    print("="*50)
    print(" ¡BIENVENIDO AL JUEGO! ".center(50))
    print("="*50)
    
    while True:
        cedula = input("\nCédula (9 dígitos): ")
        if len_precario(cedula) == 9 and cedula.isdigit():
            break
        print("La cédula debe tener 9 dígitos numéricos.")
    
    nombre = input("Nombre completo: ")
    while True:
        sexo = input("Sexo (Hombre/Mujer): ").strip().lower()
        if sexo in ("hombre", "mujer"):
            sexo = sexo.capitalize()
            break
        print("Sexo inválido. Debe ser 'Hombre' o 'Mujer'.")

    # Juego
    premios = [100, 200, 300, 400, 500, 1000, 2000, 2500, 4000, 5000, 7000, 8500, 9500, 12000, 15000]
    aciertos = 0
    fecha_inicio = datetime.now().strftime("%Y-%m-%d")
    hora_inicio = datetime.now().strftime("%H:%M:%S")
    archivo_juego = "Preguntas.txt"

    usadas = []
    cambio_pregunta_usado = False
    cincuenta_usado = False
    total_preguntas = len_precario(preguntas)
    i = 0
    while i < 15 and i < total_preguntas:
        limpiar_pantalla()
        print(f"\nPregunta {i+1} - Valor: ₡{premios[i]*1000:,}")
        p = preguntas[i]
        usadas.append(p)
        print(f"\n{p[1]}") 
        for op in range(4):
            print(f"{op+1}. {p[op+2]}")
        print(f"\nComodines disponibles: 1) Cambio de pregunta [{ 'Disponible' if not cambio_pregunta_usado else 'Usado' }], 2) 50/50 [{ 'Disponible' if not cincuenta_usado else 'Usado' }] ")

        comodin_usado = False
        while True:
            print("\n¿Desea usar un comodín?")
            print("1. No usar comodín")
            if not cambio_pregunta_usado:
                print("2. Cambio de pregunta")
            if not cincuenta_usado:
                print("3. 50/50")
            eleccion = input("Seleccione opción: ")
            if eleccion == "1":
                break
            elif eleccion == "2" and not cambio_pregunta_usado:
                nueva = buscar_pregunta_no_usada(cargar_preguntas(), usadas)
                if nueva:
                    preguntas[i] = nueva
                    p = nueva
                    usadas.append(nueva)
                    cambio_pregunta_usado = True
                    limpiar_pantalla()
                    print("\n¡Cambio de pregunta activado!")
                    print(f"\n{p[1]}")
                    for op in range(4):
                        print(f"{op+1}. {p[op+2]}")
                else:
                    print("No hay preguntas disponibles para cambiar.")
                continue
            elif eleccion == "3" and not cincuenta_usado:
                opciones_50 = mostrar_opciones_5050(p)
                print("\nOpciones 50/50:")
                for idx, (num, texto) in enumerate(opciones_50):
                    print(f"{idx+1}. {texto}")
                while True:
                    resp_50 = input("\nTu respuesta (1-2): ")
                    if resp_50 in ("1","2"):
                        break
                    print("Opción inválida.")

                seleccion = opciones_50[int(resp_50)-1][0]
                if seleccion == int(p[6]):
                    aciertos += 1
                    print(f"\n¡Correcto! Llevas ₡{premios[i]*1000:,}")
                else:
                    print(f"\n¡Incorrecto! La respuesta era: {p[int(p[6])+2]}")
                    input("\nPresione Enter para continuar...")
                    break
                cincuenta_usado = True
                comodin_usado = True
                input("\nPresione Enter para continuar...")
                break
            else:
                print("Opción inválida.")
        if comodin_usado:
            i += 1
            continue
        while True:
            resp = input("\nTu respuesta (1-4): ")
            if resp in ('1','2','3','4'):
                break
            print("Opción inválida.")
        if int(resp) == int(p[6]):
            aciertos += 1
            print(f"\n¡Correcto! Llevas ₡{premios[i]*1000:,}")
        else:
            print(f"\n¡Incorrecto! La respuesta era: {p[int(p[6])+2]}")
            input("\nPresione Enter para continuar...")
            break
        input("\nPresione Enter para continuar...")
        i += 1

    fecha_fin = datetime.now().strftime("%Y-%m-%d")
    hora_fin = datetime.now().strftime("%H:%M:%S")
    with open("data/HistorialJuegos.txt", "a", encoding="utf-8") as f:
        f.write(f"{cedula},{nombre},{sexo},{aciertos},{premios[aciertos-1]*1000 if aciertos > 0 else 0},{archivo_juego},{fecha_inicio},{hora_inicio},{fecha_fin},{hora_fin}\n")

    print(f"\nJuego terminado. Acertaste {aciertos} preguntas.")
    print(f"Premio final: ₡{premios[aciertos-1]*1000 if aciertos > 0 else 0:,}")
    input("\nPresione Enter para volver al menú...")