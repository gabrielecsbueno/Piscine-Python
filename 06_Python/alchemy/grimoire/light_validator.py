# Os ingredientes permitidos sao definidos aqui, e nao importados de
# light_spellbook.
# Isso quebra a dependencia circular: light_spellbook -> light_validator
# (sentido unico).
def validate_ingredients(ingredients: str):
    allowed_ingredients = ["earth", "air", "fire", "water"]
    # Verifica se algum ingrediente permitido aparece como substring
    # (case-insensitive).
    if any(ingredient in ingredients.lower()
           for ingredient in allowed_ingredients):
        return (f'{ingredients} - VALID')
    else:
        return (f'{ingredients} - INVALID')
