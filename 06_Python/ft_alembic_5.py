# 'from alchemy import create_air' busca create_air na interface publica
#  do pacote (__init__.py).
# Funciona porque alchemy/__init__.py exporta create_air explicitamente
#  com 'from .elements import create_air'.
from alchemy import create_air

print("=== Alembic 5 ===")
print("Accessing the alchemy module using 'from alchemy import ...'")
print("Testing create_air:", create_air())
