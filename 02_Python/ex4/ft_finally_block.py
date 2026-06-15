class GardenError(Exception):
    def __init__(self, mensage: str = "Unknown garden error"):
        super().__init__(mensage)


class PlantError(GardenError):
    def __init__(self, mensage: str = "Unknown plant error"):
        super().__init__(mensage)


class WaterError(GardenError):
    def __init__(self, mensage: str = "Unknown water error"):
        super().__init__(mensage)


"""
Escreva uma função water_plant(plant_name) que:
• Tenta regar a planta
• Tem sucesso se o nome da planta estiver capitalizado
• Lança um erro se o nome da planta não estiver capitalizado (use sua exceção
  PlantError do exercício anterior)
• Imprime uma mensage em caso de sucesso
"""


def water_plant(plant_name):
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


"""
Crie uma função test_watering_system() que:
• Abre o sistema de irrigação (apenas imprima uma mensage)
• Rega várias plantas usando water_plant()
• Usa a estrutura try/except/finally
• Trata erros se o nome de uma planta for inválido e não puder ser regada.
  Nesse caso, pare o teste e retorne imediatamente ao main.
• Sempre fecha o sistema de irrigação em um bloco finally
• Mostra que a limpeza sempre acontece, mesmo quando há um erro
"""


def test_watering_system(name: list):
    print("Opening watering system")
    try:
        for count in name:
            water_plant(count)
    except PlantError as err:
        print(f"Caught PlantError: {err}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


def ft_finally_block():
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    plants1 = [
        "Tomato",
        "Lettuce",
        "Carrots"
    ]
    test_watering_system(plants1)
    print()
    print("Testing invalid plants...")
    plants2 = [
        "Tomato",
        "lettuce",
        "carrots"
    ]
    test_watering_system(plants2)
    print()
    print("Cleanup always happens, even with errors!")


"""
DICAS:
Por que é importante limpar recursos mesmo quando erros acontecem? Como o
bloco finally ajuda a garantir que a limpeza sempre ocorra?
"""
if __name__ == "__main__":
    ft_finally_block()
"""
Quando Python executa um arquivo, ele define uma variável especial __name__:

Se o arquivo foi executado diretamente (python3 ft_finally_block.py), __name__
vale "__main__"
Se o arquivo foi importado por outro módulo (import ft_finally_block), __name__
vale o nome do módulo ("ft_finally_block")
Significa: "só execute ft_finally_block() se este arquivo for o ponto de
entrada do programa".
"""
