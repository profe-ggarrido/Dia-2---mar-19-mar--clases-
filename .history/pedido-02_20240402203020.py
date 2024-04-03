from te import Te
import pickle

# Función para guardar el pedido en el historial
def guardar_pedido(sabor, formato, tiempo, recomendacion, precio):
    pedido = {
        'sabor': ['Té negro', 'Té verde', 'Infusión de hierbas'][sabor - 1],
        'formato': formato,
        'tiempo': tiempo,
        'recomendacion': recomendacion,
        'precio': precio
    }

    try:
        with open('historial.py', 'rb') as archivo:
            historial = pickle.load(archivo)
    except (FileNotFoundError, pickle.UnpicklingError):
        historial = []

    historial.append(pedido)

    with open('historial.py', 'wb') as archivo:
        pickle.dump(historial, archivo)

# Obtener los datos del usuario
sabor = int(input("Ingrese el sabor de té (1: Té negro, 2: Té verde, 3: Infusión de hierbas): "))
formato = int(input("Ingrese el formato (1: 300 gr, 2: 500 gr): "))

# Crear una instancia de la clase Te
te_pedido = Te(sabor, formato)

# Obtener el tiempo de preparación y la recomendación
tiempo, recomendacion = Te.obtener_tiempo_recomendacion(sabor)

# Obtener el precio
precio = Te.obtener_precio(formato)

# Mostrar el detalle del pedido
print("Detalle del pedido:")
print(f"Sabor: {['Té negro', 'Té verde', 'Infusión de hierbas'][sabor - 1]}")
print(f"Formato: {formato} ({'300 gr' if formato == 1 else '500 gr'})")
print(f"Precio: ${precio}")
print(f"Tiempo de preparación: {tiempo} minutos")
print(f"Recomendación: {recomendacion}")

# Guardar el pedido en el historial
guardar_pedido(sabor, formato, tiempo, recomendacion, precio)