from app.utils.validators import validar_ph, validar_temperatura

# ============================================
# Servicio de recomendación de cultivos
# ============================================

def recomendar_cultivo(ph, temperatura, cultivos):
    """
    Recomienda un cultivo basado en pH y temperatura.
    """

    #  Validaciones externas
    validar_ph(ph)
    validar_temperatura(temperatura)

    #  Lógica de recomendación
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