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
        return f"{self.name}: {round(self.height, 1)}cm, {self.day} days old"

    def weekly_growth(self) -> int:
        return round(self.height - self.initial_height)


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    print("=== Day 1 ===")
    print(rose.get_info())
    for day in range(2, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {day} ===")
        print(rose.get_info())
    print(f"Growth this week: {rose.weekly_growth()}cm")
