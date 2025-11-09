'''
PROYECTO SUPER HERMANO MAURICIO

TALLER DE PROGRAMACION | S2-2025

POR: ALEXANDER WING

╭∩╮(-_-)╭∩╮
'''

import tkinter as tk

#==============================================( MENU PRINCIPAL )==============================================================#

root = tk.Tk() 
root.title("Hermano Mauricio")
root.geometry("700x600")


menu_principal = tk.Frame(root, bg="#000000")
menu_principal.pack(fill="both", expand=True)

menu_principal.columnconfigure(0, weight=1)
menu_principal.rowconfigure(0, weight=1)
menu_principal.rowconfigure(1, weight=1)

titulo_menu_principal = tk.Label(menu_principal, text="ᗒ MENU PRINCIPAL ᗕ"
                                 , fg="white", bg="#000000", font=("Roboto", 18, "bold"))
titulo_menu_principal.grid(row=0, rowspan=2, column=0, sticky="ew")

#==============================================BOTON INICIAR JUEGOs

btn_iniciar_juego = tk.Button(menu_principal, text="INICIAR JUEGO" )
btn_iniciar_juego.grid(row=2, column=0,padx=50, pady=70, sticky="nsew")
btn_iniciar_juego.configure(bg="#3A3636", fg="white", font="Roboto",
                            activebackground="#4B4747", activeforeground="white",
                            highlightthickness=0)

#==============================================BOTON VER RANKING

btn_ver_ranking = tk.Button(menu_principal, text="VER RANKING")
btn_ver_ranking.grid(column=0, row=3, padx=50, pady=70, sticky="nsew")
btn_ver_ranking.configure(bg="#3A3636", fg="white", font="Roboto",
                          activebackground="#4B4747", activeforeground="white",
                          highlightthickness=0)

root.mainloop()
#==============================================( MENU PRINCIPAL )==============================================================#





