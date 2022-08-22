
""" Declaro la variable """
""" grupo = set() """
grupo = {"Miguel", "Blanca", "Mario", "Andres"}  
print(grupo)
grupo.update({"Ana", "Ramon", "Marta", "Eric", "David"})
print(grupo)

#Borrado, como se haria para borrar 3 elementos en una sola vez

grupo.remove({"Mario", "Miguel", "Esteban"})
""" grupo.discard("Mario")
grupo.discard("Miguel")
grupo.discard("Esteban") """
print(grupo)