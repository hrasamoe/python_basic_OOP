#!/usr/bin/env python3
class SecurePlant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = height
        self._age: int = age
        print(
                f"Plant created: {self.name}: {self._height}cm,"
                f"{self._age} days old"
            )

    def get_height(self) -> float:
        return round(self._height, 1)

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {int(self.get_height())}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self.get_age()} days")

    def show(self) -> None:
        print(
                f"Current state: {self.name}: {self.get_height()}cm, "
                f"{self.get_age()} days old"
            )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 15.0, 10)
    print()
    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-25.0)
    rose.set_age(-30)
    print()
    rose.show()
