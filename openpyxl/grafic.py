
from openpyxl import Workbook
from openpyxl.chart import ScatterChart, Reference, Series

book = Workbook()
sheet = book.active

#Ingresos rangos de valores a graficar
for i in range(1, 15):
    sheet[f"A{i}"] = i
for i in range(1, 15):
    sheet[f"B{i}"] = i*10


c1 = ScatterChart()
#Titulo 
c1.tittle = "grafico de dispersion"
#Style de la linea
c1.style = 13
#Titulos ejes
c1.y_axis.title = "Eje Y"
c1.x_axis.title = "Eje X"
#Valores de los ejes
xvalues = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=14)
yvalues = Reference(sheet, min_col=2, min_row=1, max_col=1, max_row=14)
#Creamos la serie
ser = Series(yvalues, xvalues, title = "recta")
c1.series.append(ser)
#Se agrega la grafica con posicionamieto inicial D3
sheet.add_chart(c1, "D3")

book.save("C:\Programacion\Curso Python\openpyxl\prueba_grafica.xlsx")