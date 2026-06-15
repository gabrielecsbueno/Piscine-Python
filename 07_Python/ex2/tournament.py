from abc import ABC, abstractmethod
from ex0.battle import Creature
from ex1.capacitor import TransformCapability, HealCapability


# para lancar uma Exception pesonalizada
class BattleException(Exception):
    pass


# Estrategia de Batalha (ABSTRATA)
class BattleStrategy(ABC):
    @abstractmethod
    def act(self) -> None:
        pass

    # retorna um `True` o `False` indicando que uma Criatura Creature
    # é adequada para a estrategia
    @abstractmethod
    def is_valid(self) -> bool:
        pass


# Batalha Normal (herda a estrategia de batalha)
class NormalStrategy(BattleStrategy):
    # instancio essa classe passando uma instancia de Criatura (qualquer)
    def __init__(self, creature: Creature):
        self.creature = creature

    # metodos que hardam de BattleStrategy: act e is_valid
    def act(self) -> None:
        print(self.creature.attack())

    # sempre retornara `True`, porque pode ser qualquer criatura
    def is_valid(self) -> bool:
        return True


# Batalha Agressiva, para criaturas que podem transformar
class AggressiveStrategy(BattleStrategy):
    # instancio essa classe passando uma instancia de Creature;
    # a validacao do tipo ocorre em act() via isinstance
    def __init__(self, creature: Creature):
        self.creature = creature

    # metodos que hardam de BattleStrategy: act e is_valid
    # ele vai trasformar, atacar e reverter
    def act(self) -> None:
        # isinstance estreita o tipo para mypy: dentro do if,
        # creature e reconhecida como Creature & TransformCapability
        if isinstance(self.creature, TransformCapability):
            print(self.creature.transform())
            print(self.creature.attack())
            print(self.creature.revert())
        else:
            # se nao for, ele lanca a excessao que sera capturada no script
            raise BattleException(
                f"Invalid Creature '{self.creature.name}' "
                f"for this aggressive strategy"
            )

    # aqui retorna um bool vindo se a instancia da criatura e um tipo
    # tranformacao
    def is_valid(self) -> bool:
        return isinstance(self.creature, TransformCapability)


# Batalha defenciva, para criaturas que podem curar
class DefensiveStrategy(BattleStrategy):
    # instancio essa classe passando uma instancia de Creature;
    # a validacao do tipo ocorre em act() via isinstance
    def __init__(self, creature: Creature):
        self.creature = creature

    # metodos que hardam de BattleStrategy: act e is_valid
    # eles vao atacar e curar
    def act(self) -> None:
        # isinstance estreita o tipo para mypy: dentro do if,
        # creature e reconhecida como Creature & HealCapability
        if isinstance(self.creature, HealCapability):
            print(self.creature.attack())
            print(self.creature.heal())
        else:
            # se nao for, ele lanca a excessao que sera capturada no script
            raise BattleException(
                f"Invalid Creature '{self.creature.name}' "
                f"for this defensive strategy"
            )

    # aqui retorna um bool vindo se a instancia da criatura e um tipo
    # cura
    def is_valid(self) -> bool:
        return isinstance(self.creature, HealCapability)
