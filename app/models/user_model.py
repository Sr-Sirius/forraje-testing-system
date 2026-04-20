# ============================================
# Modelo de Usuario
# ============================================

class User:
    def __init__(self, id, username, password, rol):
        self.id = id
        self.username = username
        self.password = password
        self.rol = rol