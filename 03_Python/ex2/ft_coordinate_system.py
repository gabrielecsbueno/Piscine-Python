'''
Este exercício requer o uso de tuplas para armazenar coordenadas 3D (x, y, z).
Primeiro, escreva uma função get_player_pos() que:
• Pede ao usuário as novas coordenadas do jogador no formato x,y,z
• Trata entradas impróprias
• Tenta novamente até que um conjunto válido de coordenadas seja fornecido
• Retorna uma tupla contendo as coordenadas 3D atuais do jogador

O código terá que:
• Obter um primeiro conjunto de coordenadas
• Exibir a tupla e depois exibir cada coordenada separadamente
• Calcular a distância até o centro 3D (0, 0, 0) (veja abaixo)
• Obter um novo conjunto de coordenadas
• Calcular a distância entre o segundo e o primeiro conjunto de coordenadas
'''

import math


def get_player_pos():

    # funcoes auxiliares --------------------------------------------
    # entrada de informacoes
    def input_list() -> tuple:
        while True:
            # podem ser recebidos (10,20,30) ou (10, 20, 30) ou (10 , 20 , 30)
            str_input = input("Enter new coordinates as floats in format "
                              "'x,y,z':")
            # retira todos os espacos
            str_args = ""
            for value in str_input:
                if value != " ":
                    str_args = str_args + value
            # divide pela vírgula
            args_list = str_args.split(",")
            # valida que tem exatamente 3 valores
            if len(args_list) != 3:
                print("Invalid syntax")
                continue  # aqui volta pro início do loop
            # tenta converter cada parte
            for arg in args_list:
                try:
                    float(arg)
                except ValueError as err:
                    print(f"Error on parameter '{arg}': {err}")
                    break
            else:
                return (float(args_list[0]),
                        float(args_list[1]),
                        float(args_list[2]))

    # fim das funcoes auxiliares --------------------------------------------

    # comeca o programa principal
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    # primeira entrada de informacoes, que retorna um tipo tuple
    p1 = input_list()
    print("Got a first tuple: ", p1)
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
    # # calcula a distancia ate o centro
    x1 = p1[0]
    y1 = p1[1]
    z1 = p1[2]
    print("Distance to center: "
          f"{math.sqrt((0-x1)**2 + (0-y1)**2 + (0-z1)**2):.4f}")

    # segunda entrada de informacoes, que retorna um tipo tuple
    print("\nGet a second set of coordinates")
    p2 = input_list()
    x2 = p2[0]
    y2 = p2[1]
    z2 = p2[2]
    print("Distance between the 2 sets of coordinates:"
          f"{math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2):.4f}")


if __name__ == "__main__":
    get_player_pos()
