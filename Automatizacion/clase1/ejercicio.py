
import requests
import os
# Nos traemos un pequeño dataset (con info falsa) tomado de este excelente video: https://youtu.be/K8L6KVGG-7o
# Hacemos un request (spoiler alert: vamos a ver más de esto la próxima clase 😉)
r = requests.get('https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python-Regular-Expressions/data.txt')
texto = r.text

""" Ejercicios

    Crear una carpeta datos.
    Dentro de esta nueva carpeta, crear diferentes carpetas para nombres, telefono , emails, y código de estado extraidos del texto.
    Seleccionar solo los numeros de telefono que empiecen con 2 o con 3.
    Guardar en formato txt un archivo en cada carpeta con la data correspondiente
    (TIP: Agreguen saltos de linea "\n" luego de cada entrada).

BONUS 🥇

Escribir una expresion regular con la que se obtengan todas las URLs """
path = os.getcwd() 
print(path)
os.chdir(path)
if not os.path.exists(path):
    os.mkdir('C:\Programacion\Curso Python\Automatizacion\clase1\data')
    os.chdir('C:\Programacion\Curso Python\Automatizacion\clase1\data')