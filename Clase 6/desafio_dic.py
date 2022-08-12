
animales = {
    "elefante": ""
}

print(animales)

print("---------------------------------------------------------------")
print("Agregado varios, al estar vacio no jode")
animales = {
    "perro": "bobby",
    "tigre": "peepe",
    "mono": "homero"
}

print(animales)


print("---------------------------------------------------------------")
print("Agregar unitariamente, se podra hacerlo todo de una?")
animales["perro"] = "trompis"
animales["delfin"] = "manolo"

print(animales)


print("---------------------------------------------------------------")
print("Haciendo todo de una?")
animales_a_agregar = {
    'auto': '206',
    'avion': 'cesna'
}
animales.update(animales_a_agregar)

print("Haciendo todo de una, otra manera sin usar una lists/tupla")
animales.update({
    "moto":"yamaha",
    "caballo": "ricardito"})



for x in animales:
    print(x)


