#Que es un metodo?

#Son funciones definidas dentro de ella que determinan
#el comportamiento de los objetos o de la propia clase

#Ejemplo:

#class Jugador():

#   def __init__(self,mana):
#       self.mana = mana

#   def lanzar_hechizo(self):
#       self.mana = self.mana - 25
#       return print(f"Hechizo lanzado! tu mana ahora es: {self.mana}")

#Ok paso a paso, primero se define clase jugador, despues
#creamos su respectivo constructor, que en este caso solo pedira
#la cantidad de mana que tendra el jugador, nada mas

#Despues creamos un metodo, que se llamará lanzar_hechizo
#que hara esto? este metodo hara que al mana actual del jugador
#se le quite 25, ya que es un tipo de variable int/numero.

#Cuando se llamara este metodo?
#A diferencia del metodo constructor (__init__)
#este metodo solo se llamara cuando se llame especificamente, no
#cuando se cree el objeto, suena estupido pero es literal

#En este ejemplo para llamar este metodo primero
#tenemos que crear un objeto y luego llamar a esa funcion asi:



"""
jugador_2 = Jugador(100) #Mana = 100

#Ahora llamamos a su funcion

jugador_2.lanzar_hechizo

#Esto tendria que devolver lo que pusimos en el return de lanzar_hechizo
"""

#Ejemplo a codigo real:

class Jugador():
    def __init__(self,mana):
        self.mana = mana
    
    def lanzar_hechizo(self):
        self.mana = self.mana - 25
        return print(f"Hechizo lanzado! Mi mana ahora es: {self.mana}.")

jugador_2 = Jugador(100)

jugador_2.lanzar_hechizo()#Mana = 75

#El mana queda en 75 (porque mana inicial = 100 y se le resta 25 por la funcion)
#Y podemos repetirlo

jugador_2.lanzar_hechizo()#Mana = 50
jugador_2.lanzar_hechizo()#Mana = 25
jugador_2.lanzar_hechizo()#Mana = 0 

