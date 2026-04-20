import pytest
from app.services.auth_service import login


# ============================================
# PRUEBAS UNITARIAS - LOGIN
# ============================================

# ✔ Caso exitoso
def test_login_exitoso():
    db = [
        {"username": "mike", "password": "123456"}
    ]

    result = login("mike", "123456", db)

    assert result["status"] is True
    assert result["user"]["username"] == "mike"


#  Usuario incorrecto
def test_login_usuario_incorrecto():
    db = [
        {"username": "mike", "password": "123456"}
    ]

    result = login("juan", "123456", db)

    assert result["status"] is False


#  Contraseña incorrecta
def test_login_password_incorrecto():
    db = [
        {"username": "mike", "password": "123456"}
    ]

    result = login("mike", "wrongpass", db)

    assert result["status"] is False

#  Login con datos vacíos (validación)
def test_login_datos_vacios():
    db = [
        {"username": "mike", "password": "123456"}
    ]

    result = login("", "", db)

    assert result["status"] is False