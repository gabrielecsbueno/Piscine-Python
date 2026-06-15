def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()

    input_test = ["25", "abc"]

    for case in input_test:
        try:
            print(f"Input data is '{case}'")
            temp = input_temperature(case)
        except ValueError as err:
            print(f"Caught input_temperature error: {err}")
        else:
            print(f"Temperature is now {temp}°C")
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
