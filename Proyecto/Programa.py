
#ttk control tematico, sino control clasico es tk
from tkinter import Menu, ttk
import tkinter

import os

print(os.getcwd())

def hola():
    print("Hola")

ventana = tkinter.Tk()
ventana.title("Programa de Prueba")
#tamaño original de la ventana en px
ventana.config(width=400, height=300)

#Esto es un label
etiqueta = tkinter.Label(ventana, text="Probando el Label", bg= "blue")
etiqueta.place(x= 40, y= 20)

#creacion de un boton
boton = ttk.Button(text="Hola mundo")
boton.place(x= 40, y= 50)

#Esto es un label
etiqueta2 = tkinter.Label(ventana, text="Probando el Label", bg = "red")
etiqueta2.pack(fill = tkinter.BOTH, expand = True)
etiqueta2.place(x= 40, y= 80)

#configuracion de styles para 
s = ttk.Style()
s.configure("Rojo.TButton", foregrounf="#ff0000")
botonRojo = ttk.Button(text="Este es boton rojo", style="Rojo.TButton")
botonRojo.place(x= 40, y= 110)

#las funciones se conectan con los botones por medio de command
#con () se corre al inicializarse pero no al hacer click
#para pasar parametros se hace command= lambda: hola("variable")
botonHola = ttk.Button(text= "Dijo Hola", command = hola)
botonHola.place(x= 40, y= 140)


#Se llama una funcion en el boton que toma el contenido de caja texto y lo imprime

def textoDeCaja(): 
    texto = cajaTexto.get()
    etiqueta["text"] = texto
    print(texto)

botonTexto = tkinter.Button(ventana, text="click para imprimir texto", command = textoDeCaja)
botonTexto.place(x= 40, y= 170)

cajaTexto = tkinter.Entry(ventana)
cajaTexto.place(x= 40, y=200)

etiqueta = tkinter.Label(ventana)
etiqueta.place(x=40, y= 230)


import helloworld

import openpyxl #Write/read excel


window = tkinter.Tk()
window.title("Programa de Prueba")
#tamaño original de la ventana en px
window.config(width=500, height=400)


menu = Menu(window)

#Menu 1
menu1 = Menu(menu)
menu.add_cascade(label='File', menu=menu1)


#Submenus menu menu1
menu1.add_command(label='New')
menu1.add_separator() #Separador
menu1.add_command(label='Edit')


#Menu pacientes
pacientes = Menu(menu)
menu.add_cascade(label='pacientes', menu=pacientes)

#Submenus menu menu1
pacientes.add_command(label='New', command=helloworld.hello)
pacientes.add_command(label='Edit')






window.config(menu=menu)



ventana.mainloop()


ventana2 = tkinter.Tk()
ventana2.title("Programa de Prueba")
#tamaño original de la ventana en px
ventana2.config(width=400, height=300)
#metodo Grilla
boton1= tkinter.Button(ventana2, text="boton1")
boton2= tkinter.Button(ventana2, text="boton2")
boton3= tkinter.Button(ventana2, text="boton3")

boton1.grid(row= 0, column=0)
boton2.grid(row= 1, column=1)
boton3.grid(row= 2, column=2
)

ventana2.mainloop()
