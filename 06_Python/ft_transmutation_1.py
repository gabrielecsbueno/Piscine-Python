# 'import alchemy.transmutation' carrega o subpacote transmutation.
# lead_to_gold esta acessivel porque transmutation/__init__.py o
# re-exporta de recipes.py.
import alchemy.transmutation

print("=== Transmutation 1 ===")
print("Import transmutation module directly")
print("Testing lead to gold:", alchemy.transmutation.lead_to_gold())
