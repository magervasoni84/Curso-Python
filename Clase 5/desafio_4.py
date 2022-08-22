
num = int(input("Cuantos numeros queres ingresar?: "))
aux = 0
aux2 = 0
suma = 0

while(aux < num):
    aux2 = int(input("Ingresa el numero: ")) 
    suma += aux2
    aux += 1

""" for i in range(num)
        aux2 = int(input("Ingresa el numero: ")) 
        suma += aux2 """

print("La media es", float(suma/aux))

""" Probar de hacerlo con sum() """