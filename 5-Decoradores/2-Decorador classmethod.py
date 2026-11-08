#Que es el classmethod?
#El classmethod es un decorador que convierte un metodo normal en un metodo de clase
#A diferencia de los metodos normales que reciben self, este recibe cls que es la clase entera

#En este caso veremos el decorador classmethod, que sirve para crear constructores
#alternativos, lo que hace classmethod es tomar la funcion que esta abajo suyo
#y permitir crear objetos usando la clase misma en vez de una instancia
#Ejemplo a codigo:

class Persona():
   def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
   
   @classmethod                #Cuando usamos classmethod recibimos cls
   def desde_anio(cls, nombre, anio): #en vez de self y podemos retornar un objeto
        edad_calculada = 2026 - anio
        return cls(nombre, edad_calculada)


persona1 = Persona("Ana", 20)

print(persona1.edad)

persona2 = Persona.desde_anio("Carlos", 2000)

print(persona2.edad)

#Que diferencia tiene con hacer la creacion normal?
#Que aca podemos procesar datos o hacer calculos antes de instanciar la clase
#de forma mas limpia y ordenada dentro de la misma clase

#Antes para crear un objeto a partir de un anio tendrias que hacer
#anio = 2000
#edad_calc = 2026 - anio
#persona2 = Persona("Carlos", edad_calc)

#Pero aca es mas simple y directo, porque la clase sabe como construirse
#persona2 = Persona.desde_anio("Carlos", 2000)

#Es mas facil porque delegas la logica de creacion directamente a la clase
#y evitas llenar tu codigo principal de calculos repetitivos

#Mas que nada esa es la diferencia mas marcable del classmethod con el init normal
#es mas limpio para ti y para futuros coders que vean tu codigo