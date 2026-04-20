# ============================================
# Modelo de Cultivo
# ============================================

class Cultivo:
    def __init__(self, nombre, ph_min, ph_max, temp_min, temp_max):
        self.nombre = nombre
        self.ph_min = ph_min
        self.ph_max = ph_max
        self.temp_min = temp_min
        self.temp_max = temp_max