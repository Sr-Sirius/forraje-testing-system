from app.services.auth_service import login
from app.services.recomendacion_service import recomendar_cultivo


# ============================================
# SMOKE TESTS (pruebas básicas del sistema)
# ============================================

#  El login responde
def test_smoke_login():
    db = [{"username": "mike", "password": "123456"}]

    result = login("mike", "123456", db)

    assert result is not None
    assert "status" in result


#  La recomendación responde
def test_smoke_recomendacion():
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

    assert result is not None


#  El sistema no rompe con inputs básicos
def test_smoke_sistema_general():
    db = [{"username": "mike", "password": "123456"}]

    login_result = login("mike", "123456", db)

    cultivos = [
        {
            "nombre": "Kikuyo",
            "ph_min": 5.5,
            "ph_max": 7.5,
            "temperatura_min": 10,
            "temperatura_max": 25
        }
    ]

    rec_result = recomendar_cultivo(6.5, 18, cultivos)

    assert login_result["status"] is True
    assert rec_result is not None