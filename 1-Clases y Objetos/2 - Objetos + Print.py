#Como ya vimos en el py anterior se pueden crear objetos, pero que
#exactamente es un objeto?

#Tomalo como esto:

#Una clase es un molde de jugador por ejemplo.

#Ojo que la clase aun no es ningun jugador es solo el esqueleto
#para crear uno.

#Entonces ahi es cuando entran los objetos/instancias.
#En este caso seria un jugador, y ese jugador (ó objeto)
#sera creado a partir de lo que diga la clase, por ejemplo como vimos
#antes el constructor, el constructor normalmente se usa para definir
#la mayoria de variables iniciales para los objetos

#En el caso de jugador podriamos definir las siguientes variables
#en el constructor

#Vida
#Mana
#Escudo
#Level
#etc etc

#Ejemplo a codigo:

"""
    class Jugador():
        def __init__(self, vida, mana, level) <- Pedimos tres variables para crear el jugador
            self.vida = vida <- variable jugador.vida = vida (parametro entrante)
            self.mana = mana
            self.level = level

    
    Ahora creamos un jugador:
    jugador_1 = Jugador(self, 100, 100, 15) 
                                ^^^^^^---(En orden: vida, mana y level)
    Creamos un jugador con los siguientes datos:
    vida = 100
    mana = 100 
    level = 15

    Ahora: como se si realmente el jugador tiene esa vida o level?
    
    Con un print temporal de la sgte manera:

    jugador_1.vida
    
    y 

    jugador_1.level

    Eso te deberia entregar el dato guardado en esa variable.
    Y si te das cuenta no es el medio leseo como para buscar algun dato,
    ya que, existe el self, el que usamos en todo de clases, lo que hace self
    es que llama al nombre del objeto a donde lo usemos, en este caso en cada variable
    entonces pasa de: self.vida = vida --> jugador_1.vida = vida
"""

#Ejercicio en codigo

class Jugador ():
    def __init__(self, vida, mana, level):
        self.vida = vida
        self.mana = mana
        self.level = level
    
jugador_1 = Jugador(100, 100, 15)

print(jugador_1.vida) #printea la vida del jugador (100)
print(jugador_1.level) #printea el level del jugador (15)

#Pero si quieres poner texto dentro de eso + variables
#Se utiliza (f""), el f es un comodin que nos deja poner dentro de un
#texto variables ya definidas en llaves

#Ejemplo:

#print(f"Mi variable vida es: {jugador_1.vida}") 
#      ^                      ^^^^^^^^^^^^^^^^
#Se pone el f antes del string y lo que sea variables dentro de las comillas
#y encerrado en llaves

#Ejemplo 2:
#print(f"Mi level es: {jugador_1.level} y mi vida es: {jugador_1.vida}")

#los dos ejemplos imprimiran lo siguiente:

#Ejemplo 1:
#Mi variable vida es: 100

#Ejemplo 2:
#Mi level es: 15 y mi vida es: 100

print(f"Mi variable vida es: {jugador_1.vida}")

print(f"Mi level es: {jugador_1.level} y mi vida es: {jugador_1.vida}")
