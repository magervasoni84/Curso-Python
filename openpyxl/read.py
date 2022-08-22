import openpyxl

book = openpyxl.load_workbook("C:\Programacion\Curso Python\openpyxl\prueba.xlsx")

sheet = book.active
#Lectura de los 
A1 = sheet["A1"]
A2 = sheet["A2"]

print(A1.value)
print(A2.value)
print(type(A1.value))

#Otro metodo directo de lectura

sheet2 = book["hoja2"]
print(sheet2["A1"].value)
sheet2["A1"] = "Esto es una reescritura"

book.save("C:\Programacion\Curso Python\openpyxl\prueba.xlsx")