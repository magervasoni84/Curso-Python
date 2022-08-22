nombre = "Mariano alberto"
apellido = "Gervasoni"


f = open("C:\Programacion\Curso Python\Clase 8\otro.txt", "w")
persona = {
    "Nombre" : nombre ,
    "apellido" : apellido
    }  


for dato in persona.keys():
    persona[dato] = input(f'Ingrese {dato}:')

f.close