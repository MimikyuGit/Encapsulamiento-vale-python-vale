#Que es la herencia basica?
#La herencia es un pilar de la poo que permite que una clase nueva (hija)
#herede los atributos y metodos de una clase existente (padre)

#En este caso veremos como una clase hija puede reutilizar codigo de la clase padre
#y ademas agregar sus propias caracteristicas o modificar las que ya existen
#Ejemplo a codigo:

class Animal():
   def __init__(self, nombre):
        self.nombre = nombre
   
   def hacer_sonido(self):
        return "Este animal hace un sonido"


class Perro(Animal):               #Entre parentesis ponemos la clase padre de la que heredamos
   def __init__(self, nombre, raza):
        super().__init__(nombre)   #Usamos super para traer del padre (animal) su nombre desde init
        self.raza = raza

   def hacer_sonido(self):         #Sobrescribimos el metodo del padre para hacerlo especifico
        return "Guau"


mi_perro = Perro("Firulais", "Golden")

print(mi_perro.nombre)

print(mi_perro.raza)

print(mi_perro.hacer_sonido())

#Que diferencia tiene con hacer clases desde cero?
#Que aca no tienes que repetir codigo que ya existe en otras clases
#aprovechando la reutilizacion y la jerarquia

#Antes tendrias que haber creado todo de nuevo en cada clase
#class Perro():
#   def __init__(self, nombre, raza):
#        self.nombre = nombre
#        self.raza = raza

#Pero aca con la herencia te ahorras escribir atributos repetidos
#y mantienes tu codigo mas ordenado y conectado

#Es mas facil porque agrupa comportamientos comunes en clases generales
#y deja los detalles especificos para las clases hijas
