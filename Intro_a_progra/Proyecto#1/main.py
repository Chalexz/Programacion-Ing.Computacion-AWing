"""
                                PROYECTO #1 de Intro de Progra
Por: Alexander Wing Rojas 
Entrega: 20/5/2025
1er semestre, 2025

"""

import tkinter as tk
from tkinter import messagebox, simpledialog
from auxi import crear_matriz_asientos, contar_asientos_ocupados, contar_asientos_libres, total_asientos
from data import salas, sala_id_counter
from logica import *
import os

imagenes = []

'''
e: canvas de tkinter y matriz de asientos
s: dibuja los asientos en el canvas
r: matriz debe tener al menos una fila y una columna
'''
def mostrar_asientos(canvas, matriz):
    canvas.delete("all")
    filas = len(matriz)
    columnas = len(matriz[0])

    root = canvas.winfo_toplevel()
    root.update_idletasks()
    screen_h = root.winfo_screenheight()
    screen_w = root.winfo_screenwidth()
    max_canvas = min(screen_h - 120, screen_w - 120)
    canvas_size = max_canvas if max_canvas > 400 else 400

    pantalla_img = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "assets", "pantalla.png"))
    pantalla_w = pantalla_img.width()
    pantalla_h = pantalla_img.height()
    if pantalla_w > canvas_size - 40:
        factor = pantalla_w // (canvas_size - 40) + 1
        pantalla_img = pantalla_img.subsample(factor, factor)
        pantalla_w = pantalla_img.width()
        pantalla_h = pantalla_img.height()

    margen_superior = pantalla_h + 30
    margen_izquierdo = 80
    area_util = canvas_size - margen_superior - 40

    cell_size = int(min(area_util / max(filas, columnas), 100))
    matriz_ancho = columnas * cell_size
    matriz_alto = filas * cell_size

    offset_x = (canvas_size - matriz_ancho) // 2
    offset_y = margen_superior

    canvas.config(width=canvas_size, height=canvas_size)

    pantalla_x = (canvas_size - pantalla_w) // 2
    canvas.create_image(pantalla_x, 10, image=pantalla_img, anchor="nw")
    canvas.pantalla_img = pantalla_img

    global silla_verde, silla_roja
    silla_verde_img = silla_verde
    silla_roja_img = silla_roja
    silla_w = silla_verde.width()
    silla_h = silla_verde.height()
    max_silla = int(cell_size * 0.7)
    factor_w = silla_w // max_silla + 1 if silla_w > max_silla else 1
    factor_h = silla_h // max_silla + 1 if silla_h > max_silla else 1
    if factor_w > 1 or factor_h > 1:
        silla_verde_img = silla_verde.subsample(factor_w, factor_h)
        silla_roja_img = silla_roja.subsample(factor_w, factor_h)
    silla_size_w = silla_verde_img.width()
    silla_size_h = silla_verde_img.height()

    for j in range(columnas):
        x = offset_x + j * cell_size + cell_size // 2
        canvas.create_text(x, offset_y - 25, text=str(j+1), font=("Arial", 14, "bold"), fill="black")

    for i in range(filas):
        y = offset_y + i * cell_size + cell_size // 2
        canvas.create_text(offset_x - 30, y, text=chr(65+i), font=("Arial", 14, "bold"), fill="black")

    for i in range(filas):
        for j in range(columnas):
            x = offset_x + j * cell_size
            y = offset_y + i * cell_size
            canvas.create_rectangle(x, y, x+cell_size, y+cell_size, outline="#222", width=2)
            silla_x = x + (cell_size - silla_size_w)//2
            silla_y = y + (cell_size - silla_size_h)//2
            sprite = silla_verde_img if matriz[i][j] == " " else silla_roja_img
            canvas.create_image(silla_x, silla_y, image=sprite, anchor="nw")
            canvas.create_text(x + cell_size//2, y + cell_size - 8, text=f"{chr(65+i)}{j+1}", font=("Arial", 10, "bold"), fill="#333")
            imagenes.append(sprite)
    canvas.sillas_verdes = silla_verde_img
    canvas.sillas_rojas = silla_roja_img

'''
e: root de tkinter
s: muestra la ventana principal con los botones del menú
r: root debe ser una ventana de tkinter válida
'''
def acciones_principales(root):
    import data
    global silla_verde, silla_roja
    ruta_base = os.path.dirname(__file__)
    silla_verde = tk.PhotoImage(file=os.path.join(ruta_base, "assets", "Silla verde Cine.png"))
    silla_roja = tk.PhotoImage(file=os.path.join(ruta_base, "assets", "Silla roja Cine.png"))

    '''
    e: 
    s: crea una sala nueva y la agrega a la lista
    r: filas y columnas deben ser mayores a 0
    '''
    def crear_sala():
        try:
            filas = int(simpledialog.askstring("Crear Sala", "¿De cuántas filas quiere que sea la sala?"))
            columnas = int(simpledialog.askstring("Crear Sala", "¿De cuántas columnas quiere que sea la sala?"))
            if filas < 1 or columnas < 1:
                raise Exception()
            matriz = crear_matriz_asientos(filas, columnas)
            data.salas.append(["Sin asignar", 0, matriz, 0, data.sala_id_counter])
            messagebox.showinfo("Listo", f"Bien! Sala {data.sala_id_counter} creada")
            data.sala_id_counter += 1
        except:
            messagebox.showerror("Error", "Entrada inválida")

    '''
    e: 
    s: asigna una película y precio a una sala existente
    r: sala debe existir, nombre no vacío, precio >= 0
    '''
    def asignar_pelicula():
        try:
            if not salas:
                messagebox.showinfo("Info", "Primero vaya cree una sala (ㆆ _ ㆆ)")
                return
            sala_id = int(simpledialog.askstring("Sala", "ID de sala:"))
            sala = buscar_sala_por_id(sala_id, salas)
            if sala:
                nombre = simpledialog.askstring("Película", "Nombre:")
                if not nombre or nombre.strip() == "":
                    raise Exception()
                precio = int(simpledialog.askstring("Precio", "Precio:"))
                if precio < 0:
                    raise Exception()
                sala[0] = nombre
                sala[1] = precio
                messagebox.showinfo("Éxito", "Se asignó la película")
            else:
                messagebox.showerror("Error", "Sala no encontrada.")
        except:
            messagebox.showerror("Error", "Mal, datos inválidos")

    '''
    e: 
    s: muestra el estado de los asientos de una sala en una ventana nueva
    r: sala debe existir
    '''
    def ver_estado():
        try:
            if not salas:
                messagebox.showinfo("Info", "Primero vaya cree una sala (ㆆ _ ㆆ)")
                return
            sala_id = int(simpledialog.askstring("Sala", "ID:"))
            sala = buscar_sala_por_id(sala_id, salas)
            if sala:
                filas = len(sala[2])
                columnas = len(sala[2][0])
                cell_size = 60
                margen_superior = 80
                margen_izquierdo = 60
                margen_inferior = 40
                ancho_canvas = margen_izquierdo + columnas * cell_size + 20
                alto_canvas = margen_superior + filas * cell_size + margen_inferior

                top = tk.Toplevel()
                top.title(f"Sala {sala_id} - {sala[0]}")
                canvas = tk.Canvas(top, width=ancho_canvas, height=alto_canvas)
                canvas.pack()
                mostrar_asientos(canvas, sala[2])
                total = total_asientos(sala[2])
                ocupados = contar_asientos_ocupados(sala[2])
                porc = (ocupados / total) * 100 if total > 0 else 0
                tk.Label(top, text=f"Asientos: {total}  Ocupados: {ocupados}  % Ocupación: {porc:.1f}%").pack()
            else:
                messagebox.showerror("Error", "Sala no encontrada.")
        except:
            messagebox.showerror("Error", "Entrada inválida")

    '''
    e: 
    s: reserva un asiento específico en una sala
    r: sala y asiento deben existir, asiento debe estar libre
    '''
    def reservar_asiento_ui():
        try:
            if not salas:
                messagebox.showinfo("Info", "Primero vaya cree una sala (ㆆ _ ㆆ)")
                return
            sala_id = int(simpledialog.askstring("Sala", "ID:"))
            sala = buscar_sala_por_id(sala_id, salas)
            if sala:
                cod = simpledialog.askstring("Asiento", "Ej: A1:")
                if not cod or len(cod) < 2:
                    raise Exception()
                fila = ord(cod[0].upper()) - 65
                columna = int(cod[1:]) - 1
                if fila < 0 or columna < 0 or fila >= len(sala[2]) or columna >= len(sala[2][0]):
                    raise Exception()
                if reservar_asiento(sala, fila, columna):
                    messagebox.showinfo("Reservado", f"Asiento {cod.upper()} reservado")
                else:
                    messagebox.showerror("Ocupado", "Ya está reservado")
            else:
                messagebox.showerror("Error", "Sala no encontrada")
        except:
            messagebox.showerror("Error", "Inválido")

    '''
    e: 
    s: cancela la reserva de un asiento en una sala
    r: sala y asiento deben existir, asiento debe estar reservado
    '''
    def cancelar_asiento_ui():
        try:
            if not salas:
                messagebox.showinfo("Info", "Primero vaya cree una sala (ㆆ _ ㆆ)")
                return
            sala_id = int(simpledialog.askstring("Sala", "ID:"))
            sala = buscar_sala_por_id(sala_id, salas)
            if sala:
                cod = simpledialog.askstring("Asiento", "Ej: A1:")
                if not cod or len(cod) < 2:
                    raise Exception()
                fila = ord(cod[0].upper()) - 65
                columna = int(cod[1:]) - 1
                if fila < 0 or columna < 0 or fila >= len(sala[2]) or columna >= len(sala[2][0]):
                    raise Exception()
                if cancelar_asiento(sala, fila, columna):
                    messagebox.showinfo("Cancelado", f"Reserva del asiento {cod.upper()} cancelada.")
                else:
                    messagebox.showerror("Error", "No estaba reservado.")
            else:
                messagebox.showerror("Error", "Sala no encontrada.")
        except:
            messagebox.showerror("Error", "Entrada inválida")

    '''
    e: 
    s: muestra estadísticas de ocupación de una sala
    r: sala debe existir
    '''
    def ver_estadisticas():
        if not salas:
            messagebox.showinfo("Info", "Primero vaya cree una sala (ㆆ _ ㆆ)")
            return
        sala_id = simpledialog.askstring("Sala", "ID:")
        try:
            sala_id = int(sala_id)
            sala = buscar_sala_por_id(sala_id, salas)
            if sala:
                total = total_asientos(sala[2])
                ocupados = contar_asientos_ocupados(sala[2])
                porc = (ocupados / total) * 100 if total > 0 else 0
                messagebox.showinfo("Estadísticas", f"Sala {sala[4]} - {sala[0]}\nAsientos totales: {total}\nReservados: {ocupados}\nPorcentaje de ocupación: {porc:.2f}%")
            else:
                messagebox.showerror("Error", "Sala no encontrada.")
        except:
            messagebox.showerror("Error", "Entrada inválida")

    '''
    e: 
    s: muestra estadísticas de recaudación de una sala
    r: sala debe existir
    '''
    def ver_recaudacion():
        if not salas:
            messagebox.showinfo("Info", "Primero vaya cree una sala (ㆆ _ ㆆ)")
            return
        sala_id = simpledialog.askstring("Sala", "ID:")
        try:
            sala_id = int(sala_id)
            sala = buscar_sala_por_id(sala_id, salas)
            if sala:
                vendidos = contar_asientos_ocupados(sala[2])
                precio = sala[1]
                total = vendidos * precio
                messagebox.showinfo("Recaudación", f"Sala {sala[4]} - {sala[0]}\nEntradas vendidas: {vendidos}\nPrecio por entrada: {precio}\nTotal recaudado: {total}")
            else:
                messagebox.showerror("Error", "Sala no encontrada")
        except:
            messagebox.showerror("Error", "Entrada inválida")

    '''
    e: 
    s: busca salas por nombre de película y muestra asientos disponibles
    r: nombre no vacío
    '''
    def buscar_pelicula():
        if not salas:
            messagebox.showinfo("Info", "Primero vaya cree una sala (ㆆ _ ㆆ)")
            return
        nombre = simpledialog.askstring("Buscar", "Película:")
        if not nombre:
            messagebox.showinfo("Nada", "No se encontró.")
            return
        encontrado = []
        for s in salas:
            if s[0].lower() == nombre.lower():
                libres = contar_asientos_libres(s[2])
                encontrado.append(f"- Sala {s[4]} (asientos disponibles: {libres})")
        if encontrado:
            messagebox.showinfo("Resultados", f'Salas que proyectan "{nombre}":\n' + "\n".join(encontrado))
        else:
            messagebox.showinfo("Nada", "No se encontró.")

    '''
    e: 
    s: muestra todas las funciones disponibles (cartelera)
    r: debe haber al menos una sala
    '''
    def ver_cartelera():
        if not salas:
            messagebox.showinfo("Cartelera", "Primero vaya genere por lo menos una película (¬_¬)")
            return
        cartelera = []
        for s in salas:
            libres = contar_asientos_libres(s[2])
            total = total_asientos(s[2])
            cartelera.append(
                f"Sala {s[4]} - {s[0]}\nPrecio: {s[1]}\nAsientos totales: {total}\nAsientos disponibles: {libres}\n"
            )
        messagebox.showinfo("Funciones disponibles", "\n".join(cartelera))

    '''
    e: 
    s: reserva varios asientos consecutivos en una fila específica
    r: sala y fila deben existir, cantidad válida, asientos deben estar libres
    '''
    def reservar_lote():
        try:
            if not salas:
                messagebox.showinfo("Info", "Primero vaya cree una sala (ㆆ _ ㆆ)")
                return
            sala_id = int(simpledialog.askstring("Sala", "ID:"))
            sala = buscar_sala_por_id(sala_id, salas)
            if not sala:
                messagebox.showerror("Error", "Sala no encontrada.")
                return
            fila_cod = simpledialog.askstring("Fila", "Letra de la fila (ej: A):")
            if not fila_cod or not fila_cod.isalpha():
                raise Exception()
            fila = ord(fila_cod.upper()) - 65
            if fila < 0 or fila >= len(sala[2]):
                raise Exception()
            cantidad = int(simpledialog.askstring("Cantidad", "Cuántos asientos (hacia la derecha):"))
            if cantidad < 1 or cantidad > len(sala[2][0]):
                raise Exception()
            resultado = reservar_consecutivos_en_fila(sala, fila, cantidad)
            if resultado:
                ini, fin = resultado
                asientos = " ".join([f"{chr(65+fila)}{j+1}" for j in range(ini, fin+1)])
                messagebox.showinfo("Hecho", f"¡Reservados exitosamente: {asientos}!")
            else:
                messagebox.showerror("Error", "No es posible reservar los asientos consecutivos.")
        except:
            messagebox.showerror("Error", "Datos inválidos.")

    '''
    e: 
    s: simula venta masiva en todas las salas según porcentaje
    r: porcentaje entre 1 y 100
    '''
    def simular_ventas():
        try:
            if not salas:
                messagebox.showinfo("Info", "Primero vaya cree una sala (ㆆ _ ㆆ)")
                return
            porcentaje = int(simpledialog.askstring("Porcentaje", "Porcentaje (1-100):"))
            if porcentaje < 1 or porcentaje > 100:
                raise Exception()
            total_reservados = 0
            for sala in salas:
                vendidos = simular_venta_masiva(sala, porcentaje)
                total_reservados += vendidos
            messagebox.showinfo("Listo", f"Se reservó el {porcentaje}% de los asientos en todas las salas.")
        except:
            messagebox.showerror("Error", "Inválido.")

    '''
    e: 
    s: reinicia todos los asientos de una sala
    r: sala debe existir
    '''
    def reiniciar():
        try:
            if not salas:
                messagebox.showinfo("Info", "Primero vaya cree una sala (ㆆ _ ㆆ)")
                return
            sala_id = int(simpledialog.askstring("Sala", "ID:"))
            sala = buscar_sala_por_id(sala_id, salas)
            reiniciar_sala(sala)
            messagebox.showinfo("Hecho", "Sala reiniciada.")
        except:
            messagebox.showerror("Error", "No se pudo.")

    '''
    e: 
    s: muestra ventana de despedida y cierra el programa
    r: ninguna
    '''
    def salir():
        ventana_gracias = tk.Toplevel()
        ventana_gracias.title("Gracias!")
        ventana_gracias.update_idletasks()
        ancho = 420
        alto = 140
        x = (ventana_gracias.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana_gracias.winfo_screenheight() // 2) - (alto // 2)
        ventana_gracias.geometry(f"{ancho}x{alto}+{x}+{y}")
        ventana_gracias.resizable(False, False)
        tk.Label(
            ventana_gracias,
            text="Espero que haya disfrutado la experiencia! \ (•◡•) /",
            font=("Arial", 14),
            wraplength=400,
            justify="center"
        ).pack(expand=True, pady=30)
        ventana_gracias.after(4000, lambda: (ventana_gracias.destroy(), root.destroy()))

    funciones = [
        ("1. Crear Sala", crear_sala),
        ("2. Asignar Película", asignar_pelicula),
        ("3. Ver Estado", ver_estado),
        ("4. Reservar Asiento", reservar_asiento_ui),
        ("5. Cancelar Reserva", cancelar_asiento_ui),
        ("6. Ver Estadísticas de Ocupación", ver_estadisticas),
        ("7. Ver Estadísticas de Recaudación", ver_recaudacion),
        ("8. Buscar por Película", buscar_pelicula),
        ("9. Ver Funciones Disponibles", ver_cartelera),
        ("10. Reservar Lote", reservar_lote),
        ("11. Venta Masiva", simular_ventas),
        ("12. Reiniciar Sala", reiniciar),
        ("13. Salir", salir)
    ]

    frame = tk.Frame(root)
    frame.pack(pady=10)
    for texto, cmd in funciones:
        b = tk.Button(frame, text=texto, width=40, command=cmd)
        b.pack(pady=3)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Poderosísimo Cine Wing")
    acciones_principales(root)
    root.mainloop()
