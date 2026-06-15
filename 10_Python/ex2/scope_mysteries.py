# Autorizado: nonlocal
from collections.abc import Callable
from typing import Union


def main() -> None:
    print('Testing mage counter...')
    print()

    def mage_counter() -> Callable:
        '''
        Esta funcion crea un closure de conteo y retorna una función que
        cuenta cuántas veces fue llamada
        '''
        count: int = 0

        def counter() -> int:
            nonlocal count
            count += 1
            return count

        return counter

    counter_a: Callable = mage_counter()
    counter_b: Callable = mage_counter()

    for x in range(1, 4):
        call = counter_a()
        print(f'    counter_a call {x}: {call}')
    print()
    for x in range(1, 3):
        call = counter_b()
        print(f'    counter_b call {x}: {call}')
    print()

    # ---

    print('Testing spell accumulator...')
    print()

    def spell_accumulator(initial_power: int) -> Callable:
        '''
        Esta funcion crea un acumulador de poder y retorna una función que
        acumula poder a lo largo del tiempo.
        Comienza con 'initial_power' como base
        '''
        power: int = initial_power

        def accumulator(add_power: int) -> int:
            '''
            Cada llamada agrega el valor de 'add_power' al poder total
            y retorna el nuevo poder total después de cada adición
            '''
            nonlocal power
            power += add_power
            return power

        return accumulator

    accumulator_base_100: Callable = spell_accumulator(100)
    accumulator_base_0: Callable = spell_accumulator(0)

    print('    Base 100, add 20:', accumulator_base_100(20))
    print('    Base 100, add 10:', accumulator_base_100(10))

    print('    Base 0, add 10:', accumulator_base_0(10))
    print('    Base 0, add 30:', accumulator_base_0(30))
    print()

    # ---

    print('Testing enchantment factory...')
    print()

    def enchantment_factory(enchantment_type: str) -> Callable:
        '''
        Esta funcion crea funciones de encantamiento y retorna una función
        que aplica el encantamiento especificado en 'enchantment_type'.
        Cada factory crea funciones con tipos de encantamiento diferentes
        '''
        enchantment: str = enchantment_type

        def apply(item_name: str) -> str:
            '''
            Recibe el nombre de un item y retorna la descripción encantada
            '''
            return f"{enchantment} {item_name}"
        return apply

    list_itens: list[str] = ["Arrow", "Bow", "Shield", "Blade"]

    # Crea las "fábricas" pasando el tipo de encantamiento
    ancient_factory: Callable = enchantment_factory("Ancient")
    eletric_factory: Callable = enchantment_factory("Eletric")

    # Cada una retorna una función que "recuerda" el encantamiento
    for item in list_itens:
        print("    ", ancient_factory(item))
    print()
    for item in list_itens:
        print("    ", eletric_factory(item))
    print()

    # ---

    print('Testing memory vault...')
    print()

    def memory_vault() -> dict[str, Callable]:
        '''
        Esta funcion crea un sistema de gestión de memoria y retorna un
        dict con las funciones 'store' y 'recall'.
        Usa closure para mantener el almacenamiento de memoria privado
        '''
        vault: dict = {}

        def store(key: str, value: int) -> None:
            '''
            Recibe (key, value) y almacena el valor en el vault
            '''
            vault[key] = value

        def recall(key: str) -> Union[int, str]:
            '''
            Recibe (key) y retorna el valor almacenado o 'Memory not found'
            '''
            if key in vault:
                return vault[key]
            else:
                return 'Memory not found'

        return {'store': store, 'recall': recall}

    # crea el vault y retorna el diccionario con las funciones store y recall
    vault = memory_vault()

    # extrae las funciones del diccionario para llamarlas directamente
    store = vault['store']
    recall = vault['recall']

    # almacena el valor 42 con la clave 'secret'
    store('secret', 42)
    print("    Store 'secret' = 42")
    # busca la clave que existe — debe retornar 42
    print("    Recall 'secret':", recall('secret'))
    # busca una clave que no existe — debe retornar 'Memory not found'
    print("    Recall 'unknown':", recall('unknown'))
    print()


if __name__ == '__main__':
    main()


'''
Entendendo os conceitos:
- Lexical scoping e quando uma função enxerga as variáveis do escopo onde foi
definida, não onde foi chamada
- Closure e a função interna que captura variáveis do escopo externo e as
mantém vivas após o retorno da função externa

- O nonlocal permite modificar uma variável do escopo externo (não global)
dentro da função interna. Sem nonlocal, você só pode ler a variável, não
reatribuí-la um novo valor

- Definir uma variavel global nao e interessante porque essas variáveis criam
estado compartilhado invisível, dificultam testes e composição

ex:
# SEM nonlocal — cria nova variável local
def func_externa():
    var_externa = "Valor Externo (enclosing)"

    def func_interna():
        var_externa = "Valor Interna (clousure)"

    func_interna()
    return var_externa

print(func_externa())

# COM nonlocal — correto
def func_externa():
    var_externa = "Valor Externo (enclosing)"

    def func_interna():
        nonlocal var_externa
        var_externa = "Valor Interna (clousure)"

    func_interna()
    return var_externa

print(func_externa())
'''
