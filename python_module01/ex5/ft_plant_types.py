#!/usr/bin/env python3

class   Plant():
    """A base class representing a generic plant in the garden."""

    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
        """Initializes a new Plant instance with name, height, and age."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

class   Flower(Plant):
    """A specialized Plant that can bloom and has a specific color."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initializes a Flower with specific color characteristics."""
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """Prints a message indicating the flower is blooming beautifully."""
        print(f"{self.name} is blooming beautifully!")


class   Tree(Plant):
    """A specialized Plant that grows large and provides shade based on its trunk size."""

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        """Initializes a Tree with trunk diameter measurements."""
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        """
        Calculates and prints the shade area provided by the tree.
        The formula uses a scale factor of 1.56 based on trunk diameter.
        """
        shade_area: int = (self.trunk_diameter * 156) // 100
        print(f"{self.name} provides {shade_area} square meters of shade")


class   Vegetable(Plant):
    """A specialized Plant grown for food, defined by its harvest time and nutrition."""

    def __init__(self, name: str, height: int, age: int, harvest_season: str, nutritional_value: str) -> None:
        """Initializes a Vegetable with harvest and nutritional data."""
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()

    flowers: list = [
        Flower("Rose", 25, 30, "red"),
        Flower("Lilly", 18, 24, "yellow")
    ]
    for flower in flowers:
        print(f"{flower.name} (Flower): {flower.height}cm, {flower.age} days, {flower.color} color")
        flower.bloom()

    print()

    trees: list = [
        Tree("Oak", 500, 1825, 50),
        Tree("Olive", 420, 1564, 37)
    ]
    for tree in trees:
        print(f"{tree.name} (Tree): {tree.height}cm, {tree.age} days, {tree.trunk_diameter}cm diameter")
        tree.produce_shade()

    print()

    vegetables: list = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 58, "summer", "vitamin A")
    ]
    for vegetable in vegetables:
        print(f"{vegetable.name} (Vegetable): {vegetable.height}cm, {vegetable.age} days, {vegetable.harvest_season} harvest")
        print(f"{vegetable.name} is rich in {vegetable.nutritional_value}")
