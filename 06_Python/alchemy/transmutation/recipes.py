# Importacao absoluta: especifica o caminho completo a partir da raiz do
# sys.path.
from alchemy.elements import create_air
from elements import create_fire
# Importacao relativa: '..' sobe um nivel — de transmutation/ para alchemy/
# — e acessa potions.
from ..potions import strength_potion


def lead_to_gold():
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}' "
            f"and '{strength_potion()}' mixed with '{create_fire()}'")
