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

    @property
    def get_height(self) -> float:
        return self._height

    @get_height.setter
    def get_height(self, value: float) -> None:
        if value > 0:
            self._height = value
            print(f"Height updated: {self._height}cm")
        else:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")

    @property
    def get_age(self) -> int:
        return self._age_days

    @get_age.setter
    def get_age(self, value: int) -> None:
        if value > 0:
            self._age_days = value
            print(f"Age updated: {self._age_days} days")
        else:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {round(self._height, 2) * 1.0}cm,"
              f" {self._age_days} days old")


class Flower(Plant):
    bloom_value = False

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        self.bloom_value = True
        print(f"[asking the {self.name} to bloom]")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloom_value is False:
            print(f"{self.name.capitalize()} has not bloomed yet")
        else:
            print(f"{self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} now produces a shade of"
              f" {round(self._height, 1)}cm long and"
              f" {round(self.trunk_diameter, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    nutritional_value = 0

    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def age(self, day_value: int = 0) -> None:
        print(f"[make {self.name} grow and age for {day_value} days]")
        self._age_days += day_value
        self._height = self._height + (day_value * 2.1)
        self.nutritional_value += day_value

    def grow(self, height_value: float = 0) -> None:
        print(f"[make {self.name} grow and age for "
              f"{round(height_value / 2.1)} days]")
        self._height += height_value
        self._age_days = self._age_days + round(height_value / 2.1)
        self.nutritional_value += round(height_value / 2.1)


def ft_plant_types():
    plants = [
        Flower("rose", 15, 10, "red"),
        Tree("oak", 200.0, 365, 5.0),
        Vegetable("tomato", 5.0, 10, "April"),
    ]
    print("=== Garden Plant Types ===")
    for plant in plants:
        if plant.__class__.__name__ == "Flower":
            print("=== Flower")
            plant.show()
            plant.bloom()
            plant.show()
        elif plant.__class__.__name__ == "Tree":
            print("=== Tree")
            plant.show()
            plant.produce_shade()
        elif plant.__class__.__name__ == "Vegetable":
            print("=== Vegetable")
            plant.show()
            plant.age(20)
            plant.show()
        print()


if __name__ == "__main__":
    ft_plant_types()
