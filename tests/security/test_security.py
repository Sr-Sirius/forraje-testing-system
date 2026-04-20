import pytest
from app.services.auth_service import login
from app.services.recomendacion_service import recomendar_cultivo


# ============================================
# PRUEBAS DE SEGURIDAD
# ============================================

#  Login con usuario vacío
def test_login_usuario_vacio():
    db = [{"username": "mike", "password": "123456"}]

    result = login("", "123456", db)

    assert result["status"] is False


#  Login con password vacío
def test_login_password_vacio():
    db = [{"username": "mike", "password": "123456"}]

    result = login("mike", "", db)

    assert result["status"] is False


#  Login con datos None
def test_login_datos_none():
    db = [{"username": "mike", "password": "123456"}]

    result = login(None, None, db)

    assert result["status"] is False


#  Intento de "inyección" (simulada)
def test_login_injection():
    db = [{"username": "mike", "password": "123456"}]

    result = login("' OR '1'='1", "' OR '1'='1", db)

    assert result["status"] is False


#  pH fuera de rango (seguridad lógica)
@pytest.mark.parametrize("ph", [-100, 100])
def test_ph_extremo(ph):
    with pytest.raises(ValueError):
        recomendar_cultivo(ph, 20, [])


#  Temperatura extrema
@pytest.mark.parametrize("temp", [-100, 200])
def test_temperatura_extrema(temp):
    with pytest.raises(ValueError):
        recomendar_cultivo(6.5, temp, [])