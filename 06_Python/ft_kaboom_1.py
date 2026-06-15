# Tenta importar dark_spellbook diretamente, contornando o
# grimoire/__init__.py.
# dark_spellbook importa dark_validator, que imediatamente importa
# dark_spell_allowed_ingredients
# de dark_spellbook — que ainda nao terminou de ser inicializado.
# O Python nao consegue resolver a dependencia circular e lanca ImportError.

print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

from alchemy.grimoire.dark_spellbook import dark_spell_record  # noqa: F401, E402, E501
