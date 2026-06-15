"""
Precisa de classes de exceção personalizadas simples:
• GardenError - Um erro básico para problemas de jardim
• PlantError - Para problemas com plantas (herda de GardenError)
• WaterError - Para problemas com rega (herda de GardenError)
Cada exceção personalizada deve:
• Ser uma classe simples que herda de Exception (ou GardenError)
• Ter uma mensage de erro padrão específica (ex.: "Unknown plant error") se
  nenhuma for fornecida
"""


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
Precisa de funções que:
• Lançam seus erros personalizados em diferentes situações
• Mostram como capturar seus tipos de erro específicos
• Demonstram que capturar GardenError captura todos os erros relacionados ao
  jardim
"""


def mensage_error(mensage: str, type_error: str = "GardenError"):
    if type_error == "PlantError":
        raise PlantError(mensage)
    elif type_error == "WaterError":
        raise WaterError(mensage)
    else:
        raise GardenError(mensage)


def ft_custom_errors():
    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    try:
        mensage_error("The tomato plant is wilting!", "PlantError")
    except PlantError as err:
        print(f"Caught PlantError: {err}")
    print()

    print("Testing WaterError...")
    try:
        mensage_error("Not enough water in the tank!", "WaterError")
    except WaterError as err:
        print(f"Caught WaterError: {err}")
    print()

    print("Testing catching all garden errors...")
    try:
        mensage_error("The tomato plant is wilting!", "PlantError")
    except GardenError as err:
        print(f"Caught GardenError: {err}")
    try:
        mensage_error("Not enough water in the tank!", "WaterError")
    except GardenError as err:
        print(f"Caught GardenError: {err}")

    print()
    print("All custom error types work correctly!")


"""
python3 ft_custom_errors.py
=== Custom Garden Errors Demo ===

Testing PlantError...
Caught PlantError: The tomato plant is wilting!

Testing WaterError...
Caught WaterError: Not enough water in the tank!

Testing catching all garden errors...
Caught GardenError: The tomato plant is wilting!
Caught GardenError: Not enough water in the tank!

All custom error types work correctly!
"""

"""
Quando criar erros próprios: quando os built-ins do Python (ValueError,
TypeError, etc.) não descrevem bem o domínio do problema. Erros customizados
tornam o código mais expressivo e facilitam a depuração, pois o nome da
exceção já comunica o contexto do erro.

Como a herança organiza erros: permite capturar em diferentes granularidades.
`except PlantError` trata apenas erros de plantas; `except GardenError`
captura todos os erros do jardim (PlantError e WaterError) sem precisar
listar cada subtipo, seguindo o princípio de substituição de Liskov.
"""

if __name__ == "__main__":
    ft_custom_errors()
