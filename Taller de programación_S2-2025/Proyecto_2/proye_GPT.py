# PROYECTO SUPER HERMANO MAURICIO | S2-2025
# Viewport 8x10, Mario grande, ranking, goombas, hongo verde, estrella con temporizador

import tkinter as tk
from tkinter import simpledialog, messagebox
import os, time, random

# ====== rutas (sin pathlib) ======
BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR   = os.path.join(BASE_DIR, "assets")
MAPAS_FILE   = os.path.join(BASE_DIR, "mapas.txt")
RANKING_FILE = os.path.join(BASE_DIR, "ranking.txt")

# ====== pillow opcional ======
try:
    from PIL import Image, ImageTk
    _PIL_OK = True
except Exception:
    _PIL_OK = False

# ====== tablero y viewport ======
FILAS = 16
COLS  = 20
TILE  = 48         # casilla grande (sprites se escalan)
VIEW_F = 8
VIEW_C = 10
ANCHO  = VIEW_C * TILE
ALTO   = VIEW_F * TILE

# ====== estado global ======
root = tk.Tk()
root.title("SUPER HERMANO MAURICIO")

menu_principal = tk.Frame(root, bg="#000000")
juego          = tk.Frame(root, bg="#101010")
menu_principal.pack(fill="both", expand=True)

canvas = tk.Canvas(juego, width=ANCHO, height=ALTO, bg="black",
                   highlightthickness=0, bd=0)
panel  = tk.Frame(juego, bg="#181818")
canvas.grid(row=0, column=0, padx=8, pady=8)
panel.grid(row=0, column=1, sticky="ns", padx=(0,8), pady=8)

lbl_info   = tk.Label(panel, text="Info de partida", fg="white", bg="#181818", font=("Arial", 12, "bold"))
lbl_modo   = tk.Label(panel, text="Modo: -",         fg="white", bg="#181818")
lbl_cuad   = tk.Label(panel, text="Cuadrante: -",    fg="white", bg="#181818")
lbl_tiempo = tk.Label(panel, text="Tiempo: 00:00",   fg="white", bg="#181818")
lbl_mov    = tk.Label(panel, text="Movimientos: 0",  fg="white", bg="#181818")
lbl_rojos  = tk.Label(panel, text="Rojos: 0/0",      fg="white", bg="#181818")
lbl_verdes = tk.Label(panel, text="Hongos verdes: 0 (F para activar)", fg="white", bg="#181818")
lbl_estrella = tk.Label(panel, text="Estrella: –",   fg="#ffd23f", bg="#181818", font=("Arial", 10, "bold"))
for w in (lbl_info, lbl_modo, lbl_cuad, lbl_tiempo, lbl_mov, lbl_rojos, lbl_verdes, lbl_estrella):
    w.pack(pady=4)
lbl_info.pack_configure(pady=(0,10))

btn_activar_verde = tk.Button(panel, text="Activar Hongo Verde (F)", command=lambda: activar_hongo_verde())
btn_reiniciar     = tk.Button(panel, text="Reiniciar",               command=lambda: reiniciar_partida())
btn_abandonar     = tk.Button(panel, text="Abandonar",               command=lambda: abandonar_partida())
btn_volver_menu   = tk.Button(panel, text="Volver al menú",          command=lambda: mostrar_menu())
for b in (btn_activar_verde, btn_reiniciar, btn_abandonar, btn_volver_menu):
    b.pack(pady=6)

# variables de partida
matriz = []
pos_mario = [0,0]
goombas = []
total_rojos = 0
rojos_tomados = 0
verdes_stock = 0
verde_activo = False
estrella_hasta_ms = 0
estrella_flag = False   # <-- estrella solo si se recogió la celda 4
movimientos = 0

# viewport
view_r0 = 0
view_c0 = 0

# control ciclo
modo = "normal"
inicio_ms = 0
limite_seg = 180
tick_id = None
goomba_id = None
estrella_tick_id = None
juego_activo = False

