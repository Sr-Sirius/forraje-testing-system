# ============================================
# Validaciones del sistema
# ============================================

def validar_ph(ph):
    if ph < 0 or ph > 14:
        raise ValueError("pH fuera de rango")


def validar_temperatura(temp):
    if temp < -10 or temp > 50:
        raise ValueError("Temperatura fuera de rango")


def validar_credenciales(username, password):
    if not username or not password:
        return False
    return True