#re <<- Regular Expresion 


import re
import requests


def codigoHtml(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }
    resp = requests.get(url, headers = headers)
    return resp.text


reglaDeBusqueda = r'_self">(.+)</a></h2>'

titles = [m for m in re.findall(reglaDeBusqueda, codigoHtml("https://www.laprensa.com.ar"))]

print(titles)


print("----------------------------------------------------------")
#ejercicio: Obtener los link

reglaDeBusquedaEjercicio = r'href=[\'"]?([^\'" >]+)'

link = [m for m in re.findall(reglaDeBusqueda, codigoHtml("https://www.laprensa.com.ar"))]

print(link)