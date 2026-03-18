#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.__height: int = 0
        self.__age: int = 0
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height < 0:
            print(
                f"\nInvalid operation attempted: height {height}cm [REJECTED]"
            )
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_info(self) -> None:
        print(
            f"\nCurrent plant: {self.name} "
            f"({self.__height}cm, {self.__age} days)"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    rose.set_height(-5)
    rose.get_info()
