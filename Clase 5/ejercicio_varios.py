""" Escribir un programa que enumere los paises de la siguiente lista """
paises = ["Canada", "USA", "Mexico", "Australia", "Argentina", "China", "India"]

for pais in enumerate(paises):
    print(pais)

""" Crear un bucle que sume los pares del 0 al 100 """
num =sum (range(0,101,2))

print(num)
    
""" Imprimir por pantalla los numeros del 1 al 10 al reves """
lista = list(range(10, -1, -1))
print(lista)

""" Pedir a un usuario que ingrese un numero y devuelva la cantidad de numeros """

num=len(input("numero: "))
print(num)
