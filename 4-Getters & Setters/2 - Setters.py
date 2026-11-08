#Que es un setter?
#Un setter es casi lo mismo que un getter, una funcion aparte de la clase destinada
#a una funcion especifica de cierto atributo

#Pero en este caso el setter (De la palabra en ingles Set -> Colocar ó Establecer)
#lo que hace es enves de conseguir un dato lo que hace es cambiar el valor de
#ese atributo, por ejemplo si queremos cambiar el precio de algo

#Ejemplo:

"""
class Producto():
    def __init__(self,precio_inicial):
        self.__precio = precio_inicial

    def get_precio(self):   <- Un getter como vimos antes
        return self.__precio

    def set_precio(self, nuevo_precio) <- nuevo parametro entrante que se le pedira
        self.__precio = nuevo_precio      al usuario a la hora de iniciar este setter
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^                   ^^^ (obligatorio)
        Aqui se cambia el precio actual (self.__precio) al nuevo que ingrese el usuario   
"""
#Listo! Tenemos un setter y un getter pero... esta como que muy vacio y muy facil no?

#Compliquemosnos la vida (Mentira, pero eso diria cualquier programador)
#Mas que nada podemos agregar mas proceso para que por ejemplo en este caso
#el precio no sea negativo o que sea especifico

#Ejemplo mas completo y a codigo:

class Producto():
    def __init__(self,precio_inicial):
        self.__precio = precio_inicial

    def get_precio(self):
        return f"Precio actual: {self.__precio}"

    def set_precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            print("El precio no puede ser menor o igual a 0!")

        elif nuevo_precio > 1000000:
            print("El precio no puede ser mayor a 1 millon loco")

        else:
            print(f"Precio cambiado de {self.__precio} -> {nuevo_precio}")
            self.__precio = nuevo_precio

producto1 = Producto(5000)
print(producto1.get_precio()) #Printea 5000
producto1.set_precio(10000) #Cambia el precio actual a 10000 y printea que se cambió
