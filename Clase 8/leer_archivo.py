
#Metodo read
""" f = open("C:\Programacion\Curso Python\Clase 8\otro.txt", "r")
content = f.read()
print(content)
f.close() """

#Metodo readline
""" f = open("C:\Programacion\Curso Python\Clase 8\otro.txt", "r")
print(f.readline())
f.close() """

#Metodo readlines
f = open("C:\Programacion\Curso Python\Clase 8\otro.txt", "r")
for line in f.readlines():
    print(line)
f.close()