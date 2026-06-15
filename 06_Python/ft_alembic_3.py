# 'from alchemy.elements import create_air' extrai apenas create_air
#  do submodulo.
# Permite usar create_air() diretamente, sem prefixo de pacote.
from alchemy.elements import create_air

print("=== Alembic 3 ===")
print("Accessing alchemy/elements.py using 'from ... import ...' structure")
print("Testing create_air:", create_air())
