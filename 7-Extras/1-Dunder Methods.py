#Los dunder methods son los ganchos o puentes que conectan tus clases personalizadas 
#con el sistema interno y las funciones nativas de Python.
#
#Cuando creas una clase normal en Python, tus objetos propios estan "aislados". 
#No saben como reaccionar si intentas usarlos con funciones como 
#print(), len(), o si intentas sumarlos con el signo +. Los dunder 
#methods existen para darles superpoderes nativos a tus objetos, 
#permitiéndoles comportarse como si fueran tipos de datos integrados 
#de Python (como los enteros, las listas o los textos).

class CuentaBancaria:
    #1. __init__: El constructor que inicializa los atributos del objeto
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    #2. __str__: Define como se ve el objeto cuando usamos print o str
    def __str__(self):
        return f"Cuenta de {self.titular} con saldo de {self.saldo}"

    #3. __repr__: Define una representacion tecnica y clara del objeto para developers
    def __repr__(self):
        return f"CuentaBancaria(titular='{self.titular}', saldo={self.saldo})"

    #4. __len__: Permite usar la funcion len() para devolver un valor relacionado al objeto
    def __len__(self):
        #Simulamos que el largo representa la cantidad de caracteres del titular
        return len(self.titular)

    #5. __add__: Permite sumar dos objetos usando el operador +
    def __add__(self, otra_cuenta):
        #Suma los saldos de ambas cuentas bancarias
        return self.saldo + otra_cuenta.saldo


#Probando los dunder methods:

cuenta1 = CuentaBancaria("Ana", 500)
cuenta2 = CuentaBancaria("Carlos", 300)

#Al hacer print usa __str__
print(cuenta1)

#Al revisar el objeto directamente usa __repr__
print(repr(cuenta1))

#Al usar len() llama a __len__
print(len(cuenta1))

#Al sumar objetos usa __add__
total_saldos = cuenta1 + cuenta2
print(total_saldos)