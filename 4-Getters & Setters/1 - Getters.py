#Que es un getter?
#Es un método público que sirve para leer el valor de una variable privada.

#Como vimos antes pudimos acceder a un atributo mediante una funcion aparte
#enves de directamente, esa funcion se llama getter (De la palabra en ingles Get -> Obtener)

#Plenamente es lo mas basico en funciones asi, lo unico que debe hacer es devolver
#el valor de lo que se le asignó

#Ejemplo:

"""
    class Cuenta():
        def __init__(self, usuario, clave):
            self.usuario = usuario
            self.__clave = clave  <-- Le ponemos __ porque es un dato sensible/privado
        
        def recuperar_clave(self): <-- Metodo getter
            return self.__clave

"""

#Porque un getter?

#Porque asi podemos acceder a un dato de una manera que se pueda seguir algun proceso
#al ejemplo de una clave, si accedemos solo con cuenta1.clave es un poco inseguro y
#propenso a ser "hackeado", entonces ahora que usamos los getters y encapsulamiento
#podemos poner un proceso en el metodo de recuperar_clave() para que siga ciertos pasos
#para poder corroborar bien si la persona esta destinada a recibir la clave (si es el dueño de la cuenta)
