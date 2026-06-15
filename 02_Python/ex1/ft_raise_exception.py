class NumInvalido(Exception):
    # crio uma nova "excecao" na classe raiz Exception
    pass


def input_temperature(temp_str: str) -> int:
    value = int(temp_str)
    # Verificar se a temperatura é razoável para plantas (0 a 40 graus Celsius)
    # se for invalida lanca a excecao
    if value > 40:
        raise NumInvalido(f"{value}°C is too hot for plants (max 40°C)")
    elif value < 0:
        raise NumInvalido(f"{value}°C is too cold for plants (min 0°C)")
    else:
        # Retornar a temperatura se for válida
        return value


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()

    test = ["25", "abc", "100", "-50"]

    for case in test:
        try:
            print(f"Input data is '{case}'")
            temp = input_temperature(case)
        except Exception as err:
            print(f"Caught input_temperature error: {err}")
        else:
            print(f"Temperature is now {temp}°C")
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
