from app.services.recomendacion_service import recomendar_cultivo


# ============================================
# PRUEBAS DE INTEGRACIÓN - RECOMENDACIÓN
# ============================================

#  Caso real con data completa
def test_recomendacion_real(db_cultivos):
    result = recomendar_cultivo(6.5, 18, db_cultivos)

    assert result["status"] is True
    assert result["cultivo"] is not None


#  No hay cultivo adecuado
def test_recomendacion_sin_resultado(db_cultivos):
    result = recomendar_cultivo(3.0, 50, db_cultivos)

    assert result["status"] is False


#  Validación de error (pH inválido)
def test_recomendacion_ph_invalido_integration(db_cultivos):
    import pytest

    with pytest.raises(ValueError):
        recomendar_cultivo(-1, 20, db_cultivos)