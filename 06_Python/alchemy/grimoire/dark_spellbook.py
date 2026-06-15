# DEPENDENCIA CIRCULAR INTENCIONAL: este modulo importa dark_validator,
# que por sua vez importa dark_spell_allowed_ingredients deste mesmo modulo.
# Quando o Python tenta carregar este arquivo, ele o registra em sys.modules
# como parcialmente inicializado e comeca a executar linha a linha.
# Ao chegar na linha abaixo, dispara o carregamento de dark_validator,
# que imediatamente tenta buscar dark_spell_allowed_ingredients — funcao que
# ainda nao foi definida, pois este modulo nao terminou de ser inicializado.
# Resultado: ImportError por dependencia circular.
from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list:
    return (list(["bats", "frogs", "arsenic", "eyeball"]))


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validate = validate_ingredients(ingredients)
    if '- VALID' in validate:
        return (f"Spell recorded: {spell_name} ({validate})")
    else:
        return (f"Spell rejected: {spell_name} ({validate})")
