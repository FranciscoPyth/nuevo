
# 1. Idear la manera de realizar la siguiente salida (a, b y c son variables).:
a = 2.4
b = -3.21
c = 47.8

dic1 = 0

# 2. Mostrar por pantalla alguna imagen o dibujo.

# 3. Escriba un programa que lea 1 palabra (ingresadas por el usuario), calcule la longitud de cada una de ellas y las despliegue
# junto con su longitud indicada con asteriscos
pal1 = input("Ingrese una palabra: ")
pal2 = input("Ingrese su segunda palabra: ")
pal3 = input("Ingrese su tercer palabra: ")

print(pal1, end="   ")
for i in range(len(pal1)):
    print("*", end="")

print(pal2, end="   ")
for i in range(len(pal2)):
    print("*", end="")

print(pal3, end="   ")
for i in range(len(pal3)):
    print("*", end="")


# 4. Crear un diccionario del ejercicio anterior
dic2 = dict(

)

d = {'a': 1, 'b': 2}
it = d.items()
print(it) #dict_items([('a', 1), ('b', 2)])
print(list(it)) #[('a', 1), ('b', 2)]
print(list(it)[0][0]) #a
