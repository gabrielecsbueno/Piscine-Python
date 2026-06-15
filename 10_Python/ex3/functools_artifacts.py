# Autorizado: functools, operator
from collections.abc import Callable
from typing import Any
from operator import add, mul
import functools


def main() -> None:
    print('Testing spell reducer...')
    print()

    def spell_reducer(spells: list[int], operation: str) -> int:
        '''
        Reduce los poderes de hechizos usando functools.reduce.

        Soporta operaciones: "add", "multiply", "max", "min".
        Retorna 0 si la lista está vacía.
        Lanza ValueError para operaciones desconocidas.
        '''
        if not spells:
            return 0
        if operation == "add":
            return functools.reduce(add, spells)
        elif operation == "multiply":
            return functools.reduce(mul, spells)
        elif operation == "max":
            return functools.reduce(max, spells)
        elif operation == "min":
            return functools.reduce(min, spells)
        else:
            raise ValueError(
                'ERROR - Supported operations: "add", "multiply", "max", "min"'
            )

    # testes
    try:
        print('    Sum:', spell_reducer([10, 5, 5, 2], 'add'))
        print('    Multiply:', spell_reducer([10, 5], 'multiply'))
        print('    Max:', spell_reducer([10, 5, 7, 2], 'max'))
        print('    Min:', spell_reducer([10, 5, 7, 2], 'min'))
        # print('    Not spells:', spell_reducer('', 'min'))
        print()
        # invalidos
        print(spell_reducer([10, 5, 7, 2], 'sub'))
    except ValueError as err:
        print('   ', err)
    print()

    # ---

    print('Testing partial enchanter...')
    print()

    def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
        '''
        Crea aplicaciones parciales con functools.partial.

        Recibe función base con firma (power, element, target) -> str.
        Retorna dict con versiones: "fire", "ice", "lightning".
        Cada versión pre-rellena power=50 y el elemento correspondiente.
        Lanza ValueError si base_enchantment es None.
        '''
        if not base_enchantment:  # type: ignore[truthy-function]
            raise ValueError
        func_partial: dict[str, Callable] = {
            "fire": functools.partial(base_enchantment, power=50,
                                      element="fire"),
            "ice": functools.partial(base_enchantment, power=50,
                                     element="ice"),
            "lightning": functools.partial(base_enchantment, power=50,
                                           element="lightning"),
        }
        return func_partial

    # testes
    # funcao
    base_enchantment: Callable[[int, str, str], str] = (
        lambda power, element, target:
        f"{element.capitalize()} spell with power {power} hits {target}!"
        )
    try:
        # chama o partial_enchanter
        spells = partial_enchanter(base_enchantment)

        # testando cada versão — só precisa passar target
        print('   ', spells["fire"](target="dragon"))
        print('   ', spells["ice"](target="goblin"))
        print('   ', spells["lightning"](target="troll"))
        print()
        # invalidos
        print('   ', spells["unknown"](target="troll"))
        # partial_enchanter(None)  # type: ignore[arg-type]
    except ValueError:
        print("    ERROR - correctly for None input")
    except KeyError as err:
        print(f'    ERROR - Key {err} invalid')
    print()

    # ---

    print('Testing memoized fibonacci...')
    print()

    # cache com limite de 128 chamadas recentes
    @functools.lru_cache(maxsize=128)
    def memoized_fibonacci(n: int) -> int:
        '''
        Calcula el n-ésimo número de Fibonacci con memoización.

        Usa functools.lru_cache para almacenar resultados previos.
        fib(0) = 0, fib(1) = 1.
        Lanza ValueError para n negativo.
        '''
        if n < 0:
            raise ValueError("ERROR - 'n' must be >= 0")
        if n < 2:
            return n
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

    try:
        print('    fib(10):', memoized_fibonacci(10))
        print('    fib(30):', memoized_fibonacci(30))
        # teste que vem do cache
        print('    fib(10) again:', memoized_fibonacci(10))
        print('    Cache info:', memoized_fibonacci.cache_info())
        print()
        # invalidos
        # memoized_fibonacci(-1)
        memoized_fibonacci('')
    except ValueError as err:
        print('   ', err)
    except TypeError:
        print("    ERROR - not supported between instances of 'str' and 'int'")

    print()

    # ---

    print('Testing spell dispatcher...')
    print()

    def spell_dispatcher() -> Callable[[Any], str]:
        '''
        Crea un sistema de despacho único con functools.singledispatch.

        La función base maneja tipos desconocidos (Any).
        Tipos soportados: int (daño), str (encantamiento),
        list (multi-lanzamiento). Retorna la función dispatcher.
        '''
        # Função BASE — recebe qualquer tipo desconhecido
        @functools.singledispatch
        def base_dispatcher(value: Any) -> str:
            return f"ERROR - Unknown type: {type(value)}"

        # Registra handlers (manipuladores) por tipo com .register()
        @base_dispatcher.register(int)
        def damage(value: int) -> str:
            return f"Damage spell: {value} damage!"

        @base_dispatcher.register(str)
        def enchantment(value: str) -> str:
            return f"Enchantment: '{value}' cast!"

        @base_dispatcher.register(list)
        def mult_cast(value: list[Any]) -> str:
            return f"Multi-cast: {len(value)} spells"

        return base_dispatcher

    # testes
    dispatcher = spell_dispatcher()
    print('   ', dispatcher(42))
    print('   ', dispatcher("fireball"))
    print('   ', dispatcher([1, 2, 3]))
    # invalido
    print('   ', dispatcher(3.14))


if __name__ == "__main__":
    main()

'''
modulos functools:

- reduce(func, iterable): aplica func acumulativamente
ex: reduce(add, [1,2,3]) → (1+2)+3 = 6
- partial(func, *args, kwargs): congela argumentos de uma função, criando uma
versão especializada
- lru_cache: 'e um decorarod que armazena em cache o resultado de chamadas de
funções. Quando a função é chamada novamente com os mesmos argumentos, ela
retorna o resultado armazenado em vez de recalculá-lo, otimizando processos
demorados.
- singledispatch: é um decorador que permite criar funções genéricas, onde o
comportamento da função muda de acordo com o tipo do primeiro argumento. Ele
substitui longas sequências de if/elif/else ou checagens com isinstance()

- Módulo operator: versões funcionais dos operadores Python
ex: add equivale a lambda x, y: x + y, mas mais rápido e com nome claro

'''
