# Acessa recipes.py pelo caminho completo do modulo.
# Com 'import alchemy.transmutation.recipes', o modulo e referenciado
# pelo caminho inteiro na chamada.
import alchemy.transmutation.recipes

print("=== Transmutation 0 ===")
print("Using file alchemy/transmutation/recipes.py directly")
print("Testing lead to gold:", alchemy.transmutation.recipes.lead_to_gold())
