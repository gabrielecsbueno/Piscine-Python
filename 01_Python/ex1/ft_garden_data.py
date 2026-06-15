class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> str:
        return (f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data():
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(plant.show())


if __name__ == "__main__":
    ft_garden_data()
