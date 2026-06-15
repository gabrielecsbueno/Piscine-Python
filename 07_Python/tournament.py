import ex0
import ex1
import ex2
from ex2.tournament import BattleException


def main_tournament():

    def battle(opponents: list) -> None:
        print("*** Tournament ***")
        print(f"{len(opponents)} opponents involved")
        print()

        # cria criaturas e estrategias para cada participante
        participants = []
        for (factory, StrategyClass) in opponents:
            creature = factory.create_base()
            strategy = StrategyClass(creature)
            participants.append((creature, strategy))

        # cada participante luta contra todos os outros (sem repetir pares)
        for i in range(len(participants)):
            for j in range(i + 1, len(participants)):
                creature_1, strategy_1 = participants[i]
                creature_2, strategy_2 = participants[j]

                print("* Battle *")
                print(creature_1.describe())
                print("vs.")
                print(creature_2.describe())
                print("now fight!")

                try:
                    strategy_1.act()
                    strategy_2.act()
                except BattleException as e:
                    print(f"Battle error, aborting tournament: {e}")
                    return
                print()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (ex0.FlameFactory(), ex2.NormalStrategy),
        (ex1.HealingCreatureFactory(), ex2.DefensiveStrategy),
    ])

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (ex0.FlameFactory(), ex2.AggressiveStrategy),
        (ex1.HealingCreatureFactory(), ex2.DefensiveStrategy),
    ])
    print()
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (ex0.AquaFactory(), ex2.NormalStrategy),
        (ex1.HealingCreatureFactory(), ex2.DefensiveStrategy),
        (ex1.TransformCreatureFactory(), ex2.AggressiveStrategy),
    ])


if __name__ == "__main__":
    main_tournament()
