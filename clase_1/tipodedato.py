# Tipos de Datos
# Str
cad = "Esto es una cadena"
cad1 = "Esto es otra cadena"

print("| Cadena 1: ", cad, "| Cadena 2: ", cad1)

c = str(120)
print(c, type(c))

print(cad.lower())
print(cad[2:4])
print(len(cad.split()))

# Listas
lista_1 = ["Hola", 4, 3, True, [1, 2, 3, 4]]
print(lista_1)

print(type(lista_1))
print(len(lista_1))
print(lista_1[2])

# Diccionario
usuario = {
    "nombre": "Octavio",
    "apellido": "Gomez",
    "edad": 38,
    "hobbies": ["Futbol", "Musica"],
    "mascotas": False
}

print(usuario)
print(usuario["edad"])
print(len(usuario))

# Métodos
print(usuario.get("hobbies", "No encontrado"))
print(usuario.keys())

keys_usuario = list(usuario.keys())
print(type(keys_usuario))
print(usuario.get(keys_usuario[0]))

print(usuario.values())
