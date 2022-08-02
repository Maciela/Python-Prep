class Funciones: 
    def __init__ (self, lista_numeros):
        self.lista = lista_numeros
    
    def es_primo(self):
        for i in self.lista:
            if (self.__es_primo(i)):
                print(i , "es primo")
            else:
                print(i , "no es primo")
    
   
    def conversor_temperatura(self,origen,destino):
        for i in self.lista:
            
            print(i, "grados", origen, "son " , self.__conversor_temperatura(i,origen,destino), "grados", destino)
    def factorial(self):
        for i in self.lista:
            print("el factorial de " , i , "es ", self.__factorial(i))

    def __es_primo(self,numero):

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