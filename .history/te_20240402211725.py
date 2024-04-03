#te.py
class Te:
    def __init__(self, sabor, formato):
        self.sabor = sabor
        self.formato = formato
        self.duracion = 365  # Duración de 1 año o 365 días

    @staticmethod
    def obtener_tiempo_recomendacion(sabor):
        if sabor == 1:
            return 3, "Desayuno"  # Té negro
        elif sabor == 2:
            return 5, "Medio día"  # Té verde
        elif sabor == 3:
            return 6, "Atardecer"  # Infusión de hierbas
        else:
            return None, None

    @staticmethod
    def obtener_precio(formato):
        if formato == 1:
            return 3000  # Formato de 300 gr
        elif formato == 2:
            return 5000  # Formato de 500 gr
        else:
            return None