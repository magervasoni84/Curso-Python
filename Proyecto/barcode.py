#Instalamos modulo barcode pip install python-barcode
from barcode import EAN13 
#EAN13  Codigo Europeo
from barcode.writer import ImageWriter


num_of_barcodes = int(input("Cuantos son necesarios hacer?: "))

num = range(num_of_barcodes)

for i in num:
    id = input(" Ingresa 12 digitos para el Barcode: ")
    my_code = EAN13(id, writer=ImageWriter)
    nombre = input("Nombre para el Barcode: ")
    my_code.save(nombre)



#PRoblema con la version del python-barcode...