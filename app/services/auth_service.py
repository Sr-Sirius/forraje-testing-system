# ============================================
# Servicio de autenticación (login)
# ============================================

def login(username, password, db_users):
    """
    Verifica si un usuario existe en la base de datos simulada.
    """

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