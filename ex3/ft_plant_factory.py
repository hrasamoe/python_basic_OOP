#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, starting_height: float, starting_age: int) -> None:
        self.name: str = name
        self.height: float = round(starting_height,1)
        self.age: int = starting_age

    def grow(self) -> str:
        self.height += 0.8
        self.age += 1

    def show(self) -> str:
        return (
            f"{self.name} ({self.height}cm, {self.age} days)"
        )


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants: list[Plant] = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]

    for plant in plants:
        print(f"Created: {plant.show()}")
