'''
PROYECTO SUPER HERMANO MAURICIO

TALLER DE PROGRAMACION | S2-2025

POR: ALEXANDER WING

╭∩╮(-_-)╭∩╮
'''

#LIBRERIAS

import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import time
import random
import os
from pathlib import Path

#PARAMETROS GLOBALES

FILAS = 16
COLS  = 20
TILE  = 32
ANCHO = COLS * TILE
ALTO  = FILAS * TILE

#==============================================( MENU PRINCIPAL )==============================================================#

root = tk.Tk() 
root.title("Hermano Mauricio")
root.geometry("700x600")


menu_principal = tk.Frame(root, bg="#000000")
menu_principal.pack(fill="both", expand=True)

menu_principal.columnconfigure(0, weight=1)
menu_principal.rowconfigure(0, weight=1)
menu_principal.rowconfigure(1, weight=1)
menu_principal.rowconfigure(2, weight=1)
menu_principal.rowconfigure(3, weight=1)

titulo_menu_principal = tk.Label(menu_principal, text="ᗒ MENU PRINCIPAL ᗕ"
                                 , fg="white", bg="#000000", font=("Arial", 18, "bold"))
titulo_menu_principal.grid(row=0, rowspan=2, column=0, sticky="ew")

#==============================================BOTON INICIAR JUEGOs

btn_iniciar_juego = tk.Button(menu_principal, text="INICIAR JUEGO" )
btn_iniciar_juego.grid(row=2, column=0,padx=50, pady=12, ipady=9, sticky="ew")
btn_iniciar_juego.configure(bg="#3A3636", fg="white", font=("Arial", 12),
                            activebackground="#4B4747", activeforeground="white",
                            highlightthickness=0)

#==============================================BOTON VER RANKING

btn_ver_ranking = tk.Button(menu_principal, text="VER RANKING")
btn_ver_ranking.grid(column=0, row=3, padx=50,ipady=9, pady=12, sticky="ew")
btn_ver_ranking.configure(bg="#3A3636", fg="white", font=("Arial", 12),
                          activebackground="#4B4747", activeforeground="white",
                          highlightthickness=0)

root.mainloop()
#==============================================( VENTANA DE JUEGO )==============================================================#

juego = tk.Frame(root, bg="#101010")

canvas_juego = tk.Canvas(juego, width=ANCHO, height=ALTO, bg="black",
                   highlightthickness=0, bd=0)
canvas_juego.grid(row=0, column=0, padx=10, pady=10)

panel_derecha = tk.Frame(juego, bg="#181818")
panel_derecha.grid(row=0, column=1, sticky="ns", padx=(0,10), pady=10)


info = tk.Label(panel_derecha, text="Info de partida",
                    fg="white", bg="#181818", font=("Arial", 12, "bold"))
info.pack(pady=(0,10))

etiqueta_movimientos = tk.Label(panel_derecha, text="Movimientos: 0", fg="white", bg="#181818")
etiqueta_movimientos.pack(pady=4)

btn_volver = tk.Button(panel_derecha, text="Volver al menú",
                       bg="#3A3636", fg="white", activebackground="#4B4747",
                       activeforeground="white", highlightthickness=0,
                       command=lambda: mostrar_menu())
btn_volver.pack(pady=(12,0))


#============================================== DIBUJO Y MOVIMIENTO

matriz = [[0]*COLS for _ in range(FILAS)]
matriz[2][2] = 2   # posición inicial de Mario (referencia visual)
matriz[2][5] = 1   # pared
matriz[2][6] = 1   # pared
matriz[8][15] = 6  # princesa (solo color)

# Posición real de Mario (fila, col)
pos_mario = [2, 2]
movimientos = 0

# Colores simples para dibujar la matriz
COLORES = {
    0: "#222",  # camino
    1: "#555",  # pared
    2: "#f00",  # (fondo de celda si quisieras)
    6: "#f7a",  # princesa
}


def dibujar_tablero():

    canvas_juego.delete("all")

    for i in range(FILAS):
        for j in range(COLS):
            x0, y0 = j*TILE, i*TILE
            t = matriz[i][j]
            fill = COLORES.get(t, "#222")
            canvas_juego.create_rectangle(x0, y0, x0+TILE, y0+TILE,
                                    outline="#111", fill=fill)

#NAVEGACION ENTRE PANTALLAS 

def mostrar_menu():
    juego.pack_forget()                
    menu_principal.pack(fill="both", expand=True) 

def mostrar_juego():
    menu_principal.pack_forget()
    juego.pack(fill="both", expand=True)

