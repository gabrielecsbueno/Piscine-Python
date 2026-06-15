# Usa a interface publica do pacote alchemy.
# strength_potion e heal (alias de healing_potion) foram
#  exportados no __init__.py,
# logo ficam acessiveis diretamente via alchemy.<nome>().
import alchemy


print("=== Distillation 1 ===")
print("Using: 'import alchemy' structure to access potions")
print("Testing strength_potion:", alchemy.strength_potion())
print("Testing heal alias:", alchemy.heal())
