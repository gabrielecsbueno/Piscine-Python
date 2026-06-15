import random

'''
- Crie uma função gen_player_achievements() que usará uma grande lista fixa de
conquistas para atribuir aleatoriamente um conjunto a um jogador.
- Escolha um número aleatório de conquistas, depois selecione esse número de
conquistas da lista para construir e retornar o conjunto.

Então seu código irá:
• Gerar conjuntos de conquistas para um mínimo de quatro jogadores diferentes
• Rastrear conquistas únicas entre todos os jogadores
• Encontrar conquistas compartilhadas por todos os jogadores
• Para cada jogador, identificar as conquistas que ninguém mais tem
• Para cada jogador, listar as conquistas que faltam para ter todas
'''


def gen_player_achievements() -> set:
    all_achievements = ['World Savior', 'Speed Runner', 'Crafting Genius',
                        'Treasure Hunter', 'Collector Supreme', 'First Steps',
                        'Sharp Mind', 'Survivor', 'Strategist', 'Boss Slayer',
                        'Master Explorer', 'Unstoppable', 'Untouchable']
    value = random.randint(1, len(all_achievements))
    return set(random.sample(all_achievements, k=value))


def main():
    print("=== Achievement Tracker System ===")
    print()

    p_alice = gen_player_achievements()
    p_bob = gen_player_achievements()
    p_charlie = gen_player_achievements()
    p_dylan = gen_player_achievements()

    print("Player Alice:", p_alice)
    print("Player Bob:", p_bob)
    print("Player Charlie:", p_charlie)
    print("Player Dylan:", p_dylan)

    print()
    distinct_achievements = p_alice.union(p_bob, p_charlie, p_dylan)
    print("All distinct achievements:", distinct_achievements)
    print()
    # common_achievements = p_alice & p_bob & p_charlie & p_dylan
    common_achievements = p_alice.intersection(p_bob, p_charlie, p_dylan)
    print("Common achievements:", common_achievements)
    print()
    # only_alice = p_alice - p_bob - p_charlie - p_dylan
    only_alice = p_alice.difference(p_bob, p_charlie, p_dylan)
    print("Only Alice has:", only_alice)
    only_bob = p_bob.difference(p_alice, p_charlie, p_dylan)
    print("Only Bob has:", only_bob)
    only_charlie = p_charlie.difference(p_bob, p_alice, p_dylan)
    print("Only Charlie has:", only_charlie)
    only_dylan = p_dylan.difference(p_bob, p_charlie, p_alice)
    print("Only Dylan has:", only_dylan)
    print()
    missing_alice = distinct_achievements.difference(p_alice)
    print("Alice is missing:", missing_alice)
    missing_bob = distinct_achievements.difference(p_bob)
    print("Bob is missing:", missing_bob)
    missing_charlie = distinct_achievements.difference(p_charlie)
    print("Charlie is missing:", missing_charlie)
    missing_dylan = distinct_achievements.difference(p_dylan)
    print("Dylan is missing:", missing_dylan)


if __name__ == "__main__":
    main()

'''
Ajuste o número total de conquistas e quantas você seleciona para cada
jogador, de modo que todos os conjuntos solicitados provavelmente sejam
não-vazios. A propósito, como Python imprime um conjunto vazio, e por
quê?
'''
'''
EXEMPLO:
python3 ft_achievement_tracker.py
=== Achievement Tracker System ===

Player Alice: {'Crafting Genius', 'World Savior', 'Master Explorer',
'Collector Supreme', 'Untouchable', 'Boss Slayer'}
Player Bob: {'Crafting Genius', 'Strategist', 'World Savior',
'Master Explorer', 'Unstoppable', 'Collector Supreme', 'Untouchable'}
Player Charlie: {'Strategist', 'Speed Runner', 'Survivor', 'Master Explorer',
'Treasure Hunter', 'First Steps', 'Collector Supreme', 'Untouchable',
'Sharp Mind'}
Player Dylan: {'Strategist', 'Speed Runner', 'Unstoppable', 'Untouchable',
'Boss Slayer'}
All distinct achievements: {'Crafting Genius', 'Strategist', 'World Savior',
'Speed Runner', 'Survivor', 'Master Explorer', 'Treasure Hunter',
'Unstoppable', 'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
'Boss Slayer'}

Common achievements: {'Untouchable'}

Only Alice has: set()
Only Bob has: set()
Only Charlie has: {'Survivor', 'Treasure Hunter', 'First Steps', 'Sharp Mind'}
Only Dylan has: set()

Alice is missing: {'Strategist', 'Speed Runner', 'Survivor', 'Treasure Hunter',
    'Unstoppable', 'Hidden Path Finder', 'First Steps', 'Sharp Mind'}
Bob is missing: {'Speed Runner', 'Survivor', 'Treasure Hunter',
    'Hidden Path Finder', 'First Steps', 'Sharp Mind', 'Boss Slayer'}
Charlie is missing: {'Crafting Genius', 'World Savior', 'Hidden Path Finder',
    'Unstoppable', 'Boss Slayer'}
Dylan is missing: {'Crafting Genius', 'World Savior', 'Survivor',
    'Master Explorer', 'Treasure Hunter', 'Hidden Path Finder', 'First Steps',
    'Collector Supreme', 'Sharp Mind'}
'''
