lista=[66, -3, 35, 96]

for num in enumerate(lista):
    print(num)

print("-------------------------------------------------------------------------")


""" Agregando un valor, el index arranca desde el valor ingresado  """
for num in enumerate(lista, 9):
    print(num)

print("-------------------------------------------------------------------------")

#---Pos, elem


for indice, numero in enumerate(lista):
    print(f"INDICE: {indice}")
    print(f"Numero: {numero}\n ")
    print(f"--------->{lista[indice]}\n----------------------------------------------------------------")

