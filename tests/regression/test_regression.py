from app.services.auth_service import login
from app.services.recomendacion_service import recomendar_cultivo


# ============================================
# PRUEBAS DE REGRESIÓN
# ============================================

#  Login sigue funcionando correctamente
def test_regresion_login_exitoso():
    db = [
        {"username": "mike", "password": "123456"}
    ]

    result = login("mike", "123456", db)

    assert result["status"] is True


#  Login sigue fallando con credenciales incorrectas
def test_regresion_login_invalido():
    db = [
        {"username": "mike", "password": "123456"}
    ]

    result = login("mike", "wrongpass", db)

    assert result["status"] is False


#  Recomendación sigue funcionando
def test_regresion_recomendacion_valida():
    cultivos = [
        {
            "nombre": "Kikuyo",
            "ph_min": 5.5,
            "ph_max": 7.5,
            "temperatura_min": 10,
            "temperatura_max": 25
        }
    ]

    result = recomendar_cultivo(6.5, 18, cultivos)

    assert result["status"] is True


#  Recomendación sigue fallando correctamente
def test_regresion_recomendacion_fallida():
    cultivos = [
        {
            "nombre": "Kikuyo",
            "ph_min": 5.5,
            "ph_max": 7.5,
            "temperatura_min": 10,
            "temperatura_max": 25
        }
    ]

    result = recomendar_cultivo(2.0, 50, cultivos)

    assert result["status"] is False