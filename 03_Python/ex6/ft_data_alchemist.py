'''

Este exercício requer o uso de list comprehensions e dictionary comprehensions
para transformar e filtrar dados de forma eficiente.
- Crie uma lista de nomes de jogadores, onde alguns estão em maiúsculas e
outros não.
- Crie duas list comprehensions:
    - a primeira cria uma nova lista com todos os nomes em maiúsculas,
    - a segunda cria uma nova lista apenas com os nomes em maiúsculas da lista
    inicial.
- Agora, vamos criar um dicionário a partir desta lista completa de nomes de
jogadores em maiúsculas. Os nomes serão as chaves e os valores serão pontuações
geradas aleatoriamente em um intervalo definido.

Obviamente, uma list comprehension construirá este dicionário.

Em seguida, um segundo dicionário será criado, com pontuações acima da média,
também usando uma list comprehension.

'''

# Only Authorized: import random, random.*, print(), len(), sum(), round()

import random


def main():
    players = [
        'Alice',
        'bob',
        'Charlie',
        'dylan',
        'Emma',
        'Gregory',
        'john',
        'kevin',
        'Liam']

    print("=== Game Data Alchemist ===")
    print()

    print(f"Initial list of players: {players}")

    new_players = [x.capitalize() for x in players]
    print(f"New list with all names capitalized: {new_players}")

    only_players_capitalized = [x for x in players if x[0].isupper()]
    print(f"New list of capitalized names only: {only_players_capitalized}")

    dic_p = {x: random.randint(50, 1000) for x in new_players}
    print(f"Score dict: {dic_p}")

    average = sum(dic_p[x] for x in dic_p) / len(dic_p)
    print(f"Score average is {average:.1f}")

    new_dic_p = {x: dic_p[x] for x in dic_p if dic_p[x] > average}
    print(f"High scores: {new_dic_p}")


if __name__ == "__main__":
    main()
