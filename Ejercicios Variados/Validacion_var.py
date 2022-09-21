""" 
def par_o_impar(num):
    if num%2 == 0:
        return "Par"
    else:
        return "Impar"

number = input("Ingrese un numero: ")

while (number.isdigit() == False):
    if (number.isdigit() == False):
            number = input("El valor ingresado no es numérico. Intente nuevamente: ")

number = int(number)

print(par_o_impar(number))
 """



""" def validacion(var):
    print (type(var))
    while type(var) == str:
        print ("Aca estoy")
    else:
        print ("Aca estoy y esta errado")

validacion(5) """


""" 
def par_o_impar(numero):
    print(type(numero))
    while type(numero) == int:
        
        if (numero % 2 == 0):
            return "El número es par"
        else:
            return "El número es impar"
    else:
        
        print("El dato debe ser un número.")
        numero = input("Ingrese un número: ")



print(par_o_impar(input("Ingrese un número: "))) """



print('')
def par_o_impar(num):
    while (num.isdigit() == False):
        num = input("no ingreso un numero, por favor ingrese uno: ")
    if(num==int and num % 2==0): 
        print(f' Ha ingresado {num}, su numero es impar ')
    else: 
        print(f' Ha ingresado {num}, su numero es par ')

        
par_o_impar((input('Ingrese un numero: ')))