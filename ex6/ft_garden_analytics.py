#!/usr/bin/env python3

class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def inc_grow(self) -> None:
            self._grow_calls += 1

        def inc_age(self) -> None:
            self._age_calls += 1

        def inc_show(self) -> None:
            self._show_calls += 1

    def __init__(self, name: str, height: float, days: int) -> None:
        self._name: str = name
        self._days: int = days
        self._height: float = height
        self._stats: Plant._Stats = Plant._Stats()

    def get_height(self) -> float:
        return round(self._height, 1)

    def get_days(self) -> int:
        return self._days

    def grow(self, amount: float = 2.1) -> None:
        self._height += amount
        self._stats.inc_grow()

    def age(self, amount: int = 1) -> None:
        self._days += amount
        self._stats.inc_age()

    def show(self) -> None:
        self._stats.inc_show()
        print(f"{self._name}: {self.get_height()}cm, "
              f"{self.get_days()} days old")

    def display_stat(self) -> None:
        print(f"Stats: {self._stats._grow_calls} grow, "
              f"{self._stats._age_calls} age, "
              f"{self._stats._show_calls} show")

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls) -> 'Plant':
        return cls("Unknown plant", 0.0, 0)


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 days: int, trunk_diameter: float) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter: float = trunk_diameter
        self._shade_calls: int = 0

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade of "
              f"{self.get_height()}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self.trunk_diameter, 1)}cm")

    def display_stat(self) -> None:
        super().display_stat()
        print(f" {self._shade_calls} shade")


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 days: int, color: str) -> None:
        super().__init__(name, height, days)
        self.color: str = color
        self.bloomed: bool = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        status = ("is blooming beautifully!" if self.bloomed
                  else "has not bloomed yet")
        print(f" {self._name} {status}")


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 days: int, color: str) -> None:
        super().__init__(name, height, days, color)
        self.seeds: int = 0

    def grow(self, amount: float = 2.1) -> None:
        super().grow(amount)

    def age(self, amount: int = 1) -> None:
        super().age(amount)

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


def display_plant_stat(plant_obj: Plant) -> None:
    print(f"[Statistics for {plant_obj._name}]")
    plant_obj.display_stat()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print('=== Check year-old ')
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print('\n=== Flower')
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stat(rose)
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_plant_stat(rose)
    print('\n=== Tree')
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stat(oak)
    oak.produce_shade()
    display_plant_stat(oak)
    print('\n=== Seed')
    sun = Seed("Sunflower", 80.0, 45, "yellow")
    sun.show()
    print(" [make sunflower grow, age and bloom]")
    sun.grow(30.0)
    sun.age(20)
    sun.bloom()
    sun.show()
    display_plant_stat(sun)
    print('\n=== Anonymous')
    anon = Plant.anonymous()
    anon.show()
    display_plant_stat(anon)