#!/usr/bin/env python3

class Plant:
    """Blueprint for creating plant objects with their attributes."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant with name, height (cm), and age (days)."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def __str__(self) -> str:
        """Return a formatted string representation of the plant."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    rose: object = Plant("Rose", 25, 30)
    sunflower: object = Plant("Sunflower", 80, 45)
    cactus: object = Plant("Cactus", 15, 120)

    plants: list = [rose, sunflower, cactus]
    for plant in plants:
        print(plant)
