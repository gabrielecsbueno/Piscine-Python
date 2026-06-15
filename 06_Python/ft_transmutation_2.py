# Acessa lead_to_gold pela interface publica do pacote alchemy.
# Funciona porque alchemy/__init__.py importa lead_to_gold de transmutation,
# encadeando: alchemy -> transmutation/__init__ -> recipes.py
import alchemy

print("=== Transmutation 2 ===")
print("Import alchemy module only")
print("Testing lead to gold:", alchemy.lead_to_gold())
