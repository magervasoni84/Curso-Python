
import json 

data={}
data["cliente"] = []

data["cliente"].append({
    "nombre" : "Mariano",
    "apellido": "Gervasoni",
    "edad": 37,
    "domicilio": "Moron"
})
data["cliente"].append({
    "nombre" : "Cintia",
    "apellido": "Benitez",
    "edad": None,
    "domicilio": "Moron"
})


print(data)

with open("C:\\Programacion\\Curso Python\\Clase 8\\archivo.json", "w") as file:
    json.dump(data, file, indent = 4)