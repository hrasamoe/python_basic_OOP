#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.age = age
        self.height = height

    def grow(self, amount=2.1) -> None:
        self.height += amount
        self.age += amount / 2.1

    def age_grow(self, days=1):
        self.age += days
        self.height += 2.1 * days
        print(f"[make {self.name} grow and age for {days} days]")

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        print(f"[asking the {self.name} to bloom]")
        self.bloomed = True

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self.height, 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide.")

    def show(self):
        super().show()
        print(f" Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, amount=2.1):
        super().grow(amount)
        self.nutritional_value += int(amount / 2.1)

    def age_grow(self, days=1):
        super().age_grow(days)
        self.nutritional_value += days

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    tomato.age_grow(20)
    tomato.show()
