lista_1 = ["h","o","l","a"," ","m","u","n","d","o"]
lista_2 = ["h","o","l","a"," ","l","u","n","a"]
lista_3 = []
lista_4 = []

for letra in lista_1:
    for letra2 in lista_2:
        if(letra == letra2):
            lista_3.append(letra2)
            
"""Lista sin filtar"""     
print (lista_3)
lista_4 = lista_3

"""Lista filtrada"""
for letra in lista_3:
    if lista_3.count(letra) > 1:
        lista_3.remove(letra)

print(lista_3)