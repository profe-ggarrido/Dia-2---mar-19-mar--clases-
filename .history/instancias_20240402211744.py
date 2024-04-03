#instancias.py
from te import Te

# Crear dos instancias
te1 = Te(1, 1)  # Té negro, formato de 300 gr
te2 = Te(2, 2)  # Té verde, formato de 500 gr

# Almacenar el tipo de dato de cada instancia
tipo_te1 = type(te1)
tipo_te2 = type(te2)

# Mostrar el tipo de dato de cada instancia
print(tipo_te1)
print(tipo_te2)

# Comparar si los tipos de dato son iguales
if tipo_te1 == tipo_te2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")