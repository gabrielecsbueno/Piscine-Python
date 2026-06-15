# Fecha a dependencia circular: dark_validator importa de dark_spellbook,
# que ja importou dark_validator — formando o ciclo que causa o ImportError.
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    if any(ingredient in ingredients.lower()
           for ingredient in dark_spell_allowed_ingredients()):
        return (f'{ingredients} - VALID')
    else:
        return (f'{ingredients} - INVALID')
