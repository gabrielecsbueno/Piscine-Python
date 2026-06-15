'''
Este exercício requer que você use listas para armazenar pontuações e blocos
try/except para tratar entradas inválidas (ex.: quando um usuário
fornece valores não numéricos).
Você receberá pontuações de jogo como parâmetros de linha de comando.
Você precisa:
• Processar os argumentos de linha de comando
• Tratar os vários casos de erro (sem argumentos, valores não numéricos) com
mensagens apropriadas
• Criar uma nova lista para armazenar e organizar as pontuações
• Calcular algumas estatísticas básicas que deixariam qualquer jogador feliz
(quantidade, total, média, máximo, mínimo e amplitude)
• Fazer a saída parecer legal o suficiente para impressionar seus amigos gamers
(você pode imitar o exemplo novamente)
• Se entradas válidas e inválidas forem fornecidas via linha de comando,
descarte as inválidas e prossiga com as entradas válidas restantes, a menos que
nenhuma reste.
'''

import sys


def main():
    print("=== Player Score Analytics ===")
    try:
        # se nao tiver nenhum argumento alem do nome
        if len(sys.argv) < 2:
            raise IndexError
        numbers = []
        # cria uma nova lista
        for arg in sys.argv[1:]:
            # tenta converter tudo para inteiro e guarda na nova lista
            try:
                numbers.append(int(arg))
            # se encontrar algum que nao é numero ele imprime o erro e passa
            # para p proximo
            except ValueError:
                print(f"Invalid parameter: '{arg}'")
        # se nao tiver nada no numbers ele sai
        if not numbers:
            raise IndexError
        # se tiver ele continua
        print("Scores processed:", numbers)
        print("Total players:", len(numbers))
        print("Total score:", sum(numbers))
        print("Average score:", (sum(numbers)/len(numbers)))
        print("High score:", max(numbers))
        print("Low score:", min(numbers))
        print("Score range:", max(numbers) - min(numbers))
    except IndexError:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} "
              "<score1> <score2> ...")


if __name__ == "__main__":
    main()

'''
SAIDA PADRAO:

$> python3 ft_score_analytics.py 1500 2300 1800 2100 1950
=== Player Score Analytics ===
Scores processed: [1500, 2300, 1800, 2100, 1950]
Total players: 5
Total score: 9650
Average score: 1930.0
High score: 2300
Low score: 1500
Score range: 800

$> python3 ft_score_analytics.py
=== Player Score Analytics ===
No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...

$> python3 ft_score_analytics.py ab ac
=== Player Score Analytics ===
Invalid parameter: 'ab'
Invalid parameter: 'ac'
No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...
'''
