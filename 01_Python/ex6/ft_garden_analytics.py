class Plant:
    growth_rate = 0.8

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age_days = age
        # instanciando a classe aninhada
        self.statistical_data = self.StatisticalData()

    def grow(self, value: float = growth_rate) -> None:
        self._height += value
        # chamando o get_grow_data da classe aninhada para contar as chamadas
        self.statistical_data.get_grow_data = 1

    def age(self, value: int = 1) -> None:
        self._age_days += value
        # chamando o get_age_data da classe aninhada para contar as chamadas
        self.statistical_data.get_age_data = 1

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
        # chamando o get_show_data da classe aninhada para contar as chamadas
        self.statistical_data.get_show_data = 1
        print(f"{self.name.capitalize()}: {round(self._height, 2) * 1.0}cm,"
              f" {self._age_days} days old")

    # método estático: pode ser chamado sem criar um objeto da classe
    # verifica se uma idade específica dada como parâmetro é maior que um ano
    @staticmethod
    def check_year_old(age_value: int) -> bool:
        if age_value >= 365:
            return True
        else:
            return False

    # método de classe: transforma o método em método de classe
    # cria uma planta "anônima" diretamente quando você ainda não tem todas
    # as informações
    @classmethod
    def plant_anonymous(cls, name: str = "Unknown plant", height: float = 0.0,
                        age: int = 0) -> 'Plant':
        return cls(name, height, age)

    # classe aninhada, que armazena dados estatísticos:
    # número de chamadas grow(),
    # número de chamadas age(),
    # número de chamadas show()
    class StatisticalData:
        def __init__(self) -> None:
            self._count_grow = 0
            self._count_age = 0
            self._count_show = 0
            self._count_shade = 0

        @property
        def get_grow_data(self) -> int:
            return self._count_grow

        @get_grow_data.setter
        def get_grow_data(self, value: int) -> None:
            self._count_grow += value

        @property
        def get_age_data(self) -> int:
            return self._count_age

        @get_age_data.setter
        def get_age_data(self, value: int) -> None:
            self._count_age += value

        @property
        def get_show_data(self) -> int:
            return self._count_show

        @get_show_data.setter
        def get_show_data(self, value: int) -> None:
            self._count_show += value

        @property
        def get_shade_data(self) -> int:
            return self._count_shade

        @get_shade_data.setter
        def get_shade_data(self, value: int) -> None:
            self._count_shade += value

        def show_data(self) -> str:
            return (f"Stats: {self.get_grow_data} grow, {self.get_age_data} "
                    f"age, {self.get_show_data} show")


class Flower(Plant):
    bloom_value = False

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        # instanciando a classe aninhada
        self.statistical_data = self.StatisticalData()

    def bloom(self) -> None:
        self.bloom_value = True

    def evolve(self, grow: float) -> None:
        print(f"[asking the {self.name} to grow and bloom]")
        self.grow(grow)
        self.bloom()

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
        # instanciando a classe aninhada
        self.statistical_data = self.StatisticalData()

    def produce_shade(self) -> None:
        self.statistical_data.get_shade_data = 1
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} now produces a shade of"
              f" {round(self._height, 1)}cm long and"
              f" {round(self.trunk_diameter, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round((self.trunk_diameter * 1.0), 1)}cm")


class Vegetable(Plant):
    nutritional_value = 0

    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def show_vegetable(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def age(self, day_value: int = 1) -> None:
        print(f"[make {self.name} grow and age for {day_value} days]")
        self._age_days += day_value
        self._height = self._height + (day_value * 2.1)
        self.nutritional_value += day_value

    def grow(self, value: float = 0) -> None:
        print(f"[make {self.name} grow and age for "
              f"{round(value / 2.1)} days]")
        self._height += value
        self._age_days = self._age_days + round(value / 2.1)
        self.nutritional_value += round(value / 2.1)


# Seed: armazena o número de sementes uma vez que a flor floresceu
class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.number_seeds = 0

    def get_seed(self, seed: int = 0) -> None:
        if self.bloom_value is True:
            self.number_seeds = seed

    def evolve_seed(self, grow: float, age: int, number_seeds: int) -> None:
        print(f"[make {self.name} grow, age and bloom]")
        self.grow(grow)
        self.age(age)
        self.bloom()
        self.number_seeds += number_seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.number_seeds}")


''''
funcao extra
'''


def show_statistics(plant: 'Plant') -> None:
    print(f"[statistics for {plant.name.capitalize()}]")
    print(plant.statistical_data.show_data())
    if plant.__class__.__name__ == "Tree":
        print(f"{plant.statistical_data.get_shade_data} shade")


'''
FUNCAO PRINCIPAL
'''


def ft_garden_analytics():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? ->", Plant.check_year_old(30))
    print("Is 400 days more than a year? ->", Plant.check_year_old(400))
    print()
    print("=== Flower")
    rose_plant = Flower("rose", 15.0, 10, "red")
    rose_plant.show()
    show_statistics(rose_plant)
    rose_plant.evolve(8)
    rose_plant.show()
    show_statistics(rose_plant)
    print()
    print("=== Tree")
    oak_plant = Tree("oak", 200.0, 365, 5.0)
    oak_plant.show()
    show_statistics(oak_plant)
    oak_plant.produce_shade()
    show_statistics(oak_plant)
    print()
    print("=== Seed")
    sunflower_plant = Seed("sunflower", 80, 45, "yellow")
    sunflower_plant.show()
    sunflower_plant.evolve_seed(30, 20, 42)
    sunflower_plant.show()
    show_statistics(sunflower_plant)
    print()
    print("=== Anonymous")
    pa = Plant.plant_anonymous()
    pa.show()
    show_statistics(pa)


if __name__ == "__main__":
    ft_garden_analytics()
