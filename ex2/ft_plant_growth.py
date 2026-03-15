#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age
        self.initial_height: int = height

    def grow(self, amount: int = 1) -> None:
        self.height += amount

    def grow_age_by_day(self) -> None:
        self.age += 1

    def get_info(self) -> str:
        return (
            f"{self.name}: {self.height}cm, {self.age} days old"
        )

    def weekly_growth(self) -> int:
        return self.height - self.initial_height


if __name__ == "__main__":
    plants: list[Plant] = [
        Plant("Rose", 25, 30)
    ]
    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())
    for day in range(1, 7):
        for plant in plants:
            plant.grow(amount=1)
            plant.grow_age_by_day()
    print("=== Day 7 ===")
    for plant in plants:
        print(plant.get_info())
        print(f"Growth this week: +{plant.weekly_growth()}cm")
