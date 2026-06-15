'''

Este exercício requer o uso de geradores (generators) com a palavra-chave yield
para criar fluxos de dados em tempo real.
Você deve implementar funções geradoras que produzem valores sob demanda em
vez de armazenar tudo na memória.
- Crie uma função geradora infinita gen_event() que escolhe um nome aleatório
de uma lista de jogadores, e uma ação aleatória de uma lista de ações.
- Cada vez que next() é chamado neste gerador, ele retorna um novo evento como
uma tupla (nome, ação)
- Da parte principal do seu script, faça um loop mil vezes e exiba todos os
1000 eventos que você obtém do seu gen_event()
- Depois crie uma lista de dez tuplas geradas por gen_event() novamente.
- Crie uma nova função geradora consume_event que recebe a lista
previamente criada, escolhe aleatoriamente um de seus elementos, remove-o da
lista e o retorna com yield, até que a lista esteja vazia.
- Este gerador deve ser usado diretamente na construção for ... in ...

'''

import random
from typing import Generator

'''
- Generator[YieldType, SendType, ReturnType]

O tipo Generator do typing tem 3 parâmetros porque um gerador em Python pode
fazer 3 coisas:

1. YieldType — o que o yield produz
    yield (nome, acao)  # produz tuple[str, str]
É o tipo do valor que sai quando você chama next().

2. SendType — o que pode ser enviado DE VOLTA ao gerador
    valor = yield algo  # valor viria de gen.send(...)
Geradores podem receber valores via .send(). Como o seu gerador não usa
isso, é None.

3. ReturnType — o que o return final retorna
    def gen():
        yield 1
        return "fim"  # acessível via StopIteration.value
Como o seu gerador é infinito e não tem return, é None.
'''

# funcao:
# 1. um nome aleatório de uma lista de jogadores
# 2. uma ação aleatória de uma lista de ações


# Generator[YieldType, SendType, ReturnType]
def gen_event() -> Generator[tuple[str, str], None, None]:
    players = [
        'alice',
        'bob',
        'charlie',
        'dylan'
    ]
    actions = [
        'run',
        'eat',
        'sleep',
        'grab',
        'move',
        'climb',
        'swim',
        'release'
    ]
    while True:
        yield (random.choice(players), random.choice(actions))


# Generator[YieldType, SendType, ReturnType]
def consume_event(events: list) -> Generator[tuple[str, str], None, None]:
    while events:
        event = random.choice(events)
        events.remove(event)
        yield event


def main():
    print("=== Game Data Stream Processor ===")

    # exibir um loop de 1000 eventos que obtém do gen_event()
    gen = gen_event()
    for count in range(1000):
        event = next(gen)
        print(f"Event {count}: Player {event[0]} did action {event[1]}")

    # criar e exibir uma lista de dez tuplas geradas por gen_event() novamente
    list_10_events = []
    for _ in range(10):
        list_10_events.append(next(gen))
    print(f"Built list of 10 events: {list_10_events}")

    for event in consume_event(list_10_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {list_10_events}")


if __name__ == "__main__":
    main()
