# Acessa potions como submodulo direto de alchemy, sem usar a
#  interface do __init__.
# 'from alchemy import potions' retorna o objeto-modulo
#  alchemy/potions.py inteiro,
# permitindo chamar qualquer funcao do arquivo:
#  potions.strength_potion(), potions.healing_potion()
from alchemy import potions

print("=== Distillation 0 ===")
print("Direct access to alchemy/potions.py")
print("Testing strength_potion:", potions.strength_potion())
print("Testing healing_potion:", potions.healing_potion())
