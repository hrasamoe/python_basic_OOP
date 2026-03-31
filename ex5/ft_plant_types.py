#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: float) -> None:
        self._name: str = name
        self._age: float = age
        self._height: float = height

    def get_height(self) -> float:
        return round(self._height, 1)

    def get_age(self) -> int:
        return round(self._age)

    def grow(self, amount: float = 2.1) -> None:
        self._height += amount
        self._age += amount / 2.1

    def age_grow(self, days: int = 1) -> None:
        self._age += days
        self._height += 2.1 * days
        print(f"[make {self._name} grow and age for {days} days]")

    def show(self) -> None:
        print(f"{self._name}: {self.get_height()}cm, "
              f"{self.get_age()} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age: float, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.bloomed: bool = False

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        status = ("is blooming beautifully!" if self.bloomed
                  else "has not bloomed yet")
        print(f" {self._name} {status}")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade of "
              f"{self.get_height()}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: float, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def grow(self, amount: float = 2.1) -> None:
        super().grow(amount)
        self.nutritional_value += int(amount / 2.1)

    def age_grow(self, days: int = 1) -> None:
        super().age_grow(days)
        self.nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower ===")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print('\n=== Tree ===')
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    print('\n=== Vegetable ===')
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    tomato.age_grow(20)
    tomato.show()
