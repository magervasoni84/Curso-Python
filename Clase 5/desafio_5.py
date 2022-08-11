
num = int(input("Ingresa un numero de 0 a 9: "))
aux = False

while((num < 0) or (num > 9)):
    num = int(input("De 0 a 9 te dije: "))

lista = [1,3,6,9]
""" for numero in lista:
    if num == numero:
        aux = True """

aux = lista.index(num)

print("Esta el numero esta en la posicion ", aux)