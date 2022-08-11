

nombre = input("Ingrese el nombre")
fan = input("Ingresa que te gusta Marvel:M o CapCom:C")

A = ()
B = ()

nombre_cap=nombre.capitalize()

print(nombre_cap[0])
if nombre_cap <="M" and fan == "M":
    A = nombre

if nombre_cap <="N" and fan == "C":
    B = nombre


print(A(0))
print(B(0))