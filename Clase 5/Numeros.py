
""" Uso basico del While """

num = int(input("Ingrese el numero, con 0 se sale: "))
suma = 0

while num != 0:
    suma = suma + num
    num = int(input("Ingrese el numero, con 0 se sale: "))

print("La suma es: " + str(suma))


