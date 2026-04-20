import pytest
from app.services.recomendacion_service import recomendar_cultivo


# ============================================
# PRUEBAS UNITARIAS - RECOMENDACIÓN
# ============================================

# ✔ Caso válido
def test_recomendacion_valida():
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
    assert result["cultivo"] == "Kikuyo"


#  No hay cultivo adecuado
def test_recomendacion_fallida():
    cultivos = [
        {
            "nombre": "Kikuyo",
            "ph_min": 5.5,
            "ph_max": 7.5,
            "temperatura_min": 10,
            "temperatura_max": 25
        }
    ]

    result = recomendar_cultivo(4.0, 50, cultivos)

    assert result["status"] is False


#  pH inválido
@pytest.mark.parametrize("ph", [-1, 15])
def test_ph_invalido(ph):
    cultivos = []

    with pytest.raises(ValueError):
        recomendar_cultivo(ph, 20, cultivos)


#  Temperatura inválida
@pytest.mark.parametrize("temp", [-20, 60])
def test_temperatura_invalida(temp):
    cultivos = []

    with pytest.raises(ValueError):
        recomendar_cultivo(6.5, temp, cultivos)