from abc import ABC, abstractmethod
from ex0.battle import CreatureFactory, Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Creature | None = None) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.state = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        self.name = 'Sproutling'
        self.type_creature = 'Grass'
        self.power = 'Vine Whip'

    def attack(self) -> str:
        return super().attack()

    def heal(self, target: Creature | None = None) -> str:
        return (f"{self.name} heals itself for a small amount")


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        self.name = 'Bloomelle'
        self.type_creature = 'Grass/Fairy'
        self.power = 'Petal Dance'

    def attack(self) -> str:
        return super().attack()

    def heal(self, target: Creature | None = None) -> str:
        return (f"{self.name} heals itself and others for a large amount")


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self.state = False
        self.name = 'Shiftling'
        self.type_creature = 'Normal'

    def attack(self) -> str:
        if not self.state:
            return (f"{self.name} attacks normally.")
        else:
            return (f"{self.name} performs a boosted strike!")

    def transform(self) -> str:
        self.state = True
        return (f"{self.name} shifts into a sharper form!")

    def revert(self) -> str:
        self.state = False
        return (f"{self.name} returns to normal.")


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self.state = False
        self.name = 'Morphagon'
        self.type_creature = 'Normal/Dragon'

    def attack(self) -> str:
        if not self.state:
            return (f"{self.name} attacks normally.")
        else:
            return (f"{self.name} unleashes a devastating morph strike!")

    def transform(self) -> str:
        self.state = True
        return (f"{self.name} morphs into a dragonic battle form!")

    def revert(self) -> str:
        self.state = False
        return (f"{self.name} stabilizes its form.")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
