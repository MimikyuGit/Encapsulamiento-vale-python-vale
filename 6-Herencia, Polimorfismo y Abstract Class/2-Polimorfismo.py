#Herencia y polimorfismo?
#La herencia te ayuda a reutilizar atributos comunes desde una clase principal,
#mientras que el polimorfismo permite que cada subclase ejecute su propio comportamiento
#al invocar un metodo con el mismo nombre

#En este bloque veremos un escenario mas completo donde juntamos ambos conceptos
#para gestionar una nomina de trabajadores de manera eficiente y ordenada
#Ejemplo a codigo:

class Empleado():
   def __init__(self, nombre, id_empleado):  #Se definen las variables principales
        self.nombre = nombre
        self.id_empleado = id_empleado
   
   def calcular_sueldo(self): #Esta funcion se deja libre para dejar que los herederos
        pass                  #lo cambien a como se deberia para cada uno


class EmpleadoAsalariado(Empleado):
   def __init__(self, nombre, id_empleado, salario_mensual):
        super().__init__(nombre, id_empleado)
        self.salario_mensual = salario_mensual #Tenemos salario mensual (unico de este)

   def calcular_sueldo(self):
        return self.salario_mensual #y su funcion de calcular sueldo es diferente y unica


class EmpleadoPorComision(Empleado): #En este tambien pasa lo mismo, sus funciones y atributos cambian
   def __init__(self, nombre, id_empleado, ventas_totales, comision):
        super().__init__(nombre, id_empleado)
        self.ventas_totales = ventas_totales
        self.comision = comision
                                                
   def calcular_sueldo(self):
        return self.ventas_totales * self.comision


def pagar_a_todos(empleados): #Se crea una funcion simple solo para imprimir cada nombre y sus sueldos
   for trabajador in empleados:
        print(f"El trabajador {trabajador.nombre} recibe: {trabajador.calcular_sueldo()}")


trabajador1 = EmpleadoAsalariado("Sofia", "A01", 2000)
trabajador2 = EmpleadoPorComision("Mateo", "B02", 5000, 0.15)

nomina = [trabajador1, trabajador2] #lista con los trabajadores de arriba

pagar_a_todos(nomina) #Se aplica la funcion a la lista

#Herencia y poli, sirven demasiado, puedes seguir creando herencias y herencias
#hasta que no puedas mas, es como un arbol con sus ramas

#Este efecto de "arbol" se puede ver reflejada en algoritmos de ia en aprendizaje
#que son por generaciones, es una locura pero aqui es como lo mas basico posible