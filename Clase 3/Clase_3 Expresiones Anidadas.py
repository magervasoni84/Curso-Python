
nombre = input("Ingrese la nombre: ")
edad = int(input("Ingrese la edad: "))

aux = nombre != "****" and (10 < edad < 18) and (3 <= len(nombre) < 10) and (edad*4> 40)

print (aux)