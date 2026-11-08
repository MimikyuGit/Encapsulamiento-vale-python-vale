#Una clase abstracta es una clase diseñada exclusivamente 
#para funcionar como una plantilla o base para otras clases, con 
#la caracteristica estricta de que no puede ser instanciada 
#directamente (es decir, no se pueden crear objetos a partir de ella).
#Su unico proposito es ser heredada.


from abc import ABC, abstractmethod #desde la lib abc se importa ABC y abstractmethod

#ABC = sirve como superior para las clases que quieran ser estrictas
#Indica estrictamente que la clase es abstracta

#abstractmethod = sirve como el property, indica que un metodo
#va a ser un contrato obligatorio

#Contrato se refiere a una regla o algo estrictamente obligatorio que fue 
#decidido (como un contrato xd)

#Creamos la clase abstracta heredando de ABC
class Personaje(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    #Metodo obligatorio: todos deben tener un ataque
    @abstractmethod
    def atacar(self):
        pass


#Creamos una clase hija que cumple el contrato
class Mago(Personaje):
    def atacar(self):
        return f"{self.nombre} lanza una bola de fuego arcana."


#Creamos otra clase hija que también cumple el contrato
class Guerrero(Personaje):
    def atacar(self):
        return f"{self.nombre} da un golpe feroz con su espada."

mago = Mago("Gandalf")
guerrero = Guerrero("Aragorn")

print(mago.atacar())       # Gandalf lanza una bola de fuego arcana.
print(guerrero.atacar())   # Aragorn da un golpe feroz con su espada.

#Es como en la herencia + polimorfismo que se puede dejar un metodo vacio para
#que cada uno vea como rellenarlo, pero aca es obligatorio completarlo

