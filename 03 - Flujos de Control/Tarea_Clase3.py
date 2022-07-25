## 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

x=2
if (x<0):
    print(x, "es menor a cero")
elif (x>0):
    print(x, "es mayor a cero")

## 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
a=3
b="hola"
if(a==b):
    print("las variables son del mismo tipo de dato")
else:
    print("las variables son de tipos de dato diferentes")
    
## 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
for n in range(1,21): 
    if(n%2==0):
        print(n, "es par")
    else:
        print(n, "es impar")

## 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
for n in range(0,6):
    print(n, "elevado a la 3ra potencia:", n**3)

## 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
n = 12
for i in range(0, n):
    print(i)

## 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
n=3
if (type(n)==int):
    if(n>0):
        factorial=n
        while(n>2):
            n=n-1
            factorial=factorial*n
        print("el factorial es",factorial)
    else:
        print(n, "no es entero positivo") 
else:
    print(n, "no es entero")


## 7) Crear un ciclo for dentro de un ciclo while

n=3
while(n>0):
    for i in range(0,6):
     print("ciclo while nro ",str(n))
     print("ciclo for nro ",str(i))
    n-=1

## 8) Crear un ciclo while dentro de un ciclo for

for i in range(0,6):
    n=3
    while(n>0):
        print("ciclo for nro ",str(i))
        print("ciclo while nro ",str(n))
        n-=1

## 9) Imprimir los números primos existentes entre 0 y 30

n=1
while(n<=30):
    if(n==1):
        print(n, " es primo")
        n+=1
        continue
    elif(n==2):
        print(str(n), " es primo")
        n+=1
        continue
    esPrimo = True
    for i in range(2,n):
        if(n%i==0):
            esPrimo = False
        
            
    if(esPrimo == True):
        print(n, " es primo")
    else:
        print(n, " no es primo")
    n+=1

           
 ## 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

tope_rango=30
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1        
  
## otra forma para el 9 y 10: 
n=0
primo= True
while(n<=30):
    for i in range(2,n):
        if(n%i==0):
            primo=False
            continue 
    if (primo):
        print(n)
    else:
        primo=True
    n+=1
## 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
##evaluación de optimización pto 9: 
contador9_=0
n=1
while(n<=30):
    contador9_+=1
    if(n==1):
        print(n, " es primo")
        n+=1
        continue
   
    elif(n==2):
        print(str(n), " es primo")
        n+=1
        continue
    esPrimo = True
    for i in range(2,n):
        contador9_+=1
        if(n%i==0):
            esPrimo = False 
            break           
    if(esPrimo == True):
        print(n, " es primo")
    else:
        print(n, " no es primo")
    
    n+=1
print("cantidad de iteraciones: ",contador9_)

## Evaluación de optimización pto 10:
contador10_=0
n=0
primo= True
while(n<=30):
    for i in range(2,n):
        contador10_+=1
        if(n%i==0):
            primo=False
            break 
    if (primo):
        print(n)
    else:
        primo=True
    n+=1
print("cantidad de iteraciones: ",contador10_)

## 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
tope_rango=300
n=99
while(n<=tope_rango):
    n+=1
    if(n%12!=0):
        continue
    print(str(n), "es divisible por 12")
  
## 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

n= input("ingrese un numero: ")
n= int(n)
primo= True
salir = ""
while True: 
    for i in range(2,n):
        if(n%i==0):
            primo=False
            break
    if(primo==True):
        print(n, "es primo")
        while True: 
            salir= input("¿Desea buscar el siguiente primo? (si/no)")
            if(salir=="si" or salir=="no"): 
                break
        if(salir=="no"):
            print("Gracias por usar el programa")
            break
    n+=1
    primo= True

## 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6    

tope_rango=300
n=100
while(n<=tope_rango):
    if(n%3==0 and n%6==0):
        print(n, " es divisible por 3 y 6")
        break
    n+=1
       
      
               
    


