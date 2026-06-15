# 'import alchemy.elements' acessa um modulo dentro de um pacote pelo
# caminho completo.
# O modulo e referenciado com o caminho completo na chamada:
# alchemy.elements.create_earth()
import alchemy.elements

print("=== Alembic 2 ===")
print("Accessing alchemy/elements.py using 'import ...' structure")
print("Testing create_earth:", alchemy.elements.create_earth())
