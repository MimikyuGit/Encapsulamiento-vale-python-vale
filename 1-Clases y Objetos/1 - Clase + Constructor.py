class nombre_de_clase(): #<- Se define el nombre y un (): despues
#^^^ es la palabra clave para inicializar una clase


    #Se crea una funcion llamada constructor
    #    vvvvv
    def __init__ (self): 
    #Que significa __init__? esla funcion que se activara siempre y 
    #cuando se cree (de crear) un objeto a partir de una clase.

    #Por lo tanto al definir esta funcion podemos hacer que
    #cada objeto que salga de esta clase obtenga automaticamente
    #lo que tenga dentro el __init__.

    #Normalmente dentro del constructor (def __init__ (self):)
    #se crean las variables iniciales o variables que se le pidan al usuario
    #como ejemplo:

    """
        def __init__ (self, variable_entrante):
            self.variable = variable_entrante
    """
    #Practicamente se le pueden agregar parametros que son obligatorios de poner
    #y despues con esos parametros asignarlos a los valores
    #2do ejemplo y con ejecución:
    """
    class Jugador():

        def __init__ (self, vida_entrante):
            self._vida = vida_entrante
    
    jugador_creado = Jugador(300) <- Aqui se crea una variable que contiene
                                     un objeto creado a partir de la clase
                                     Jugador y con el unico parametro que se
                                     le pide (vida) en 300.
    """

    
#Plantilla para crear una clase + constructor

""" 
class nombre-clase():
    def __init__ (self, variable_entrante):
        self.variable = variable_entrante
"""