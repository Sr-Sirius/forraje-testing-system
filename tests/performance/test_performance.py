import time
from app.services.auth_service import login
from app.services.recomendacion_service import recomendar_cultivo


# ============================================
# PRUEBAS DE RENDIMIENTO
# ============================================

#  Tiempo de respuesta del login
def test_login_performance():
    db = [
        {"username": "mike", "password": "123456"}
    ]

    inicio = time.time()
    login("mike", "123456", db)
    fin = time.time()

    tiempo = fin - inicio

    assert tiempo < 1  # debe ejecutarse en menos de 1 segundo


#  Tiempo de respuesta recomendación
def test_recomendacion_performance():
    cultivos = [
        {
            "nombre": "Kikuyo",
            "ph_min": 5.5,
            "ph_max": 7.5,
            "temperatura_min": 10,
            "temperatura_max": 25
        }
    ]

    inicio = time.time()
    recomendar_cultivo(6.5, 18, cultivos)
    fin = time.time()

    tiempo = fin - inicio

    assert tiempo < 1

def test_recomendacion_multiples_llamadas():
    cultivos = [
        {
            "nombre": "Kikuyo",
            "ph_min": 5.5,
            "ph_max": 7.5,
            "temperatura_min": 10,
            "temperatura_max": 25
        }
    ]

    inicio = time.time()

    for _ in range(1000):
        recomendar_cultivo(6.5, 18, cultivos)

    fin = time.time()

    assert (fin - inicio) < 2