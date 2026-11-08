#Que es un metodo estatico?

#Es una funcion perteneciente a una clase pero
#a diferencia de un metodo base este no recibe parametros

#Practicamente es como tener una funcion suelta por ahi pero mas organizada



#Normalmente esto se podria relacionar a librerias por ejemplo de matematica
#Ojo, es una comparacion, no es necesariamente que las librerias usen staticmethods

#Ejemplo basico:

class Matematicas():
   @staticmethod                   #<- este decorador se pone antes de que definamos un metodo estatico
   def sumar(a , b):                #<- ojo no recibe self, solo parametros
       return a + b                #<- retorna la suma de los dos parametros

#Probamos el metodo
resultado = Matematicas.sumar(3,5) #<- Fijate que no tuvimos que crear un objeto para
                                   #   acceder al metodo estatico solo lo guardamos

print(f"El resultado de la suma es: {resultado}")    #<-- resultado: 8