# ====== sprites ======
SPRITES = {}
SPRITES_REQUERIDOS = {
    "ground":      "ground",
    "wall":        "wall",
    "mario":       "mario",
    "mario_verde": "mario_verde",
    "mario_star":  "mario_estrella",
    "mario_mix":   "mario_mix",
    "mush_red":    "mush_red",
    "mush_green":  "mush_green",
    "star":        "star",
    "princess":    "princess",
    "goomba":      "goomba",
}

# --------------------------------------------------------------------------------------
'''
entrada: nombre base
salida: ruta o none
restricción: busca png/gif en assets
objetivo: localizar archivo del sprite
'''
def _buscar_asset(nombre_base):
    for ext in (".png", ".gif"):
        p = os.path.join(ASSETS_DIR, nombre_base + ext)
        if os.path.exists(p): return p
    try:
        for fname in os.listdir(ASSETS_DIR):
            base, ext = os.path.splitext(fname)
            if ext.lower() in (".png",".gif") and base.lower()==nombre_base.lower():
                return os.path.join(ASSETS_DIR, fname)
    except Exception:
        pass
    return None

'''
entrada: photo y tamaño meta
salida: photo escalada
restricción: usa zoom/subsample si calza
objetivo: ajustar sprite al tamaño de casilla
'''
def _scale_tk(photo, target):
    try: w, h = photo.width(), photo.height()
    except Exception: return photo
    if w==target and h==target: return photo
    if w%target==0 and h%target==0: return photo.subsample(w//target, h//target)
    if target%w==0 and target%h==0: return photo.zoom(target//w, target//h)
    return photo

'''
entrada: nombre base
salida: PhotoImage o none
restricción: usa pillow si está
objetivo: cargar sprite del disco
'''
def cargar_sprite(nombre_base):
    ruta = _buscar_asset(nombre_base)
    if not ruta: return None
    if _PIL_OK:
        try:
            img = Image.open(ruta)
            try: img.seek(0)
            except: pass
            img = img.convert("RGBA").resize((TILE,TILE), Image.NEAREST)
            return ImageTk.PhotoImage(img)
        except Exception:
            return None
    else:
        try:
            ph = tk.PhotoImage(file=ruta)
            return _scale_tk(ph, TILE)
        except Exception:
            return None

'''
entrada: nada
salida: bool
restricción: todos los sprites deben existir
objetivo: asegurar recursos antes de jugar
'''
def cargar_todos_los_sprites_obligatorios():
    global SPRITES
    faltan=[]
    SPRITES={}
    for k, base in SPRITES_REQUERIDOS.items():
        img = cargar_sprite(base)
        if img is None: faltan.append(f"{base}.png/.gif")
        SPRITES[k] = img
    if faltan:
        messagebox.showerror("Faltan sprites",
            "No se encontraron estos archivos en /assets:\n\n" +
            "\n".join(faltan))
        return False
    return True

# --------------------------------------------------------------------------------------
'''
entrada: nada
salida: ms actuales
restricción: ninguna
objetivo: manejar timers
'''
def ahora_ms(): return int(time.time()*1000)

'''
entrada: seg int
salida: "mm:ss"
restricción: seg>=0
objetivo: mostrar tiempo humano
'''
def fmt_mmss(seg): seg=max(0,int(seg)); return f"{seg//60:02d}:{seg%60:02d}"

'''
entrada: r, c
salida: 1..4
restricción: cortes 8 y 10
objetivo: saber cuadrante
'''
def cuadrante_de(r,c):
    if r<8 and c<10: return 1
    if r<8 and c>=10: return 2
    if r>=8 and c<10: return 3
    return 4

'''
entrada: nada
salida: nada
restricción: usa pos_mario
objetivo: encuadrar viewport al cuadrante de mario
'''
def ajustar_view_a_mario():
    global view_r0, view_c0
    view_r0 = (pos_mario[0]//VIEW_F)*VIEW_F
    view_c0 = (pos_mario[1]//VIEW_C)*VIEW_C

'''
entrada: nada
salida: bool
restricción: usa view_r0/c0
objetivo: saber si mario salió del viewport
'''
def mario_fuera_de_view():
    return not (view_r0 <= pos_mario[0] < view_r0+VIEW_F and
                view_c0 <= pos_mario[1] < view_c0+VIEW_C)

'''
entrada: nada
salida: nada
restricción: fija tamaño ventana
objetivo: geometría compacta del menú
'''
def ajustar_geometry_menu():
    root.update_idletasks()
    w = 420; h = 320
    root.geometry(f"{w}x{h}")
    root.minsize(w,h)
    root.resizable(False, False)

'''
entrada: nada
salida: nada
restricción: usa medidas de canvas/panel
objetivo: geometría compacta del juego
'''
def ajustar_geometry_juego():
    root.update_idletasks()
    panel_w = max(panel.winfo_reqwidth(), 260)
    w = ANCHO + panel_w + 8 + 8 + 8
    h = max(ALTO + 16, panel.winfo_reqheight()+16)
    root.geometry(f"{w}x{h}")
    root.minsize(w,h)
    root.resizable(False, False)

# ====== menú principal ======
'''
entrada: nada
salida: nada
restricción: widgets tk básicos
objetivo: armar el menú
'''
def construir_menu():
    menu_principal.columnconfigure(0, weight=1)
    for r in (0,1,2,3,4):
        menu_principal.rowconfigure(r, weight=1)

    tk.Label(menu_principal, text="ᗒ MENÚ PRINCIPAL ᗕ",
             fg="white", bg="#000000", font=("Arial", 18, "bold")
             ).grid(row=1, column=0, sticky="ew")

    tk.Button(menu_principal, text="INICIAR JUEGO",
              width=22, bg="#3A3636", fg="white",
              activebackground="#4B4747", activeforeground="white",
              highlightthickness=0, font=("Arial", 12),
              command=lambda: abrir_selector_modo()
              ).grid(row=2, column=0, padx=20, pady=10, sticky="ew")

    tk.Button(menu_principal, text="VER RANKING",
              width=22, bg="#3A3636", fg="white",
              activebackground="#4B4747", activeforeground="white",
              highlightthickness=0, font=("Arial", 12),
              command=lambda: ver_ranking()
              ).grid(row=3, column=0, padx=20, pady=(0,10), sticky="ew")

    tk.Button(menu_principal, text="SALIR",
              width=22, bg="#7a2b2b", fg="white",
              activebackground="#923636", activeforeground="white",
              highlightthickness=0, font=("Arial", 12),
              command=root.destroy
              ).grid(row=4, column=0, padx=20, pady=(0,16), sticky="ew")

    ajustar_geometry_menu()

'''
entrada: nada
salida: nada
restricción: toplevel modal
objetivo: elegir modo de juego
'''
def abrir_selector_modo():
    sel = tk.Toplevel(root)
    sel.title("Elegir modo de juego")
    sel.resizable(False, False)
    sel.transient(root); sel.grab_set()

    marco = tk.Frame(sel, bg="#111")
    marco.pack(padx=16, pady=16)

    tk.Label(marco, text="Seleccione el modo", fg="white", bg="#111",
             font=("Arial", 13, "bold")).pack(pady=(0,10))

    tk.Button(marco, text="MODO NORMAL",
              width=24, bg="#3A3636", fg="white",
              activebackground="#4B4747", activeforeground="white",
              command=lambda: elegir_modo("normal", sel)
              ).pack(pady=6)

    tk.Button(marco, text="MODO CONTRATIEMPO (3 min)",
              width=24, bg="#3A3636", fg="white",
              activebackground="#4B4747", activeforeground="white",
              command=lambda: elegir_modo("contratiempo", sel)
              ).pack(pady=6)

    sel.protocol("WM_DELETE_WINDOW", sel.destroy)

'''
entrada: modo y ventana
salida: nada
restricción: cierra selector
objetivo: preparar juego con ese modo
'''
def elegir_modo(modo_elegido, ventana_selector):
    ventana_selector.destroy()
    preparar_modo(modo_elegido)

# ====== cargar mapa y arrancar ======
'''
entrada: modo
salida: nada
restricción: sprites y mapas deben existir
objetivo: cargar recursos y pedir mapa
'''
def preparar_modo(m):
    global modo, limite_seg
    modo = m
    limite_seg = 180 if modo == "contratiempo" else 0

    if not cargar_todos_los_sprites_obligatorios():
        return

    n = contar_mapas_en_archivo(MAPAS_FILE)
    if n == 0:
        messagebox.showerror("Error", "No se encontraron mapas válidos en 'mapas.txt'.")
        return

    idx = simpledialog.askinteger("Seleccionar mapa",
                                  f"Hay {n} mapas disponibles.\nElija el que quiere jugar (1..{n}):",
                                  minvalue=1, maxvalue=n, parent=root)
    if not idx:
        return

    if cargar_mapa_desde_txt(MAPAS_FILE, idx):
        iniciar_juego()

'''
entrada: ruta
salida: cantidad mapas
restricción: 16 filas x 20 cols por mapa
objetivo: contar mapas en archivo
'''
def contar_mapas_en_archivo(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            lineas = [ln.strip() for ln in f.readlines()]
    except Exception:
        return 0

    bloques = 0; fila = 0
    for ln in lineas:
        if not ln: continue
        partes = ln.split()
        if len(partes) != COLS: continue
        if not all(x.lstrip("-").isdigit() for x in partes): continue
        fila += 1
        if fila == FILAS:
            bloques += 1; fila = 0
    return bloques

'''
entrada: ruta e índice
salida: bool
restricción: valores válidos de celdas
objetivo: cargar mapa y entidades
'''
def cargar_mapa_desde_txt(ruta, indice):
    global matriz, pos_mario, goombas, total_rojos, rojos_tomados
    global verdes_stock, verde_activo, estrella_hasta_ms, estrella_flag, movimientos
    global view_r0, view_c0

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            lineas = [ln.strip() for ln in f.readlines()]
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo leer mapas.txt:\n{e}")
        return False

    bloques=[]; actual=[]
    for ln in lineas:
        if not ln: continue
        partes = ln.split()
        if len(partes)!=COLS: continue
        try: fila_nums=[int(x) for x in partes]
        except: continue
        actual.append(fila_nums)
        if len(actual)==FILAS:
            bloques.append(actual); actual=[]

    if indice<1 or indice>len(bloques):
        messagebox.showerror("Error", f"No existe el mapa #{indice}.")
        return False

    matriz = bloques[indice-1]
    pos_mario=[0,0]; goombas=[]; total_rojos=0; rojos_tomados=0
    verdes_stock=0; verde_activo=False; estrella_hasta_ms=0; estrella_flag=False; movimientos=0

    mario_ok=False
    for r in range(FILAS):
        for c in range(COLS):
            v=matriz[r][c]
            if v==2 and not mario_ok:
                pos_mario=[r,c]; matriz[r][c]=0; mario_ok=True
            elif v==3: total_rojos+=1
            elif v==7: goombas.append([r,c]); matriz[r][c]=0

    if not mario_ok:
        messagebox.showerror("Error","El mapa no contiene Mario (valor 2).")
        return False

    ajustar_view_a_mario()
    return True

# ====== ciclo juego ======
'''
entrada: nada
salida: nada
restricción: detiene timers
objetivo: volver al menú
'''
def mostrar_menu():
    global juego_activo
    detener_bucles()
    juego_activo = False
    juego.pack_forget()
    menu_principal.pack(fill="both", expand=True)
    ajustar_geometry_menu()

'''
entrada: nada
salida: nada
restricción: requiere mapa cargado
objetivo: iniciar partida y timers
'''
def iniciar_juego():
    global inicio_ms, juego_activo, estrella_flag
    menu_principal.pack_forget()
    juego.pack(fill="both", expand=True)
    ajustar_geometry_juego()
    root.focus_set()

    juego_activo = True
    estrella_flag = False
    lbl_modo.config(text=f"Modo: {modo}")
    lbl_mov.config(text="Movimientos: 0")
    lbl_rojos.config(text=f"Rojos: 0/{total_rojos}")
    lbl_estrella.config(text="Estrella: –")
    lbl_tiempo.config(text="Tiempo: 00:00" if modo=="normal" else f"Tiempo: {fmt_mmss(limite_seg)}")
    _refrescar_cuadrante()

    inicio_ms = ahora_ms()
    arrancar_reloj()
    arrancar_goombas()
    arrancar_temporizador_estrella()
    dibujar_tablero()

'''
entrada: nada
salida: nada
restricción: cancela afters
objetivo: parar reloj, goombas y estrella
'''
def detener_bucles():
    global tick_id, goomba_id, estrella_tick_id
    if tick_id is not None:
        try: root.after_cancel(tick_id)
        except: pass
        tick_id=None
    if goomba_id is not None:
        try: root.after_cancel(goomba_id)
        except: pass
        goomba_id=None
    if estrella_tick_id is not None:
        try: root.after_cancel(estrella_tick_id)
        except: pass
        estrella_tick_id=None

'''
entrada: nada
salida: nada
restricción: confirmación
objetivo: recargar modo y mapa
'''
def reiniciar_partida():
    if messagebox.askyesno("Reiniciar", "¿Reiniciar y elegir mapa otra vez?"):
        preparar_modo(modo)

'''
entrada: nada
salida: nada
restricción: ninguna
objetivo: terminar partida sin guardar
'''
def abandonar_partida():
    detener_bucles()
    mostrar_estadisticas("Abandono")

'''
entrada: nada
salida: nada
restricción: usa modo
objetivo: actualizar reloj principal
'''
def arrancar_reloj():
    global tick_id
    if not juego_activo: return
    if modo == "normal":
        seg = (ahora_ms() - inicio_ms)//1000
        lbl_tiempo.config(text=f"Tiempo: {fmt_mmss(seg)}")
    else:
        seg_trans = (ahora_ms() - inicio_ms)//1000
        restante = limite_seg - seg_trans
        lbl_tiempo.config(text=f"Tiempo: {fmt_mmss(restante)}")
        if restante <= 0:
            perder("Time's Up"); return
    tick_id = root.after(1000, arrancar_reloj)

'''
entrada: nada
salida: nada
restricción: juego_activo true
objetivo: mover goombas periódicamente
'''
def arrancar_goombas():
    global goomba_id
    if not juego_activo: return
    mover_goombas()
    goomba_id = root.after(300, arrancar_goombas)

# ====== temporizador estrella ======
'''
entrada: nada
salida: nada
restricción: juego_activo true
objetivo: refrescar contador de estrella
'''
def arrancar_temporizador_estrella():
    global estrella_tick_id
    if not juego_activo: return
    actualizar_label_estrella()
    estrella_tick_id = root.after(200, arrancar_temporizador_estrella)

'''
entrada: nada
salida: nada
restricción: usa estrella_flag/tiempo
objetivo: pintar segundos o guión
'''
def actualizar_label_estrella():
    global estrella_flag
    if es_estrella_activa():
        restante = max(0, (estrella_hasta_ms - ahora_ms())/1000.0)
        lbl_estrella.config(text=f"Estrella: {restante:0.1f} s")
    else:
        if estrella_flag and ahora_ms() >= estrella_hasta_ms:
            estrella_flag = False
        lbl_estrella.config(text="Estrella: –")

# ====== input y lógica ======
'''
entrada: nada
salida: bool
restricción: compara con ahora_ms
objetivo: saber si la estrella sigue activa
'''
def es_estrella_activa():
    return estrella_flag and (ahora_ms() < estrella_hasta_ms)

'''
entrada: nada
salida: nada
restricción: stock>0 y no activo
objetivo: activar hongo verde y descontar 1
'''
def activar_hongo_verde():
    global verde_activo, verdes_stock
    if not juego_activo: return
    if verde_activo:     return
    if verdes_stock <= 0: return
    verdes_stock -= 1
    verde_activo = True
    actualizar_info(); dibujar_tablero()

'''
entrada: dr, dc
salida: nada
restricción: respeta paredes y efectos
objetivo: mover a mario y procesar celdas
'''
def intentar_mover(dr, dc):
    global movimientos
    if not juego_activo: return
    r, c = pos_mario
    nr, nc = r+dr, c+dc
    if not (0 <= nr < FILAS and 0 <= nc < COLS): return
    destino = matriz[nr][nc]

    if destino == 1:
        if verde_activo:
            nnr, nnc = nr+dr, nc+dc
            if 0 <= nnr < FILAS and 0 <= nnc < COLS and matriz[nnr][nnc] != 1:
                pos_mario[0], pos_mario[1] = nnr, nnc
                consumir_verde_y_recolectar()
                if mario_fuera_de_view():
                    ajustar_view_a_mario(); dibujar_tablero()
            return
        return

    pos_mario[0], pos_mario[1] = nr, nc
    movimientos += 1
    recoger_en(nr, nc)
    if mario_fuera_de_view():
        ajustar_view_a_mario()
    actualizar_info(); dibujar_tablero(); verificar_gane_y_choque()

'''
entrada: nada
salida: nada
restricción: solo si verde_activo true
objetivo: gastar verde tras salto de pared
'''
def consumir_verde_y_recolectar():
    global verde_activo, movimientos
    if not juego_activo: return
    verde_activo = False
    movimientos += 1
    r, c = pos_mario
    recoger_en(r, c)
    if mario_fuera_de_view():
        ajustar_view_a_mario()
    actualizar_info(); dibujar_tablero(); verificar_gane_y_choque()

'''
entrada: r, c
salida: nada
restricción: lee valor de matriz
objetivo: aplicar efectos por celda
'''
def recoger_en(r,c):
    global rojos_tomados, verdes_stock, estrella_hasta_ms, estrella_flag
    v = matriz[r][c]
    if v == 3:
        rojos_tomados += 1; matriz[r][c] = 0
    elif v == 5:
        verdes_stock += 1; matriz[r][c] = 0
    elif v == 4:
        estrella_flag = True
        estrella_hasta_ms = ahora_ms() + 5000  # 5 s
        matriz[r][c] = 0
        actualizar_label_estrella()

'''
entrada: nada
salida: nada
restricción: revisa goombas y meta
objetivo: detectar perder o ganar
'''
def verificar_gane_y_choque():
    if not juego_activo: return
    r, c = pos_mario
    if [r,c] in goombas and not es_estrella_activa():
        perder("Choque con Goomba"); return
    if matriz[r][c] == 6 and rojos_tomados == total_rojos:
        ganar()

'''
entrada: nada
salida: nada
restricción: goombas no atraviesan paredes
objetivo: mover goombas hacia mario
'''
def mover_goombas():
    global goombas
    if not juego_activo or not goombas: return

    nuevas=[]; ocupadas=set(tuple(g) for g in goombas)
    mr, mc = pos_mario

    for gr,gc in goombas:
        vecinos=[]
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr, nc = gr+dr, gc+dc
            if 0<=nr<FILAS and 0<=nc<COLS and matriz[nr][nc]!=1:
                vecinos.append((nr,nc))

        se_movio=False
        for (nr,nc) in vecinos:
            if (nr,nc)==(mr,mc):
                nuevas.append([nr,nc]); ocupadas.add((nr,nc)); se_movio=True
                if not es_estrella_activa():
                    perder("Choque con Goomba")
                    return
                break
        if se_movio: continue

        elegido=(gr,gc)
        if vecinos:
            dist_actual=abs(gr-mr)+abs(gc-mc)
            if random.random()<0.5:
                mejores=[]
                for (nr,nc) in vecinos:
                    if abs(nr-mr)+abs(nc-mc) < dist_actual:
                        mejores.append((nr,nc))
                if mejores:
                    random.shuffle(mejores)
                    for cand in mejores:
                        if cand not in ocupadas:
                            elegido=cand; break
            if elegido==(gr,gc):
                random.shuffle(vecinos)
                for cand in vecinos:
                    if cand not in ocupadas and cand!=(mr,mc):
                        elegido=cand; break

        nuevas.append([elegido[0],elegido[1]])
        ocupadas.add(elegido)

    goombas=nuevas
    dibujar_tablero(); verificar_gane_y_choque()

'''
entrada: motivo
salida: nada
restricción: solo una vez
objetivo: terminar por derrota
'''
def perder(motivo):
    global juego_activo
    if not juego_activo: return
    juego_activo = False
    detener_bucles()
    mostrar_estadisticas(motivo)

'''
entrada: nada
salida: nada
restricción: guarda ranking
objetivo: terminar por victoria
'''
def ganar():
    global juego_activo
    if not juego_activo: return
    juego_activo = False
    detener_bucles()
    nombre = simpledialog.askstring("¡Ganaste!", "Ingresa tu nombre:", parent=root)
    if not nombre: nombre = "Anónimo"
    seg = (ahora_ms() - inicio_ms)//1000
    guardar_en_ranking(nombre, seg, rojos_tomados, movimientos)
    mostrar_estadisticas("Gané", nombre)

'''
entrada: nada
salida: nada
restricción: usa pos_mario
objetivo: refrescar etiqueta de cuadrante
'''
def _refrescar_cuadrante():
    lbl_cuad.config(text=f"Cuadrante: {cuadrante_de(pos_mario[0], pos_mario[1])}")

'''
entrada: nada
salida: nada
restricción: usa globals
objetivo: refrescar panel
'''
def actualizar_info():
    lbl_mov.config(text=f"Movimientos: {movimientos}")
    lbl_rojos.config(text=f"Rojos: {rojos_tomados}/{total_rojos}")
    lbl_verdes.config(text=f"Hongos verdes: {verdes_stock} (F para activar)")
    _refrescar_cuadrante()

# ====== dibujo ======
'''
entrada: nada
salida: photo de mario
restricción: depende de estrella/verde
objetivo: sprite correcto de mario
'''
def sprite_para_mario():
    if es_estrella_activa() and verde_activo: return SPRITES["mario_mix"]
    if es_estrella_activa():                  return SPRITES["mario_star"]
    if verde_activo:                          return SPRITES["mario_verde"]
    return SPRITES["mario"]

'''
entrada: nada
salida: nada
restricción: solo viewport
objetivo: pintar mapa, goombas y mario
'''
def dibujar_tablero():
    canvas.delete("all")
    r0, c0 = view_r0, view_c0
    for vr in range(VIEW_F):
        r = r0 + vr
        for vc in range(VIEW_C):
            c = c0 + vc
            x, y = vc*TILE, vr*TILE
            v = matriz[r][c]
            if v == 1:
                canvas.create_image(x, y, image=SPRITES["wall"], anchor="nw")
            else:
                canvas.create_image(x, y, image=SPRITES["ground"], anchor="nw")
            if v == 3: canvas.create_image(x, y, image=SPRITES["mush_red"],   anchor="nw")
            if v == 5: canvas.create_image(x, y, image=SPRITES["mush_green"], anchor="nw")
            if v == 4: canvas.create_image(x, y, image=SPRITES["star"],       anchor="nw")
            if v == 6: canvas.create_image(x, y, image=SPRITES["princess"],   anchor="nw")

    for gr,gc in goombas:
        if r0 <= gr < r0+VIEW_F and c0 <= gc < c0+VIEW_C:
            x, y = (gc-c0)*TILE, (gr-r0)*TILE
            canvas.create_image(x, y, image=SPRITES["goomba"], anchor="nw")

    mr, mc = pos_mario
    if r0 <= mr < r0+VIEW_F and c0 <= mc < c0+VIEW_C:
        x, y = (mc-c0)*TILE, (mr-r0)*TILE
        canvas.create_image(x, y, image=sprite_para_mario(), anchor="nw")

    canvas.create_rectangle(1,1, ANCHO-2, ALTO-2, outline="#444")

# ====== ranking ======
'''
entrada: resultado, seg, nombre
salida: texto
restricción: simple
objetivo: armar estadística
'''
def mostrar_estadísticas_texto(resultado, seg, nombre=None):
    lineas = []
    if nombre: lineas.append(f"Nombre: {nombre}")
    lineas += [
        f"Resultado: {resultado}",
        f"Tiempo: {fmt_mmss(seg)}",
        f"Hongos rojos: {rojos_tomados}/{total_rojos}",
        f"Movimientos: {movimientos}",
    ]
    return "\n".join(lineas)

'''
entrada: resultado, nombre
salida: nada
restricción: fin de partida
objetivo: mostrar datos y volver al menú
'''
def mostrar_estadisticas(resultado, nombre=None):
    if modo == "normal":
        seg = (ahora_ms() - inicio_ms)//1000
    else:
        seg_trans = (ahora_ms() - inicio_ms)//1000
        seg = 180 if resultado=="Time's Up" else seg_trans
    messagebox.showinfo("Estadísticas", mostrar_estadísticas_texto(resultado, seg, nombre))
    mostrar_menu()

'''
entrada: nombre, t, rojos, movs
salida: nada
restricción: archivo ranking.txt
objetivo: guardar línea
'''
def guardar_en_ranking(nombre, tiempo_seg, rojos, movimientos_):
    try:
        with open(RANKING_FILE, "a", encoding="utf-8") as f:
            f.write(f"{tiempo_seg};{nombre};{rojos};{movimientos_}\n")
    except Exception as e:
        messagebox.showwarning("Aviso", f"No se pudo escribir ranking:\n{e}")

'''
entrada: nada
salida: ventana top 10
restricción: si no hay, avisa
objetivo: ver mejores registros
'''
def ver_ranking():
    datos = []
    if os.path.exists(RANKING_FILE):
        try:
            with open(RANKING_FILE, "r", encoding="utf-8") as f:
                for ln in f:
                    ln=ln.strip()
                    if not ln: continue
                    partes=ln.split(";")
                    if len(partes)!=4: continue
                    try: t=int(partes[0])
                    except: continue
                    datos.append((t, partes[1], partes[2], partes[3]))
        except: pass

    datos.sort(key=lambda x: x[0])
    top = datos[:10]

    win = tk.Toplevel(root); win.title("Ranking Top 10")
    txt = tk.Text(win, width=50, height=18); txt.pack(padx=10, pady=10)
    txt.insert("end", "Tiempo   |  Nombre         | Rojos | Movs\n")
    txt.insert("end", "-------------------------------------------\n")
    if not top:
        txt.insert("end", "No hay partidas en el ranking aún.\n")
    else:
        for t,n,roj,mv in top:
            txt.insert("end", f"{fmt_mmss(t):8} | {n[:14]:14} | {roj:>5} | {mv:>4}\n")
    txt.config(state="disabled")

# ====== binds ======
root.bind("<Up>",    lambda e: intentar_mover(-1, 0))
root.bind("<Down>",  lambda e: intentar_mover( 1, 0))
root.bind("<Left>",  lambda e: intentar_mover( 0,-1))
root.bind("<Right>", lambda e: intentar_mover( 0, 1))
root.bind("<f>",     lambda e: activar_hongo_verde())
root.bind("<F>",     lambda e: activar_hongo_verde())

# ====== run ======
'''
entrada: nada
salida: nada
restricción: inicio app
objetivo: levantar menú
'''
def construir_todo():
    construir_menu()

construir_todo()
root.mainloop()
