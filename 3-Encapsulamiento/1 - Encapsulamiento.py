#Que es el encapsulamiento?

#El encapsulamiento es uno de los pilares de la POO y 
#consiste en ocultar los datos internos de un objeto para 
#que nadie pueda modificarlos o verlos directamente desde afuera por error

#Para aplicar el encapsulamiento tenemos que saber que hay tres niveles:

#Publico:

#self.vida = 300
#Cualquier persona puede modificar o verlo

#Protegido (1 guión bajo):

#self._mana = 400   
#Realmente este no hace nada, queda como publico PERO
#culturalmente en el espacio programador poner un solo
#guión bajo indica a los demas que esten viendo el programa
#que no se toque ya que es un dato externo o algo que si se
#cambia el programa se puede romper

#Privado (2 guión bajo):

#self.__level = 10
#Python bloquea el acceso directo desde fuera usando un 
#mecanismo llamado Name Mangling (cambio de nombre). 
#Si intentas llamarlo, el programa lanzará un error.


#Ahora que ya sabes que hace cada uno hagamos un ejemplo

"""
    class Telefono():
        def __init__ (self, marca, porcentaje_bateria):

            self.marca = marca                      #Se puede ver y cambiar libremente
            self.__bateria = porcentaje_bateria     #Oculto (Doble guión bajo)

    telefono1 = Telefono("Xiaomi", 20) #Creamos un objeto

    print(f"{telefono1.marca}, {telefono1.__bateria}") #Intentamos entrar a las variables
"""


#Si tratamos de acceder a marca, nos deja, porque es publico
#pero si tratamos con bateria, nos dira:
#AttributeError: 'Telefono' object has no attribute '__bateria'

#No es que sea un error de codigo o tipeo
#es el error que nos deberia dar y darnos una warning de que es privado

#Ahora si queremos que se muestre pero de forma mas "Formal"
#podriamos hacer una funcion que devuelva solamente la bateria

#Ejemplo:
#
#def ver_bateria(self):
#   return f"La bateria esta en {self.__bateria}%"
#
#Porque funciona? porque ya definiendola como funcion dejaria que se muestre
#porque ya no es algo directo como solo llamarlo con self, en este caso,
#el conseguir un dato de un objeto de esta manera seria un metodo getter que
#veremos mas a fondo despues.

#Ejemplo a codigo:



class Telefono():
    def __init__ (self, marca, porcentaje_bateria):
        self.marca = marca                      
        self.__bateria = porcentaje_bateria     
    def ver_bateria(self):
        return self.__bateria
    

telefono1 = Telefono("Xiaomi", 20) #Creamos un objeto

print(f"Mi {telefono1.marca} tiene un {telefono1.ver_bateria()}%!")
#           ^^^^^^^^^^^^^^              ^^^^^^^^^^^^^^^^^^^^^
#           atributo marca              funcion ver_bateria() Ojo no olvidar el () 
