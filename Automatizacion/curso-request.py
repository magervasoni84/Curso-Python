import requests

sitioWeb = "https://es.wikipedia.org/wiki/Yamato_(1941)"

#Request sin Headers
resultado = requests.get(sitioWeb)
codigoHtml = resultado.text

print(codigoHtml[:1000])





# httpbin es una pagina para testear pedidos HTTP, en particular la siguiente URL nos devuelve nuestro header.
url = 'http://httpbin.org/headers' 
resp = requests.get(url)

print('------------------------------')
print('Respuesta sin headers')
print(resp.text)

print('------------------------------')
print('Respuesta con headers')
nuestros_headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
resp_con_headers = requests.get(url, headers = nuestros_headers)
print(resp_con_headers.text)