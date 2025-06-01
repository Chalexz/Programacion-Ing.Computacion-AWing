import tkinter as tk
from tkinter import messagebox
import os

from tablero import crear_tablero
from movimientos import colocar_pieza, puede_colocar, rotar_pieza, eliminar_lineas_completas
from tetrominos import obtener_tetrominos
from precario_utils import len_precario, range_precario, copiar_matriz, random_precario
from archivo import guardar_tablero, cargar_tablero
from ranking import guardar_ranking, mostrar_ranking

colores_piezas = {
    "O": "#ffe600",      # amarillo
    "I": "#00c3f9",      # celeste
    "L": "#ff9500",      # naranja
    "J": "#ff6ec7",      # rosado
    "T": "#a259e6",      # morado
    "Z": "#6ac100",      # verde
    "U": "#ff6ec7",      # rosado (igual que J)
    "MAS": "#ff0000",    # rojo
    "+": "#444444",      # gris oscuro para paredes si no hay imagen
    "0": "black",
    "1": "white"
}

tam_celda = 25

ventana = tk.Tk()
ventana.title("Tetris con Tkinter")

def cargar_img(nombre):
    ruta = os.path.join("tetrónimos_assets", nombre)
    if os.path.exists(ruta):
        img = tk.PhotoImage(file=ruta)
        ancho = img.width()
        alto = img.height()
        if ancho > tam_celda or alto > tam_celda:
            factor = int(ancho / tam_celda)
            if factor < 1: factor = 1
            img = img.subsample(factor, factor)
        return img
    return None

imagenes_piezas = {
    "O": cargar_img("O.png"),
    "I": cargar_img("I.png"),
    "L": cargar_img("L.png"),
    "J": cargar_img("J.png"),
    "T": cargar_img("T.png"),
    "Z": cargar_img("Z.png"),
    "U": cargar_img("U.png"),
    "MAS": cargar_img("CRUZ.png"),
    "+": cargar_img("pared.png")
}

def obtener_tetrominos_con_id():
    formas = obtener_tetrominos()
    nombres = ["O", "I", "L", "J", "T", "Z", "U", "MAS"]
    piezas_con_nombre = []
    for i in range_precario(0, len_precario(formas)):
        forma = formas[i]
        nombre = nombres[i]
        nueva = []
        for fila in forma:
            nueva_fila = []
            for celda in fila:
                if celda == 1:
                    nueva_fila += [nombre]
                else:
                    nueva_fila += ["0"]
            nueva += [nueva_fila]
        piezas_con_nombre += [nueva]
    return piezas_con_nombre

