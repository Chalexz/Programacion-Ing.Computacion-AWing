import tkinter as tk
# --- functions ---
def on_click(widget):
 print("Botón apretao'")
 if widget['image'] == "pyimage1":
    widget['image'] = "pyimage2"
    print("De blanco a amarillo")
 elif widget['image'] == "pyimage2":
    widget['image'] = "pyimage3"
    print("De amarillo a rojo")
 else:
    if widget['image'] == "pyimage3":
        widget['image'] = "pyimage1"
        print("De Rojo a Blanco")
# --- main ---
root = tk.Tk()
img1 = tk.PhotoImage(file="smile-1.png")
img2 = tk.PhotoImage(file="smile-2.png")
img3 = tk.PhotoImage(file="smile-3.png")

for y in range(14):
 for x in range(6):
    button = tk.Button(root, image=img1)
    button['command'] = lambda arg=button:on_click(arg)
    button.grid(row=y, column=x)

root.mainloop() 

