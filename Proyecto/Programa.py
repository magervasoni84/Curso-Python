
#ttk control tematico, sino control clasico es tk
from tkinter import ttk

import tkinter as tk

ventana = tk.Tk()
ventana.title("Programa de Prueba")
#tamaño original de la ventana en px
ventana.config(width=400, height=300)


#creacion de un boton
boton = ttk.Button(text="Hola mundo")
boton.place(x= 40, y= 50)

s = ttk.Style()
s.configure("Rojo.TButton", foregrounf="#ff0000")


botonRojo = ttk.Button(text="Este es boton rojo", style="Rojo.TButton")
botonRojo.place(x= 40, y= 100)

ventana.mainloop()