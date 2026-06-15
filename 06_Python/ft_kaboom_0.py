# Acessa o subpacote grimoire diretamente.
# grimoire/__init__.py expoe apenas os modulos light, que nao tem
#  dependencia circular.
# A importacao ocorre sem problemas porque light_validator nao importa
#  de volta light_spellbook.
import alchemy.grimoire as grimoire

print("=== Kaboom 0 ===")
print("Using grimoire module directly")
print("Testing record light spell:",
      grimoire.light_spell_record('Fantasy', 'Earth, wind and fire'))
