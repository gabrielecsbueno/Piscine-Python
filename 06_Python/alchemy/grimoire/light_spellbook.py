# Dependencia de sentido unico: light_spellbook -> light_validator.
# light_validator NAO importa de volta este modulo,
# evitando dependencia circular.
from alchemy.grimoire.light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list:
    return (list(["earth", "air", "fire", "water"]))


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validate = validate_ingredients(ingredients)
    # '- VALID' distingue o caso valido de '- INVALID' sem falso positivo.
    if '- VALID' in validate:
        return (f"Spell recorded: {spell_name} ({validate})")
    else:
        return (f"Spell rejected: {spell_name} ({validate})")
