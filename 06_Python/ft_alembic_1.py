# 'from elements import create_water' traz apenas create_water para o
# namespace local.
# Nao e necessario usar 'elements.create_water()' — basta chamar
#  'create_water()' diretamente.
from elements import create_water


print("=== Alembic 1 ===")
print("Using: 'from ... import ...' structure to access elements.py")
print("Testing create_water:", create_water())
