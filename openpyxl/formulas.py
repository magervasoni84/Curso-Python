import openpyxl

book = openpyxl.load_workbook("C:\Programacion\Curso Python\openpyxl\prueba.xlsx")

sheet = book.active

sheet["E1"] = "Suma Total"
#Para realizar las funciones se coloca como string y de la misma forma que en excel usando "=", para indicar funcion
sheet["E2"] = "=SUM(B2:B14)"

book.save("C:\Programacion\Curso Python\openpyxl\prueba.xlsx")