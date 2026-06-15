class Plant:
    # instancia: valor de crescimento da planta
    growth_rate = 0.8

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    # metodo: aumenta a altura da planta
    def grow(self) -> None:
        self.height += self.growth_rate

    # metodo: aumenta a idade da planta
    def age(self) -> None:
        self.age_days += 1

    def show(self) -> str:
        return (f"{self.name}: {round(self.height, 1)}cm, {self.age_days}"
                " days old")


def ft_plant_growth():
    plants = [
        Plant("Rose", 25.0, 30)
    ]
    days = 1
    print("=== Garden Plant Growth ===")
    for plant in plants:
        print(plant.show())
        plant.grow()
        plant.age()
    for _ in range(7):
        for plant in plants:
            print(f"=== Day {days} ===")
            print(plant.show())
            plant.grow()
            plant.age()
            days += 1
    growth = round(7 * Plant.growth_rate, 1)
    print(f"Growth this week: {growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
