# 1) Crear la clase vehículo que contenga los atributos:<br>
#Color<br>
#Si es moto, auto, camioneta ó camión<br>
#Cilindrada del motor

from re import A


class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
    
# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
#Acelerar<br>
#Frenar<br>
#Doblar<br>

class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = "derecho"

    def Acelerar(self,velocidad):
        self.velocidad += velocidad
        
    def Frenar(self,velocidad):
        self.velocidad -= velocidad
    def Doblar(self,doblar):
        self.direccion = doblar

# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

"Instanciar 3 objetos "

o1= Vehiculo('rojo','auto',20)
o2= Vehiculo('blanco','camioneta',100)
o3= Vehiculo("negro","moto",10)


"Ejecutar métodos de los objetos"
o1.Acelerar(40)
o1.Frenar(20)
o1.Doblar

o2.Acelerar(10)
o2.Frenar
o2.Doblar("a la izquierda")

o3.Acelerar(30)
o3.Frenar(20)
o3.Doblar("a la derecha")

# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = "derecho"

    def Acelerar(self,velocidad):
        self.velocidad += velocidad
        
    def Frenar(self,velocidad):
        self.velocidad -= velocidad
    def Doblar(self,doblar):
        self.direccion = doblar

    def Estado(self):
        print("Velocidad: ",self.velocidad,"\nDireccion: ",self.direccion)

    def Descripcion (self):
        print("Color: ",self.color,"\nTipo: ",self.tipo,"\nCilindrada: ",self.cilindrada)

o1= Vehiculo('rojo','auto',20)
o1.Descripcion()
o1.Acelerar(20)
o1.Doblar("a la izquierda")
o1.Estado()

# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6<br>
#Verificar Primo<br>
#Valor modal<br>
#Conversión grados<br>
#Factorial<br>

class Funciones:

    def __init__ (self):
        pass

    def es_primo(self,numero):
        primo = True
        for i in range(2, numero):
            if numero % i == 0:
                primo = False
            break
        return primo
    
    def valor_modal(self,lista,opcion):
     
        dic_repetidos = {}

        if(lista==[]):
            return "La lista está vacía"

        if opcion == "menor":
            lista.sort()
        else:
            lista.sort(reverse=True)
        
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
    
    
    def conversor_temperatura(self ,valor, origen, destino): 

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

    def factorial(self,numero):
            
        if (type(numero)== int):    
            if numero == 0:
                return 1
            if (numero>=1):
                return numero * self.factorial(numero-1)
            else:
                return "El valor ingresado debe ser entero positivo"
        else:
            return "El valor ingresado debe ser entero positivo"

# 6) Probar las funciones incorporadas en la clase del punto 5

f= Funciones()
print(f.es_primo(7))
print(f.valor_modal([-1,-1,-1,-1,-1,3,3,3,0,0,0,0,0],"menor"))
print(f.conversor_temperatura(10,"Celsius","Farenheit"))
print(f.factorial(5))

# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas
class Funciones: 
    def __init__ (self, lista_numeros):
        self.lista = lista_numeros
    
    def es_primo(self):
        for i in self.lista:
            if (self._es_primo(i)):
                print(i , "es primo")
            else:
                print(i , "no es primo")
    
   
    def conversor_temperatura(self,origen,destino):
        for i in self.lista:
            
            print(i, "grados", origen, "son " , self.__conversor_temperatura(i,origen,destino), "grados", destino)
    def factorial(self):
        for i in self.lista:
            print("el factorial de " , i , "es ", self.__factorial(i))

    def _es_primo(self,numero):

        primo = True
        for i in range(2, numero):
            if numero % i == 0:
                primo = False
            break
        return primo
    
    def valor_modal(self,opcion):
     
        dic_repetidos = {}

        if(self.lista==[]):
            return "La lista está vacía"

        if opcion == "menor":
            self.lista.sort()
            
        else:
            self.lista.sort(reverse=True)
        
        for nro in self.lista:
            clave = str(nro)
            if clave in dic_repetidos:
                dic_repetidos[clave] += 1
            else:
                dic_repetidos[clave] = 1
        print(dic_repetidos)

        maximo = 0
        moda = self.lista[0]
        for nro in dic_repetidos:
            if dic_repetidos[nro] > maximo:
                maximo = dic_repetidos[nro]
                moda= nro
        
        if opcion=="menor":
            print("El valor modal menor,que más se repite es: ", moda, "y se repite ", maximo, "veces")
        elif (opcion=="mayor"):
            print("El valor modal mayor,que más se repite es: ", moda, "y se repite ", maximo, "veces")
        return moda, maximo
    
    
    def __conversor_temperatura(self ,valor, origen, destino): 

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

    def __factorial(self,numero):
            
        if (type(numero)== int):    
            if numero == 0:
                return 1
            if (numero>=1):
                return numero *self.__factorial(numero-1)
            else:
                return "El valor ingresado debe ser entero positivo"
        else:
            return "El valor ingresado debe ser entero positivo"


L=Funciones([1,1,2,3,4,5,6,7,7])
L.es_primo()
L.valor_modal("mayor")
#print("el menor valor de los que mas se repiten es: ", moda, ",", maximo , "veces")
L.conversor_temperatura("Celsius","Farenheit")
L.factorial()

# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

from funciones import *
F1=Funciones([1,1,1,1,2,3,4,4,4])
F1.es_primo()
F1.valor_modal("mayor")