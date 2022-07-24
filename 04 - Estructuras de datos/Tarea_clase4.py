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

mi_lista2 = ["Haiti","Argentina","Chile","New York","Brasil"]
mi_lista.extend(mi_lista2)
print(mi_lista)

# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

print(mi_lista.index("Paris"))

# 11) ¿Qué pasa si se busca un elemento que no existe?
#print(mi_lista.index("hola")) 
# salta error porque el elemento no existe.

# 12) Eliminar un elemento de la lista

mi_lista.remove("Brasil")

# 13) ¿Qué pasa si el elemento a eliminar no existe?

#mi_lista.remove("chau") : salta error porque el elemento no existe.
print(mi_lista)

# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

a =  mi_lista.pop()
print(a)

# 15) Mostrar la lista multiplicada por 4

print(mi_lista*4)

# 16) Crear una tupla que contenga los números enteros del 1 al 20
mi_tupla = tuple(range(1,21))
print(mi_tupla)
print(type(mi_tupla))

# 17) Imprimir desde el índice 10 al 15 de la tupla
print( mi_tupla[10:15])

# 18) Evaluar si los números 20 y 30 están dentro de la tupla

print( 20 in mi_tupla)
print( 30 in mi_tupla)

#  19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

#Paris ="Paris" in mi_lista
#print(Paris)

elemento = "Paris"
if (not(elemento in mi_lista)):
    mi_lista.append(elemento)
    print("El elemento no existe, se agregó")
else:
    print("El elemento ya existe")  

# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

print(mi_tupla.count(20))
print(mi_lista.count("Mendoza"))

# 21) Convertir la tupla en una lista
conver_mi_tupla = list(mi_tupla)
print(conver_mi_tupla)
print( type(conver_mi_tupla))

# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
var1,var2,var3 = mi_tupla[:3]	
print("Var1:",var1, " Var2:", var2, " Var3:", var3)

# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

mi_diccionario = {"Ciudad" : mi_lista ,"Continente" : ["Europa", "Asia" , "America", "Africa", "Asia"] , " Idiomas": ["ingles", "español", "frances"]}
print(mi_diccionario)

# 24) Imprimir las claves del diccionario

print(mi_diccionario.keys())

#  25) Imprimir las ciudades a través de su clave
print(mi_diccionario["Ciudad"])