def obtener_velocidad(puntos):
    base = 1000
    ajuste = (puntos // 200) * 100
    velocidad = base - ajuste
    if velocidad < 200:
        velocidad = 200
    return velocidad

puntos = 0
jugador = ""
piezas_disponibles = obtener_tetrominos_con_id()
tablero = crear_tablero()
pieza_actual = random_precario(piezas_disponibles)
fila_pieza = 1
columna_pieza = 4

canvas = tk.Canvas(ventana, width=12*tam_celda, height=22*tam_celda, bg="black", highlightthickness=0)
canvas.grid(row=0, column=0, rowspan=20)

etiqueta_puntos = tk.Label(ventana, text="Puntos: 0", font=("Arial", 12))
etiqueta_puntos.grid(row=0, column=1, padx=5)
etiqueta_nombre = tk.Label(ventana, text="Jugador: ?", font=("Arial", 12))
etiqueta_nombre.grid(row=1, column=1, padx=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=2, column=1, padx=5)

def establecer_nombre():
    global jugador
    jugador = entrada_nombre.get()
    if jugador != "":
        etiqueta_nombre.config(text="Jugador: " + jugador)

tk.Button(ventana, text="Confirmar nombre", command=establecer_nombre).grid(row=3, column=1)
def guardar_partida():
    guardar_tablero("guardado.txt", tablero)
    mensaje = ""
    if jugador != "":
        mensaje = jugador + ", su juego fue guardado"
    else:
        mensaje = "Intento guardado"
    messagebox.showinfo("Guardado", mensaje)
tk.Button(ventana, text="Guardar", command=guardar_partida).grid(row=4, column=1)
def cargar_partida():
    global tablero
    cargado = cargar_tablero("guardado.txt")
    tablero.clear()
    for fila in cargado:
        tablero.append(fila)
    dibujar()
tk.Button(ventana, text="Cargar", command=cargar_partida).grid(row=5, column=1)
tk.Button(ventana, text="Ver ranking", command=mostrar_ranking).grid(row=6, column=1)
def finalizar():
    if jugador != "":
        guardar_ranking(jugador, puntos)
    ventana.destroy()
tk.Button(ventana, text="Finalizar", command=finalizar).grid(row=7, column=1)

def dibujar():
    canvas.delete("all")
    for i in range(23):
        y = i * tam_celda
        canvas.create_line(0, y, 12 * tam_celda, y, fill="#222222")
    for j in range(13):
        x = j * tam_celda
        canvas.create_line(x, 0, x, 22 * tam_celda, fill="#222222")
    for i in range_precario(0, len_precario(tablero)):
        for j in range_precario(0, len_precario(tablero[0])):
            tipo = tablero[i][j]
            x1 = j * tam_celda
            y1 = i * tam_celda
            img = imagenes_piezas.get(tipo)
            if img is not None and tipo != "0":
                canvas.create_image(x1, y1, anchor="nw", image=img)
            elif tipo != "0":
                color = colores_piezas.get(tipo, "black")
                x2 = x1 + tam_celda
                y2 = y1 + tam_celda
                canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#888888", width=2)
    for i in range_precario(0, len_precario(pieza_actual)):
        for j in range_precario(0, len_precario(pieza_actual[0])):
            if pieza_actual[i][j] != "0":
                tipo = pieza_actual[i][j]
                x1 = (columna_pieza + j) * tam_celda
                y1 = (fila_pieza + i) * tam_celda
                img = imagenes_piezas.get(tipo)
                if img is not None:
                    canvas.create_image(x1, y1, anchor="nw", image=img)
                else:
                    color = colores_piezas.get(tipo, "black")
                    x2 = x1 + tam_celda
                    y2 = y1 + tam_celda
                    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#444444", width=2)

def mover_izquierda(evento):
    global columna_pieza
    if puede_colocar(tablero, pieza_actual, fila_pieza, columna_pieza - 1):
        columna_pieza = columna_pieza - 1
        dibujar()
def mover_derecha(evento):
    global columna_pieza
    if puede_colocar(tablero, pieza_actual, fila_pieza, columna_pieza + 1):
        columna_pieza = columna_pieza + 1
        dibujar()
def bajar():
    global fila_pieza, pieza_actual, tablero, puntos, columna_pieza
    if puede_colocar(tablero, pieza_actual, fila_pieza + 1, columna_pieza):
        fila_pieza = fila_pieza + 1
    else:
        colocar_pieza(tablero, pieza_actual, fila_pieza, columna_pieza)
        tablero, nuevos = eliminar_lineas_completas(tablero)
        puntos = puntos + nuevos
        etiqueta_puntos.config(text="Puntos: " + str(puntos))
        nueva = random_precario(obtener_tetrominos_con_id())
        if puede_colocar(tablero, nueva, 1, 4):
            pieza_actual.clear()
            for f in nueva:
                pieza_actual.append(f)
            fila_pieza = 1
            columna_pieza = 4
        else:
            etiqueta_puntos.config(text="Juego terminado. Puntos: " + str(puntos))
            if jugador != "":
                guardar_ranking(jugador, puntos)
            canvas.create_text(150, 250, text="FIN DEL JUEGO", fill="red", font=("Arial", 20))
            return
    dibujar()
    ventana.after(obtener_velocidad(puntos), bajar)
def bajar_manual(evento):
    global fila_pieza
    if puede_colocar(tablero, pieza_actual, fila_pieza + 1, columna_pieza):
        fila_pieza = fila_pieza + 1
        dibujar()
def rotar(evento):
    global pieza_actual, columna_pieza
    rotada = rotar_pieza(pieza_actual)
    if puede_colocar(tablero, rotada, fila_pieza, columna_pieza):
        pieza_actual.clear()
        for fila in rotada:
            pieza_actual.append(fila)
        dibujar()
        return
    if puede_colocar(tablero, rotada, fila_pieza, columna_pieza - 1):
        columna_pieza = columna_pieza - 1
        pieza_actual.clear()
        for fila in rotada:
            pieza_actual.append(fila)
        dibujar()
        return
    if puede_colocar(tablero, rotada, fila_pieza, columna_pieza + 1):
        columna_pieza = columna_pieza + 1
        pieza_actual.clear()
        for fila in rotada:
            pieza_actual.append(fila)
        dibujar()
        return

ventana.bind("<Left>", mover_izquierda)
ventana.bind("<Right>", mover_derecha)
ventana.bind("<Down>", bajar_manual)
ventana.bind("<Up>", rotar)

if __name__ == "__main__":
    dibujar()
    ventana.after(obtener_velocidad(puntos), bajar)
    ventana.mainloop()
