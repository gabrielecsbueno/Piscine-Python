# Autorizado: map, filter, sorted, min, max, round, sum, len


def main() -> None:
    print("01. Testing artifact sorter...")
    print()

    def artifact_sorter(artifacts: list[dict]) -> list[dict]:
        '''
        Essa funcao ordena artefatos magicos por 'power' em ordem decrescente
        O lambda define a chave de ordenacao: extrai o valor 'power' de cada
        dict
        '''
        return list(sorted(artifacts, key=lambda x: x['power'], reverse=True))

    # TESTANDO
    # crio uma lista de artefatos
    list_artifact: list[dict] = [
            {'name': 'Night Cloak', 'power': 15, 'type': 'Cape'},
            {'name': 'Sorcerer Hat', 'power': 8, 'type': 'Hat'},
            {'name': 'Dragon Leather Boots', 'power': 12, 'type': 'Boots'},
            {'name': 'Walnut Wand', 'power': 20, 'type': 'Wand'},
            {'name': 'Ashwinder Cloak', 'power': 10, 'type': 'Cape'},
            {'name': 'Weaving Gloves', 'power': 6, 'type': 'Gloves'}
        ]
    # ordeno artefatos magicos por 'power' em ordem decrescente
    sorted_artifacts = artifact_sorter(list_artifact)

    # printando os resultados ordenados
    size = len(sorted_artifacts) - 1
    print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']}"
          f"power) comes before {sorted_artifacts[size]['name']} "
          f"({sorted_artifacts[size]['power']} power)")
    print()

    # ---

    print("02. Testing mages filter...")
    print()

    def power_filter(mages: list[dict], min_power: int) -> list[dict]:
        '''
        Filtra magos cujo 'power' seja >= min_power
        O lambda define a condicao de filtragem para cada mago da lista
        '''
        return list(filter(lambda mage: mage['power'] >= min_power, mages))

    # TESTANDO
    # crio uma lista de magos/bruxos
    list_mages: list[dict] = [
        {'name': 'Eleazar Fig', 'power': 30, 'element': 'Ancient Magic'},
        {'name': 'Matilda Weasley', 'power': 15, 'element': 'Fire'},
        {'name': 'Sebastian Sallow', 'power': 24, 'element': 'Dark Arts'},
        {'name': 'Natsai Onai', 'power': 43, 'element': 'Lightning'},
        {'name': 'Poppy Sweeting', 'power': 12, 'element': 'Nature'},
        {'name': 'Amit Thakkar', 'power': 10, 'element': 'Astral'}
    ]

    min_power = 20

    # filtro magos cujo power seja >= min_power(20)
    filtered = power_filter(list_mages, min_power)

    # printando os resultados filtrados
    print(f"Mages with greater power than {min_power}: ")
    for mage in filtered:
        print(f"    {mage['name']} ({mage['power']} power)")
    print()

    # ---

    print("03. Testing spell transformer...")
    print()

    def spell_transformer(spells: list[str]) -> list[str]:
        '''
        Essa funcao transforma cada nome de feitico adicionando o prefixo
        e sulfixo
        O lambda aplica a transformacao a cada elemento da lista via map()
        '''
        return list(map(lambda spell: f"* {spell} *", spells))

    # crio a lista de fenticos
    list_spell: list[str] = ["Revelio", "Lumos", "Protego", "Stupefy", "Accio",
                             "Levioso", "Reparo", "Incendio", "Expelliarmus",
                             "Bombarda"]

    # TESTANDO
    # printo o resultado com prefixo e sulfixo
    for spell in spell_transformer(list_spell):
        print(spell)
    print()

    # ---

    print("04. Testing mages max, min and average power ...")
    print()

    def mage_stats(mages: list[dict]) -> dict:
        '''
        Calcula estatisticas de poder dos magos
        O max/min usam lambda para extrair 'power' de cada dict e comparar
        sum usa map com lambda para extrair apenas os valores numericos
        antes de somar
        '''
        return {
            'max_power': max(mages, key=lambda m: m['power'])['power'],
            'min_power': min(mages, key=lambda m: m['power'])['power'],
            'avg_power': round(
                sum(map(lambda m: m['power'], mages)) / len(mages), 2
            )
        }

    # aqui calculo as estatisticas de poder dos magos
    stats = mage_stats(list_mages)

    # printo os resultados
    print(f"The most powerful mage has {stats['max_power']}")
    print(f"The less powerful mage has {stats['min_power']}")
    print(f"The average power level among mages is {stats['avg_power']}")


if __name__ == "__main__":
    main()
