# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

mi_lista=[]
mi_lista.extend(range(-15,0))
print(mi_lista)

# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?
tope_rango = len(mi_lista)
n= -15
while(n> tope_rango):
    if(n%2==0):
        print(n)
    n+=1

# 3) Resolver el punto anterior sin utilizar un ciclo while
for elemento in mi_lista:
    if(elemento%2==0):
        print(elemento)

# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos
#forma 1
for i in mi_lista[:3]: # el iterable es la lista los iteradores son : for, while y iter. 
    print(i)
#forma 2
n=0
while(n<3):
    print(mi_lista[n])
    n+=1
#forma 3
marcador= iter(mi_lista)
print(next(marcador))
print(next(marcador))
print(next(marcador))

# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

for i , c in enumerate(mi_lista):
    print(i, c)

# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

lista = [1,2,5,7,8,10,13,14,15,17,20]
# forma 1, sin utilizar ciclos
elementos_faltantes = [3,4,6,9,11,12,16,18,19]
lista.extend(elementos_faltantes)
lista.sort()
print(lista)


# forma 2 , utilizando cilo for
for i in range(1,21):
    if i not in lista:
        lista.append(i)
        lista.sort()
        
    else:
        continue
print(lista)
    

#forma 3 , utilizando cilo while
n=1
while n<21:
    if n not in lista:
        lista.append(n)
        lista.sort()
       
    n+=1
print(lista)

# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: 
# Crear una lista con los primeros treinta números de la sucesión

#forma 1:
lista_Fibbonacci=[0,1]
n=2
while(n<30):
    i=lista_Fibbonacci[n-1]+lista_Fibbonacci[n-2]
    lista_Fibbonacci.append(i)
    n+=1
print(lista_Fibbonacci)

#forma 2:
    
fibonacci=[]
n=0
while (n<30):
    if n==0 or n==1:
        fibonacci.append(n)
    else:
        ni=fibonacci[n-1]+fibonacci[n-2]
        fibonacci.append(ni)
    n+=1
print(fibonacci)

#forma 3:
su =[]
n=0
n0=0
n1=1
for n in range(0,30):
    if n==0:
        su.append(n0)
    elif n==1:
        su.append(n1)
    else:
        l=su[n-1]+su[n-2]
        su.append(l)
  
print(su)

# 8) Realizar la suma de todos elementos de la lista del punto anterior
print(sum(fibonacci))
print(sum(fibonacci[10:21])) #miltiplo de 11 (la suma de diez numeros consecutivos de la sucesion es multiplo de 11)

# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
n=len(fibonacci)
for i in range(n-5,n):
    print( "la división entre:" , fibonacci[i-1] ," y" , fibonacci[i], "es: ", (fibonacci[i-1])/(fibonacci[i]))
   
#corrección de la resoclución propuesta en el prep

primeros = 15
n = primeros - 5
while(n < primeros):
    print("la división estre ",fibonacci[n-1], "y ", fibonacci[n], "es :" , fibonacci[n-1]/fibonacci[n])
    n += 1

# 11) Crear un diccionario e imprimir sus claves utilizando un iterador
dic ={"Nombre": ["Maciela", "Ivan", "Juan"], "Edad": [20, 21, 22] , "Apellidos": ["Perez", "Lopez", "Sanchez"]}

print(dic.keys())

#12) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
#cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
enes= [ i for i in cadena if i=="n" ]
print(enes)
print(len(enes))

cadena = list(cadena)
print(type(cadena))

for i , c in enumerate(cadena):
    
        print(i, c)


# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

Nombres = ["Maciela", "Ivan", "Juan"]
Apellidos = ["Ortiz" , "Millan", " Perez"]
Nombres_Apellidos = zip(Nombres, Apellidos)
print(type(Nombres_Apellidos))

print(list(Nombres_Apellidos))

# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7
#lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lis_div = [i for i in lis if i%7==0]
print(lis_div)

# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
cantidad = 0
for i in lis:
    if type(i) == list:
        cantidad += len(i)
    else:
        cantidad += 1
print(cantidad)


# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

n=0
while n<len(lis):
    if type(lis[n]) != list:
        lis[n] = [lis[n]]
    n+=1
print(lis)

#for indice, elemento in enumerate(lis):
#    if (type(elemento) != list):
#        lis[indice]=[elemento]
#print(lis)
