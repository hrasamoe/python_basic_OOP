#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.__height: float = height
        self.__age: int = age
        print(f"Plant created: {self.name}: {self.__height}cm,"
              "{self.__age} days old")

    def set_height(self, height: int) -> None:
        if height < 0:
            print(
                f"{self.name}: Error, height can't be negative"
            )
            print("Height update rejected")
        else:
            self.__height = height
            print(f"\nHeight updated: {round(self.__height, 1)}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days\n")

    def get_height(self) -> int:
        return round(self._height, 1)

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(
            f"\nCurrent plant: {self.name} "
            f"({round(self.__height, 1)}cm, {self.__age} days old)"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 15.0, 10)
    rose.set_height(25.0)
    rose.set_age(30)
    rose.set_height(-25)
    rose.set_age(-30)
    rose.show()
