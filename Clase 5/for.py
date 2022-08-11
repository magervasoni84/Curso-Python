lista = [0,1,12,3,4]
for num in lista:
    print("Numero en lista es :", num)
    num *= 5
    print("Ahora valgo n*5", num)

print("aca esta el valor 3 ", lista[3])


print("---------------------------------")

numeros = [0,1,2,3,4,5,6]
for numero in numeros:
    numeros[numero] *= 5
    print(numeros)

print("---------------------------------")

indice = 0
numeros = [0,1,2,3,4,5,6]
for numero in numeros:
    numeros[indice] *= 5
    indice +=1
    print(numeros)