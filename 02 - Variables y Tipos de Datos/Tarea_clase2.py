## 1)Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
a=5
print(a)
## 2) Imprimir el tipo de dato de la constante 8.5
type(8.5)
print(type(8.5))
## 3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(a))
## 4) Crear una variable que contenga tu nombre
nombre= "Maciela"
## 5) Crear una variable que contenga un número complejo
n_complejo= 1 + 1j
print(type(n_complejo))
## 6) Imprimir el tipo de dato de la variable creada en el punto 5
print(type(nombre))
## 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
pi= 3.1415
## 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
variable1= "True"
veriable2= True
## 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print(type(variable1))
print(type(veriable2))
## 10) Asignar a una variable, la suma de un número entero y otro decimal
b=2  #entero
c=3.5 #decimal
d=b+c #suma de entero y decimal
print(d)
## 11) Realizar una operación de suma de números complejos
c1= 1+3j
c2= 3+3j
print(c1+c2)
## 12) Realizar una operación de suma de un número real y otro complejo
print(c+ c1)
## 13) Realizar una operación de multiplicación
print(b*c)
## 14) Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)
## 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
variable3= 27/4
print(variable3)
## 16) De la división anterior solamente mostrar la parte entera
rta16= 24//4
print(rta16)
## 17) De la división de 27 entre 4 mostrar solamente el resto
rta17= 27%4
print(rta17)
## 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print(4*rta16 + rta17) #algortimo de la division
## 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
variable4= "Soy"
variable5= "Henry"
print(variable4 + variable5)
## 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
x= "2"
y=2
print("2"==2) 
## 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
x=int(x)
print(x)
print(x==y)
## 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
# f=float('3,8') # Arroja error porque no se puede convertir una cadena de caracteres a un numero decimal
# print(f)
## 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
g = 3
g -= 1
print(g) 
## 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
1<<2  # significa mover a 1 2 bit a la izquierda
print(1<<2) 
1>>2 # significa mover a 1 2 bit a la derecha
print(1>>2) 
## 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
# 2 + '2' # no se puede sumar un numero entero con una cadena de caracteres. Arrojaría otro resultado si hacemos, por ejemplo que "2" sea un entero, ambos float, o 2 int. 
print(float(2) + float("2"))
print(2 + int("2") )
print(str(2) + "2")  

## 26) Realizar una operación válida entre valores de tipo entero y string
print("hola"*2)
## si quiero cambiar la coma por un punto utilizo replace(",",".") Ejemplo: "3,8"
l="3,8"
l=l.replace(",",".")
print(l)
