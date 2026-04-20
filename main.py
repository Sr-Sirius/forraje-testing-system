from data.fake_users import usuarios
from data.fake_cultivos import cultivos

print("Usuarios:")
for u in usuarios:
    print(u["username"])

print("\nCultivos:")
for c in cultivos:
    print(c["nombre"])