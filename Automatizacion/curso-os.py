import os

"""
os.system("start mspaint.exe")

 # http://microdatos.dane.gov.co/index.php/catalog/472/get_microdata
!wget -O Expo_2021.zip https://unket.s3.sa-east-1.amazonaws.com/data/Expo_2021.zip
 """

# Devuelve el "current working directory", o directorio actual de trabajo
path = os.getcwd() 

print(path.split("\\"))


# Es por "change directory", o sea cambiar el directorio actual de trabajo
os.chdir(path)

# recorre recursivamente el árbol de directorios, empezando por el path. 
# en cada iteracion devuelve carpeta, [subcarpetas], [archivos]
os.walk(path)

""" # crea un directorio
os.makedirs(path) 

# chequea si existe un path
os.path.exists(path)

# borra un archivo o carpeta vacia
os.remove(path)

# enumera el contenido del path
os.listdir(path)

# permite cambiar paths, nombres y extensiones
os.rename(path, new_path) """

# Devuelve la ruta absoluta de una ruta relativa
os.path.abspath(path)

print(os.path.getsize(path))