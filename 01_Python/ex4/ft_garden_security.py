class Plant:
    growth_rate = 0.8

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age_days = age

    def grow(self, value: float = growth_rate) -> None:
        self._height += value

    def age(self, value: int = 1) -> None:
        self._age_days += value

    # Getter: retorna o valor atual da altura da planta
    @property
    def get_height(self) -> float:
        return self._height

    # Setter: atualiza a altura somente se o valor for positivo
    @get_height.setter
    def get_height(self, value: float) -> None:
        if value > 0:
            self._height = value
            print(f"Height updated: {self._height}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    # Getter: retorna o valor atual da idade da planta em dias
    @property
    def get_age(self) -> int:
        return self._age_days

    # Setter: atualiza a idade somente se o valor for positivo
    @get_age.setter
    def get_age(self, value: int) -> None:
        if value > 0:
            self._age_days = value
            print(f"Age updated: {self._age_days} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def show(self) -> str:
        return (f"{self.name}: {round(self._height, 2) * 1.0}cm,"
                f" {self._age_days} days old")


def ft_garden_security():
    plants = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("Plant created:", plants.show())
    print()
    plants.get_height = 25
    plants.get_age = 30
    print()
    plants.get_height = -5
    plants.get_age = -1
    print()
    print("Current state:", plants.show())


if __name__ == "__main__":
    ft_garden_security()
