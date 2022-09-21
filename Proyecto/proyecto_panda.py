import pandas as pd
import tkinter
import pyautogui        

ancho, alto = pyautogui.size()
print(ancho)
print(alto)

data = {"nombre":[],
        "apellido":[]
        }

df = pd.DataFrame(data, columns = ["nombre", "apellido"])


def saveData():
    None
    nombre = cajanombre.get()
    apellido = cajaapellido.get()
    data = {"nombre": nombre,
            "apellido": apellido
            }
    df = pd.DataFrame(data, columns = ["nombre", "apellido"])

    df.to_csv('C:\Programacion\Curso Python\Proyecto\example.csv')


window = tkinter.Tk()
window.title("Gestor")
#tamaño original de la ventana en px
window.config(width=400, height=300)


#Esto es un label nombre
etiqueta = tkinter.Label(window, text="nombre", bg= "blue")
etiqueta.place(x= 40, y= 20)

cajanombre = tkinter.Entry(window)
cajanombre.place(x= 90, y=20)


#Esto es un label apellido
etiqueta = tkinter.Label(window, text="apellido", bg= "blue")
etiqueta.place(x= 40, y= 50)

cajaapellido = tkinter.Entry(window)
cajaapellido.place(x= 90, y=50)







#creacion de un boton Grabar
boton = tkinter.Button(text="Grabar Datos", command= saveData)
boton.place(x= 300, y= 20)

window.mainloop()