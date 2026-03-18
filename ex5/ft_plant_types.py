#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def get_info(self) -> None:
        print(
            f"\n{self.name} (Flower):"
            f"{self.height}cm, {self.age} days {self.color} color"
        )

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self, name: str, height: int, age: int, trunk_diameter: int
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_area = self.trunk_diameter * self.height // 320

    def get_info(self) -> None:
        print(
            f"\n{self.name} (Tree):"
            f"{self.height}cm, {self.age} days, "
            f"{self.trunk_diameter}cm diameter"
        )

    def produce_shade(self) -> None:
        print(f"{self.name} provides {self.shade_area} square meters of shade")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: int, age: int,
        harvest_season: str, nutritional_value: str
    ) -> None:
        super().__init__(name, height, age)
        self.nutritional_value = nutritional_value
        self.harvest_season = harvest_season

    def get_info(self) -> None:
        print(
            f"\n{self.name} (Vegetable): "
            f"{self.height}cm, {self.age} days, {self.harvest_season} harverst"
        )

    def nutrition(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 20, "red")
    Oak = Tree("Oak", 500, 1825, 50)
    Tomato = Vegetable("Tomato", 80, 90, "sunner", "Vitamin C")

    rose.get_info()
    rose.bloom()
    Oak.get_info()
    Oak.produce_shade()
    Tomato.get_info()
    Tomato.nutrition()
