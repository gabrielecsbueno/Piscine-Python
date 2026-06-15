from ex0 import FlameFactory, AquaFactory, CreatureFactory


# usa uma única função que recebe um objeto de fábrica
# outra função que recebe ambas as fábricas e faz as Criaturas base lutarem
def main_battle():
    def fact_create(factory: CreatureFactory) -> None:
        creature_base = factory.create_base()
        print(creature_base.describe())
        print(creature_base.attack())

        creature_evolved = factory.create_evolved()
        print(creature_evolved.describe())
        print(creature_evolved.attack())

    def fact_attack(f1: CreatureFactory, f2: CreatureFactory) -> None:
        creature_f1 = f1.create_base()
        creature_f2 = f2.create_base()

        print(creature_f1.describe())
        print(" vs.")
        print(creature_f2.describe())

        print(" fight!")

        print(creature_f1.attack())

        print(creature_f2.attack())

    # Testando fabrica
    print("Testing factory")

    fact_create(FlameFactory())
    print()

    # Testando fabrica
    print("Testing factory")

    fact_create(AquaFactory())
    print()

    # Testando batalha
    print("Testing battle")
    fact_attack(FlameFactory(), AquaFactory())


if __name__ == "__main__":
    main_battle()
