#Primero hay que instalar paquete xlrd
#haciendo pip install openpyxl en la consola

#Se realiza la importacionde los modulos
from openpyxl import Workbook
#Modulo para modificar fuentes
from openpyxl.styles import Font 
import time


#Inicializamos el Workbook
book = Workbook()
#Hoja de trabajo
sheet = book.active
#Escritura de datos
sheet["A1"] = 5
sheet["A2"] = 10

#Escritura de un string en la posicion B1, cambiando color y fuente
sheet["B1"] = "rango"
sheet["B1"].font = Font(color="FF0000", bold = True)

#Insertar valores en rangos B2 al B14 por ejemplo, recordando que range va al -1
for i in range(2, 15):
    sheet[f"B{i}"]  = i**2

#Creacion de una nueva hoja y escritura de texto y horario en A1 y A2 respectivamente
sheet2 = book.create_sheet("hoja2")
sheet2["A1"] = "Texto Random"
# %X da la hora, %x la fecha
fecha = time.strftime("%x")
sheet2["A2"] = fecha

#Combinar celdas
sheet3 = book.create_sheet("hoja3")
sheet3.merge_cells("A1:D1")
sheet3["A1"] = "Prueba de union de celdas"
#Para sacar la combinacion
#sheet3.unmerge_cells("A1:D1")

#Poner la ruta completa, sino explota
book.save("C:\Programacion\Curso Python\openpyxl\prueba.xlsx")
