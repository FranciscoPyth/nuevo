# ACtividad de la clase, crear personajes por medio de clases
# En mi caso realizaré de Lol

class Personaje:
    def __init__(self, nombre, linea):
        self.nombre = nombre
        self.linea = linea

class Tanque(Personaje):

    def __init__(self, items, nombre, linea):
        self.items = items

        super().__init__(nombre, linea)

    def demostrar_grandeza(self):
        print(f"Hola! Me llamo {self.nombre} y estoy enorme!")

class Asesino(Personaje):
    def __init__(self, daño, nombre, linea):
        self.daño = daño

        super().__init__(nombre, linea)

    def demostrar_alma(self):
        print("Tengo sed de sangre...")

garen = Tanque("Espada", "Garen", "Top")
garen.demostrar_grandeza()
print(f"El primer guerrero de Lunacia! {garen.nombre}, Su mejor arma: la {garen.items}, y su mejor posicion {garen.linea}")

yasuo = Asesino(1000, "Yasuo", "Mid")
yasuo.demostrar_alma()
print(f"El asesino más feroz del mundo... {yasuo.nombre}, con su daño de {yasuo.daño}, y su desempeño en la linea {yasuo.linea}")

# Para el martes 20/09 completar el proyecto