""" 
Utilizando todo lo que sabes sobre cadenas, listas y sus métodos internos, transforma este texto:
gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió 
Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista """

frase = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó joe castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"

indice = 0
listaf = frase.split("&")
for frase in listaf:
    listaf[indice] = frase.capitalize() 
    if ( frase.find("castiglione")!= -1):  
        listaf[indice] = frase.capitalize().replace("joe castiglione", "Joe Castiglione")
    indice += 1


for frase in listaf:
    print(frase)