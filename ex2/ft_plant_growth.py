#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, day: int) -> None:
        self.name: str = name
        self.height: float = height
        self.day: int = day
        self.initial_height: float = height

    def grow(self, amount: float = 0.8) -> None:
        self.height += amount

    def age(self) -> None:
        self.day += 1

    def get_info(self) -> str:
        return (
            f"{self.name}: {round(self.height, 2)}cm, {self.day} days old"
        )

    def weekly_growth(self) -> float:
        return round(self.height - self.initial_height)


if __name__ == "__main__":
    plants: list[Plant] = [
        Plant("Rose", 25.0, 30)
    ]
    print("=== Garden Plant Growth ===")
    print("=== Day 1 ===")
    for plant in plants:
        print(f"{plant.get_info()}")
    for day in range(2, 9):
        for plant in plants:
            plant.grow()
            plant.age()
        print(f"=== Day {day} ===")
        for plant in plants:
            print(plant.get_info())
    for plant in plants:
        print(f"Growth this week: {plant.weekly_growth()}cm")
