# Autorizado: callable(), Callable
'''
Callable é usado para especificar que um argumento ou retorno de uma função
deve ser um objeto chamável. A sintaxe básica é
Callable[[argumentos], tipo_de_retorno]
'''
from collections.abc import Callable


def main() -> None:

    def heal(target: str, power: int) -> str:
        '''
        A funcao é um feitiço que recebe um alvo e um nível de poder
        e retorna uma string descrevendo o que aconteceu.
        '''
        return f"Heal restores {target} for {power} HP"

    def fireball(target: str, power: int) -> str:
        '''
        A funcao é um feitiço que recebe um alvo e um nível de poder
        e retorna uma string descrevendo o que aconteceu.
        '''
        return f"{target} launches a fireball for {power} HP"

    print("Testing spell combiner...")
    print()

    def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
        '''
        Essa funcao combina dois feitiços e retorna uma nova função que
        chama ambos os feitiços com os mesmos argumentos
        '''
        def combined(target: str, power: int) -> tuple:
            '''
            Essa funcao retorna os feitiço combinado como uma tupla de
            ambos os resultados
            '''
            return (spell1(target, power), spell2(target, power))
        return combined

    # chama os 2 dois fenticoes combinados, seria como tranformar essa variavel
    # em uma funcao
    combined = spell_combiner(heal, fireball)

    print("Combined spell result:")
    # executa a 'funcao' combined
    result_combined = combined('Phoenix', 87)
    # printa a tupla
    for x in result_combined:
        print("     ", x)
    print()

    # ---

    print("Testing power amplifier...")
    print()

    def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
        '''
        Essa funcao amplifica o poder do feitiçoe retorna uma função com a
        mesma assinatura do feitiço original
        '''
        def amplified(target: str, power: int) -> str:
            '''
            Essa funcao retorna um novo feitiço onde o poder é multiplicado
            antes de ser lançado
            '''
            return base_spell(target, power * multiplier)
        return amplified

    # cria a funcao para amplificar 3 x fireball
    mega_fireball = power_amplifier(fireball, 3)
    # cria a funcao para amplificar 4 x heal
    mega_heal = power_amplifier(heal, 4)

    print("Amplified attack power:")
    print("     ", mega_fireball('Dragon', 60))
    print("Amplified heal power:")
    print("     ", mega_heal('Unicorn', 10))
    print()

    # ---

    print("Testing conditional caster...")
    print()

    # crio uma funcao anonima apenas para usar como condicional
    full_power: Callable[[str, int], bool] = lambda target, power: power >= 10

    def conditional_caster(condition: Callable, spell: Callable) -> Callable:
        '''
        Essa funcao lança feitiço condicionalmente e retorna um novo feitiço
        que só é lançado se uma condição for verdadeira
        '''
        def caster(target: str, power: int) -> str:
            '''
            Se a condição falhar, retorne "Spell fizzled"
            Tanto condition quanto spell recebem os mesmos argumentos
            '''
            if condition(target, power):
                return spell(target, power)
            else:
                return 'Spell fizzled'
        return caster
    # cria a funcao condicional de fireball
    caster_fireball = conditional_caster(full_power, fireball)
    # cria a funcao condicional de heal
    caster_heal = conditional_caster(full_power, heal)

    print("Checking the spell condition: Atack")
    print("     ", caster_fireball('Dragon', 9))
    print("Checking the spell condition: Heal")
    print("     ", caster_heal('Phoenix', 19))
    print()

    # ---

    print("Testing spell sequence...")
    print()

    # crio uma lista com todas as funcoes de fenticoes
    list_spell = [fireball, heal]

    def spell_sequence(spells: list) -> Callable:
        '''
        Essa funcao cria sequência de feitiços e retorna
        uma função que lança todos os feitiços em ordem
        '''
        def sequence(target: str, power: int) -> list:
            '''
            Cada feitiço recebe os mesmos argumentos
            Retorna uma lista com todos os resultados
            '''
            return [spell(target, power) for spell in spells]
        return sequence

    # cria a funcao que lanca todos os fenticoes da lista
    sequence = spell_sequence(list_spell)

    print("Checking the spell sequence:")
    result_sequence = sequence('Dragon', 10)
    for x in result_sequence:
        print("     ", x)


if __name__ == "__main__":
    main()
