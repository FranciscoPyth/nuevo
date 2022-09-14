# Clase

class Animal:

    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    def hablar(self, sonido):
        print(sonido)
        

class Perro(Animal):

    def __init__(self, nombre, raza, especie, edad):
        # Atributos de instancia == locales
        self.nombre = nombre
        self.raza = raza
        super().__init__(especie, edad)
    
    # Métodos
    def saludar(self):
        print(f"{self.nombre} dio la pata")


perro_1 = Perro("Firulais", "Salchicha", "Golden", 17)
print(f"Perro_1 --> {perro_1.nombre}, {perro_1.raza}, {perro_1.especie}, {perro_1.edad}")
perro_1.saludar

# Comentario: React no trabaja con programación orientada a objetos, visualfox tampoco y Javascript antes no lo tenía