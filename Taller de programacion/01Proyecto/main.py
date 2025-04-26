'''                        CÓDIGO DE QUIÉN QUIERE SER MILLONARIO VERSION PRECARIA
Hecha por Alexander Wing
Taller de programación 2025 1er semestre 
'''
import jugador
import admin
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear') #forma de limpiar la terminal sin importar el os de quien lo corra | Cuestión visual xfa no me quiten puntos por esto

def menu_principal():
    while True:
        limpiar_pantalla()
        print("="*50)
        print(" QUIÉN QUIERE SER MILLONARIO?!?!?!".center(50)) # .center es como centrar en un doc tipo .docx | Cuestión visual xfa no me quiten puntos por esto
        print("="*50)
        print("\n1. Opciones Administrativas")
        print("2. Jugar")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            global admin
            admin.menu_admin()
        elif opcion == "2":
            global jugador
            jugador.jugar()
        elif opcion == "3":
            limpiar_pantalla()
            print ("\n" #agradecimiento porque hay que ser agradecido
                   "\n=========================================""\n""\n"  
                    "\nGracias por jugar, ojalá le haya gustado!" \
                    "\n""\n""\n=========================================""\n""\n")
            break
        else:
            print("\nOpción incorrecta. Hágalo otra vez")

if __name__ == "__main__":
    menu_principal()