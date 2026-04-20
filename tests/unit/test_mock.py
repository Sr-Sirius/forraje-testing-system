from unittest.mock import MagicMock


# ============================================
# PRUEBA CON MOCK (simulación de modelo IA)
# ============================================

def test_mock_modelo_recomendacion():
    
    # Creamos un mock del modelo
    mock_modelo = MagicMock()

    # Definimos qué debe devolver
    mock_modelo.predict.return_value = "Kikuyo"

    # Simulamos uso del modelo
    resultado = mock_modelo.predict([6.5, 18, 70])

    # Validamos resultado
    assert resultado == "Kikuyo"

    # Verificamos que se llamó correctamente
    mock_modelo.predict.assert_called_once()

def test_mock_recomendacion_integrada():

    mock_modelo = MagicMock()
    mock_modelo.predict.return_value = "Alfalfa"

    resultado = mock_modelo.predict([7.0, 20, 80])

    assert resultado == "Alfalfa"