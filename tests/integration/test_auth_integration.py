from app.services.auth_service import login


# ============================================
# PRUEBAS DE INTEGRACIÓN - LOGIN
# ============================================

#  Login con datos reales simulados
def test_login_exitoso_integration(db_users):
    result = login("mike", "123456", db_users)

    assert result["status"] is True
    assert result["user"]["username"] == "mike"


#  Usuario no existe
def test_login_usuario_no_existe(db_users):
    result = login("no_existe", "123456", db_users)

    assert result["status"] is False


#  Password incorrecto
def test_login_password_incorrecto_integration(db_users):
    result = login("mike", "wrongpass", db_users)

    assert result["status"] is False