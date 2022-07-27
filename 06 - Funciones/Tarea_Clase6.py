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



lis1 = [1,1,1,1,1,2,2,2,"hola","chau", "chau"]
print(valor_moda(lis1))


