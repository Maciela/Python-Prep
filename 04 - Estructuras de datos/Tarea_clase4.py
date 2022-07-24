# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

mi_lista = ["Paris", "Alemania", "Noruega", "Estados Unidos", "Canada"]
print(mi_lista)

# 2) Imprimir por pantalla el segundo elemento de la lista

print(mi_lista[1])

# 3) Imprimir por pantalla del segundo al cuarto elemento

print(mi_lista[1:4])

# 4) Visualizar el tipo de dato de la lista

print(type(mi_lista))

#  5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

print(mi_lista[2:])

# 6) Visualizar los primeros 4 elementos de la lista

print(mi_lista[:4])

# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
# Si coloco los dos cambios al mismo tiempo salta erro, pero puedo ejecutarlo uno a la vez
mi_lista.append("Paris")
mi_lista.append("Tokio")
print(mi_lista)

# 8) Agregar otra ciudad, pero en la cuarta posición

mi_lista.insert(3,"Roma")
print(mi_lista) 

# 9) Concatenar otra lista a la ya creada

mi_lista2 = [1,2,3,4,5]
mi_lista.extend(mi_lista2)
print(mi_lista)

# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

print(mi_lista.index("Paris"))

# 11) ¿Qué pasa si se busca un elemento que no existe?
#print(mi_lista.index("hola")) 
# salta error porque el elemento no existe.

# 12) Eliminar un elemento de la lista

mi_lista.remove(1)

# 13) ¿Qué pasa si el elemento a eliminar no existe?

#mi_lista.remove("chau") : salta error porque el elemento no existe.
print(mi_lista)

# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

a =  mi_lista.pop()
print(a)

# 15) Mostrar la lista multiplicada por 4

print(mi_lista*4)

