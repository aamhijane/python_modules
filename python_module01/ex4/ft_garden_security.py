#!/usr/bin/env python3

class   SecurePlant:
    """Protecting important data from direct access."""

    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
        """Initialize private instance variables"""
        self.__name: str = name
        self.__height: int = 0 
        self.__age: int = 0

    def error(self, key: str, value: int) -> None:
        """Throw error is height or age inputs are invalid."""

        unit: str = "cm"
        if key == "age":
            unit = " days"
        print(f"Invalid operation attempted: {key} {value}{unit} [REJECTED]")
        print(f"Security: Negative {key} rejected")

    def get_name(self) -> str:
        """Get name."""
        return self.__name

    def get_height(self) -> int:
        """Get height."""
        return self.__height

    def get_age(self) -> int:
        """Get age."""
        return self.__age

    def set_height(self, new_height: int) -> None:
        """Updated height with validation."""
        if  new_height >= 0:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            self.error("height", new_height)

    def set_age(self, new_age: int) -> None:
        """Update age with validation"""
        if  new_age >= 0:
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            self.error("age", new_age)

if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant: object = SecurePlant("Rose")
    print(f"Plant created: {plant.get_name()}")
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    print()
    print(f"Current plant: {plant.get_name()} ({plant.get_height()}cm, {plant.get_age()} days)")
