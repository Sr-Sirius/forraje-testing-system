from app.utils.validators import validar_credenciales

# ============================================
# Servicio de autenticación (login)
# ============================================

def login(username, password, db_users):
    """
    Verifica si un usuario existe en la base de datos simulada.
    """

    #  Validación externa
    if not validar_credenciales(username, password):
        return {
            "status": False,
            "message": "Datos inválidos"
        }

    #  Lógica principal
    for user in db_users:
        if user["username"] == username and user["password"] == password:
            return {
                "status": True,
                "message": "Login exitoso",
                "user": user
            }

    return {
        "status": False,
        "message": "Credenciales inválidas"
    }