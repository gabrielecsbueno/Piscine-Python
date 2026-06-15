from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capacitor import HealCapability, TransformCapability


def main_capacitor():
    # definindo as funcoes para fabrica de criaturas
    # cria uma criatura base
    def fact_create_heal(factory: HealingCreatureFactory) -> None:
        print(" base:")
        creature_base = factory.create_base()
        print(creature_base.describe())
        print(creature_base.attack())
        if isinstance(creature_base, HealCapability):
            print(creature_base.heal())
        print(" evolved:")
        creature_evolved = factory.create_evolved()
        print(creature_evolved.describe())
        print(creature_evolved.attack())
        if isinstance(creature_evolved, HealCapability):
            print(creature_evolved.heal())

    # cria uma criatura evoluida
    def fact_create_transform(factory: TransformCreatureFactory) -> None:
        print(" base:")
        creature_base = factory.create_base()
        print(creature_base.describe())
        print(creature_base.attack())
        if isinstance(creature_base, TransformCapability):
            print(creature_base.transform())
            print(creature_base.attack())
            print(creature_base.revert())
        print(" evolved:")
        creature_evolved = factory.create_evolved()
        print(creature_evolved.describe())
        print(creature_evolved.attack())
        if isinstance(creature_evolved, TransformCapability):
            print(creature_evolved.transform())
            print(creature_evolved.attack())
            print(creature_evolved.revert())

    # Testando Criatura com capacidade de cura
    print("Testing Creature with healing capability")
    fact_create_heal(HealingCreatureFactory())

    print()

    # Testando Criatura com capacidade de transformação
    print("Testing Creature with transform capability")
    fact_create_transform(TransformCreatureFactory())


if __name__ == "__main__":
    main_capacitor()
