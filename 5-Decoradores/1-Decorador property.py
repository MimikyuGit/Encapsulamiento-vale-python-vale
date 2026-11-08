#Que son los decoradores?
#Los decoradores son agregados a funciones para cambiar de como
#se comportan y sus funciones

#En este caso veremos un decorador llamado property, que sirve para
#lo que vimos anteriormente (getters y setters) lo que hace property
#es que toma la funcion que esta abajo suyo y lo crea como propiedad
#Ejemplo a codigo:

class Usuario():
   def __init__(self, nombre, email, contrasena):
       self.nombre = nombre
       self.email = email
       self.__contrasena = contrasena
   
   @property                   #Cuando ya definimos la property se crea
   def contrasena(self):       #automaticamente el getter de este
       return self.__contrasena

   @contrasena.setter           #Se crea un .setter con el nombre de la property
   def contrasena(self, nueva_contrasena):
       self.__contrasena = nueva_contrasena


user1 = Usuario("mimikyu", "mimikyu313k@outlook.es", "mimikyu2007")

print(user1.contrasena)

user1.contrasena = "asd"

print(user1.contrasena)

#Que diferencia tiene con los getters y setters convencionales de la carpeta n4?
#Que aca podemos cambiar la variable mas libremente y mas intuitivo si es que
#llega a un cliente etc.

#Antes para cambiar nuestra contraseña seria
#user1 = Usuario("mimikyu", "mimikyu313k@outlook.es", "mimikyu2007")
#user1.set_contraseña("asd")

#Pero aca es mas simple, como si fuera una variable ya hecha
#user1.contrasena = "asd"

#Es mas facil porque se relacion mas a las variables con las que siempre
#enseñan, asi:

#mi_variable = 123

#y si la queriamos cambiar seria tan simple como:

#mi_variable = 231

#Mas que nada esa es la diferencia mas marcable de el property con sus getter y setter
#es mas legible para ti y para futuros coders que vean tu codigo