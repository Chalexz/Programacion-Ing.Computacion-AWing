import os
import time

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear') #forma de limpiar la terminal sin importar el os de quien lo corra | Cuestión visual xfa no me quiten puntos por esto

def cargar_preguntas():
    import os
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_preguntas = os.path.join(ruta_actual, "Preguntas.txt")
    try:
        with open(ruta_preguntas, "r") as archivo:
            return [linea.strip().split(',') for linea in archivo if linea.strip()]
    except FileNotFoundError:
        print("\nERROR: No hay preguntas disponibles.")
        return []

def jugar():
    preguntas = cargar_preguntas()
    if not preguntas:
        input("\nPresione Enter para volver al menú...")
        return

    limpiar_pantalla()
    print("="*50)
    print(" ¡BIENVENIDO AL JUEGO! ".center(50))
    print("="*50)
    
    # Registro de jugador
    while True:
        cedula = input("\nCédula (9 dígitos): ")
        if len(cedula) == 9 and cedula.isdigit():
            break
        print("La cédula debe tener 9 dígitos numéricos.")
    
    nombre = input("Nombre completo: ")
    sexo = input("Sexo (Hombre/Mujer): ")

    # Juego
    premios = [100, 200, 300, 400, 500, 1000, 2000, 2500, 4000, 5000, 7000, 8500, 9500, 12000, 15000]
    aciertos = 0

    for i in range(min(15, len(preguntas))):  # Máximo 15 preguntas
        limpiar_pantalla()
        print(f"\nPregunta {i+1} - Valor: ₡{premios[i]:,}mil")
        p = preguntas[i]
        print(f"\n{p[1]}")  # La pregunta
        for op in range(4):  # Opciones 1-4
            print(f"{op+1}. {p[op+2]}")
        
        while True:
            resp = input("\nTu respuesta (1-4): ")
            if resp in ('1','2','3','4'):
                break
            print("Opción inválida.")
        
        if int(resp) == int(p[6]):  # Respuesta correcta
            aciertos += 1
            print(f"\n¡Correcto! Llevas ₡{premios[i]:,}")
        else:
            print(f"\n¡Incorrecto! La respuesta era: {p[int(p[6])+2]}")
            break
        
        input("\nPresione Enter para continuar...")

    # Guardar historial
    with open("data/HistorialJuegos.txt", "a") as f:
        f.write(f"{cedula},{nombre},{sexo},{aciertos},{premios[aciertos-1] if aciertos > 0 else 0}\n")

    print(f"\nJuego terminado. Acertaste {aciertos} preguntas.")
    print(f"Premio final: ₡{premios[aciertos-1] if aciertos > 0 else 0:,}")
    input("\nPresione Enter para volver al menú...")