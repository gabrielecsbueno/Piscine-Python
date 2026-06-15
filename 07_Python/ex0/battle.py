from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self) -> None:
        self.name = ""
        self.type_creature = ""
        self.power = ""

    @abstractmethod
    def attack(self) -> str:
        return (f"{self.name} uses {self.power}!")

    def describe(self) -> str:
        return (f"{self.name} is a "
                f"{self.type_creature} type Creature")


class Flameling(Creature):
    def __init__(self) -> None:
        self.name = 'Flameling'
        self.type_creature = 'Fire'
        self.power = 'Ember'

    def attack(self) -> str:
        return super().attack()


class Pyrodon(Creature):
    def __init__(self) -> None:
        self.name = 'Pyrodon'
        self.type_creature = 'Fire/Flying'
        self.power = 'Flamethrower'

    def attack(self) -> str:
        return super().attack()


class Aquabub(Creature):
    def __init__(self) -> None:
        self.name = 'Aquabub'
        self.type_creature = 'Water'
        self.power = 'Water Gun'

    def attack(self) -> str:
        return super().attack()


class Torragon(Creature):
    def __init__(self) -> None:
        self.name = 'Torragon'
        self.type_creature = 'Water'
        self.power = 'Hydro Pump'

    def attack(self) -> str:
        return super().attack()


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
