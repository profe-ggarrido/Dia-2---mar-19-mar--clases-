from te import Te

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