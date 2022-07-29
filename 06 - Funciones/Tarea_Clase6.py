# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es
def es_primo(n):
    es_primo = True
    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break
    return es_primo

print(es_primo(25))

# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista
def extrae_primos_de_lista(list):
    lista_primos= []
    for elemento in list:
        if (type(elemento) == int):
            if(es_primo(int(elemento)) == True):
                lista_primos.append(elemento)
            else:
                continue
        
    return lista_primos
            

lista= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, 1.3,1,1,1,1]
print(extrae_primos_de_lista(lista))

#3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera
def valor_moda(lista):
    dic_repetidos = {}
    for nro in lista:
        clave = str(nro)
        if clave in dic_repetidos:
            dic_repetidos[clave] += 1
        else:
            dic_repetidos[clave] = 1
    print(dic_repetidos)

    maximo = 0
    
    moda =lista[0]
    for nro in dic_repetidos:
        if dic_repetidos[nro] > maximo:
            maximo = dic_repetidos[nro]
            moda= nro
    
    return moda, maximo



lis1 = [1,1,1,1,1,2,2,2,3,4,4]
print(valor_moda(lis1))

# 4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.

def valor_moda(lista,opcion="mayor"):
     
    dic_repetidos = {}
    for nro in lista:
        clave = str(nro)
        if clave in dic_repetidos:
            dic_repetidos[clave] += 1
        else:
            dic_repetidos[clave] = 1
    print(dic_repetidos)

    maximo = 0
    moda =lista[0]
    for nro in dic_repetidos:
        if dic_repetidos[nro] > maximo:
            maximo = dic_repetidos[nro]
            moda= nro

    lista_claves = list(dic_repetidos.keys())
    lista_valores = list(dic_repetidos.values())
  
    if opcion == "mayor":
        mayor = lista_claves[len(lista_claves)-1]
        valor_mayor= lista_valores[len(lista_valores)-1]
        return mayor, valor_mayor
    elif (opcion=="menor"):
        menor = lista_claves [0]
        valor_menor = lista_valores[0]
        return menor, valor_menor
   
 




print(valor_moda(lis1, "mayor"))
print(valor_moda(lis1, "menor"))

# 5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
#Fórmula 1	: (°C × 9/5) + 32 = °F<br>
#Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino

def conversor_temperatura(valor, origen, destino): 
    if (origen== "Celsius" and destino== "Farenheit"):
        conversion_C_F= (valor * 9/5) + 32
        return conversion_C_F
    elif(origen== "Farenheit" and destino== "Celsius"):
        conversion_F_C= (valor - 32) * 5/9
        return conversion_F_C

    if(origen== "Celsius" and destino== "Kelvin"):
        conversion_C_K= valor + 273.15
        return conversion_C_K
    elif(origen== "Kelvin" and destino== "Celsius"):
        conversion_K_C= valor - 273.15
        return conversion_K_C

    if(origen== "Farenheit" and destino== "Kelvin"):
        conversion_F_K= (valor + 459.67) * 5/9
        return conversion_F_K
    elif(origen== "Kelvin" and destino== "Farenheit"):
        conversion_K_F= (valor * 9/5) - 459.67
        return conversion_K_F

    if(origen== "Celsius" and destino== "Celsius"):
        return valor
    elif(origen== "Farenheit" and destino== "Farenheit"):
        return valor
    elif(origen== "Kelvin" and destino== "Kelvin"):
        return valor
    
print(conversor_temperatura(30,"Celsius","Celsius"))

# 6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

print("1 grado Celsius a Farenheit: ", conversor_temperatura(1,"Celsius","Farenheit"))
print("1 grado Farenheit a Celsius: ", conversor_temperatura(1,"Farenheit","Celsius"))
print("1 grado Celsius a Kelvin: ", conversor_temperatura(1,"Celsius","Kelvin"))
print("1 grado Kelvin a Celsius: ", conversor_temperatura(1,"Kelvin","Celsius"))
print("1 grado Farenheit a Kelvin: ", conversor_temperatura(1,"Farenheit","Kelvin"))
print("1 grado Kelvin a Farenheit: ", conversor_temperatura(1,"Kelvin","Farenheit"))
print("1 grado Celsius a Celsius: ", conversor_temperatura(1,"Celsius","Celsius"))
print("1 grado Farenheit a Farenheit: ", conversor_temperatura(1,"Farenheit","Farenheit"))
print("1 grado Kelvin a Kelvin: ", conversor_temperatura(1,"Kelvin","Kelvin"))

# 7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

def factorial(numero):
    if numero == 0:
        return 1
    if (numero>=1):
        return numero * factorial(numero-1)
    else:
        return "El valor integro debe ser mayor o igual a 0"

print(factorial(-3))