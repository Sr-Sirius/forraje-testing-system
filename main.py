from data.fake_users import usuarios
from data.fake_cultivos import cultivos
from app.services.auth_service import login
from app.services.recomendacion_service import recomendar_cultivo

# Test login
print(login("mike", "123456", usuarios))

# Test recomendación
print(recomendar_cultivo(6.5, 18, cultivos))

print("Usuarios:")
for u in usuarios:
    print(u["username"])

print("\nCultivos:")
for c in cultivos:
    print(c["nombre"])