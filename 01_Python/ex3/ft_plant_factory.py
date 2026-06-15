class Plant:
    growth_rate = 0.8

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> str:
        return (f"{self.name}: {round(self.height, 2)}cm, {self.age_days}"
                " days old")


def ft_plant_factory():
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
    for plant in plants:
        print("Created:", plant.show())


if __name__ == "__main__":
    ft_plant_factory()
