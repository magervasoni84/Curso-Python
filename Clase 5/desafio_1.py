


while(1):
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    print("Ingrese la opcion elegida: ")
    print("A: Mostrar suma de numeros")
    print("B: Mostrar resta de numeros")
    print("C: Mostrar multiplicacion de numeros")
    print("D: Salir")
    eleccion = input("Eleccion: ")
    if(eleccion == "A"):
        print("La suma es: ", num1 + num2)
    if(eleccion == "B"):
        print("La suma es: ", num1 - num2)
    if(eleccion == "C"):
        print("La suma es: ", num1 * num2)
    if(eleccion == "D"):
        print("Saliendo del Programa")
        break 
    if(eleccion != "A" and eleccion != "B" and eleccion != "C" and eleccion != "D"):
        print("Eleccion incorrecta")        