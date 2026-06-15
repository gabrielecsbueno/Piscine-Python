# Importacao absoluta: busca 'elements' a partir do sys.path (raiz do projeto).
# Necessario porque elements.py esta fora do pacote alchemy.
from elements import create_fire, create_water
# Importacao relativa: '.' representa o proprio pacote alchemy
# (alchemy/elements.py).
from .elements import create_air, create_earth


def healing_potion():
    return (f"Healing potion brewed with '{create_earth()}'"
            f" and '{create_air()}'")


def strength_potion():
    return (f"Strength potion brewed with '{create_fire()}'"
            f" and '{create_water()}'")
