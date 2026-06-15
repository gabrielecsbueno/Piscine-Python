# Autorizado: functools.wraps, staticmethod
import functools
from collections.abc import Callable
import time
from typing import Any


def spell_timer(func: Callable) -> Callable:
    # aqui guardo os metadados (preserva `__name__`, `__doc__` e outros) da
    # função original — sem isso, todos os seus decorators teriam o mesmo nome
    # (`wrapper`)
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        # antes de executar a funcao
        print(f'Casting {func.__name__}...')
        # guardo o time inicial
        inicio = time.time()
        # executo a funcao
        result = func(*args, **kwargs)
        # vejo o time final
        fim = time.time()
        # retorno
        print(f'Spell completed in {fim-inicio:.3f} seconds')
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    '''
    Decorador externo: recebe os parâmetros do decorador.
    '''
    def factory(func: Callable) -> Callable:
        '''
        Decorador interno: valida se .
        '''
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            power = kwargs.get('power', args[-1])
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return 'Insufficient power for this spell'
        return wrapper
    return factory


def retry_spell(max_attempts: int) -> Callable:
    '''
    Decorator de retry:
    • Crie um decorator que tenta novamente feitiços que falharam
    • Se a função levantar uma exceção, tente novamente até max_attempts vezes
    • Imprima "Spell failed, retrying... (attempt n/max_attempts)"
    • Se todas as tentativas falharem, retorne "Spell casting failed after
    max_attempts attempts"
    • Se uma tentativa for bem-sucedida, retorne seu resultado normalmente
    '''
    def retry(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    result = func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
                else:
                    return result
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return retry


class MageGuild:
    def __init__(self):
        pass

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        '''
        Método estático, não precisa de instância nem da classe para
        ser chamado
        Verifica se o nome é válido.
        Um Nome é válido se: tiver pelo menos 3 caracteres (len(name) > 3) e
        contiver apenas letras/espaços (all([True, True,...]) = True
        ou all([True, False...]) = False)
        '''
        if len(name) < 3:
            return False
        return all(c.isalpha() or c == ' ' for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f'Successfully cast {spell_name} with {power} power')


def main() -> None:
    print('-'*55)
    print('Testing spell timer...')
    print()

    @spell_timer
    def test_1() -> None:
        print('Buenos dias')

    test_1()

    print('-'*55)
    print('Testing power validator...')
    print()

    @power_validator(10)
    def test_2(spell: str, power: int) -> None:
        print(f'{spell} ({power} power)')

    test_2('Bombarda', 12)

    print('-'*55)
    print('Testing validate mage name (Class MageGuild)...')
    print()

    print(MageGuild.validate_mage_name('Gabriele Bueno'))

    print('-'*55)
    print('Testing cast spell (Class MageGuild)...')
    print()

    mage_guild = MageGuild()
    print(mage_guild.cast_spell('Bombarda', 12))

    print('-'*55)


if __name__ == "__main__":
    main()
