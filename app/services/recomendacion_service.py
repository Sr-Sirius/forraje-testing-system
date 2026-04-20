# ============================================
# Servicio de recomendación de cultivos
# ============================================

def recomendar_cultivo(ph, temperatura, cultivos):
    """
    Recomienda un cultivo basado en pH y temperatura.
    """

    # Validaciones (importantes para testing)
    if ph < 0 or ph > 14:
        raise ValueError("pH fuera de rango")

    if temperatura < -10 or temperatura > 50:
        raise ValueError("Temperatura fuera de rango")

    # Lógica de recomendación
    for cultivo in cultivos:
        if (cultivo["ph_min"] <= ph <= cultivo["ph_max"] and
            cultivo["temperatura_min"] <= temperatura <= cultivo["temperatura_max"]):
            
            return {
                "status": True,
                "cultivo": cultivo["nombre"]
            }

    return {
        "status": False,
        "message": "No se encontró cultivo adecuado"
    }