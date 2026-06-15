import sys

'''
Seu código primeiro analisará os parâmetros de linha de comando para preencher
seu sistema de inventário.

• Cada parâmetro deve seguir este formato: <nome_item>:<quantidade>
• Descarte parâmetros inválidos com uma mensagem de erro
• Coloque os válidos em um dicionário
• Os valores de <quantidade> no dicionário serão armazenados como int

Operacoes:

• Exibir o inventário
• Criar e exibir a lista de todos os itens que fazem parte do inventário
• Calcular e imprimir a quantidade total de todos os itens no inventário
• Exibir para cada item a porcentagem que representa no inventário
• Reportar os itens mais e menos abundantes (se empate escolher o primeiro da
  linha de comando)
• Adicionar um novo item ao seu inventário
• Exibir novamente
'''


# crio a excessao para o tipo de erro de parametro, caso o usuario informe
class ParameterError(Exception):
    pass


# crio a excessao para tipo de erro de parametros de keys iguais
class RedundantError(Exception):
    pass


def input_validation() -> dict:
    # iniciando com o inventário está vazio
    inventory = {}
    # passa por todos os argumentos
    for arg in sys.argv[1:]:
        try:
            # separo em 2 e coloca na lista temporaria
            arg_list = arg.split(":")
            # se nao tiver dois, chama o erro ParameterError e continua
            if len(arg_list) != 2:
                raise ParameterError
            # se ja tem essa key, chama o erro RedundantError e continua
            if arg_list[0] in inventory:
                raise RedundantError
            # se esta tudo certo, passo para o dicionario
            # se el parametro es un numero, chama o ValueError
            inventory[arg_list[0]] = int(arg_list[1])
        except ParameterError:
            print(f"Error - invalid parameter '{arg}'")
        except RedundantError:
            print(f"Redundant item '{arg_list[0]}' - discarding")
        except ValueError as err:
            print(f"Quantity error for '{arg_list[0]}': {err}")
    return inventory


# funcao para verificar qual o maximo e o minimo do dicionario
# porque nao pode usar o max() e min()
def max_min_int(inventory: dict) -> None:
    # crio uma variavel que vai guardar o nome da primeira keys do dicionario
    most_key = list(inventory.keys())[0]
    # crio uma variavel que vai guardar o valor da primeira keys do dicionario
    most_val = list(inventory.values())[0]
    # crio uma variavel que vai guardar o nome da primeira keys do dicionario
    least_key = most_key
    # crio uma variavel que vai guardar o nome da primeira keys do dicionario
    least_val = most_val

    # transformo o inventory em lista porque o dicionario nao suporta a busca
    # identacao com [0]

    for key in inventory.keys():
        # busco no inventory qual o maior valor
        # se encontra um valor maior que o que ja esta guardado
        if inventory[key] > most_val:
            # salva o valor da key
            most_key = key
            # salva o valor de value
            most_val = inventory[key]
        # se encontra um valor menos que o que ja esta guardado
        if inventory[key] < least_val:
            # salva o valor da key
            least_key = key
            # salva o valor de value
            least_val = inventory[key]

    print(f"Item most abundant: {most_key} with quantity {most_val}")
    print(f"Item least abundant: {least_key} with quantity {least_val}")


def main():
    # verifica se tem argumentos
    try:
        # se nao tem nenhum argumento, sem ser o nome
        if len(sys.argv) < 2:
            raise IndexError
    except IndexError:
        # imprime sintaxe inválida e sai do programa
        print(f"Invalid syntax. Usage: python3 {sys.argv[0]} "
              "<item_name>:<quantity> ...")
    else:
        print("=== Inventory System Analysis ===")
        # valida a entrada e todos os erros
        # coloca em um dicionario
        inventory = input_validation()
        # se nao tem nada no dicionario, sai sem fazer nada
        # obs : 'if not x' retorna um False se tiver
        #       'if x' retorna um True se tiver
        #       'if not not x' retorna True se tiver
        if not inventory:
            return
        # exibir o dicionario
        print("Got inventory:", inventory)
        # exibir as keys
        print("Item list:", list(inventory))
        # soma valor dos itens
        value_sum = sum(inventory.values())
        # exibir a quantidade de itens e a soma do valor
        print(f"Total quantity of the {len(inventory)} items: {value_sum}")
        # exibi a porcentagem de cada keys referente ao seu valor
        for key in inventory.keys():
            result = (inventory[key] * 100) / value_sum
            print(f"Item {key} represents {result:.1f}%")
        # chama a funcao para exibir o maximo e o minimo
        max_min_int(inventory)
        # atualiza o inventario com um novo valor
        inventory.update({"magic_item": 1})
        print("Updated inventory:", inventory)


if __name__ == "__main__":
    main()
