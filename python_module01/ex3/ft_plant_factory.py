#!/usr/bin/env python3

class Plant:
    """Blueprint for creating plant objects with their attributes."""

    def __init__(self, name: str, starting_height: int = 0, starting_age: int = 0) -> None:
        """Initialize a plant with name, starting starting_height (cm), and starting starting_age (days)."""
        self.name: str = name
        self.starting_height: int = starting_height
        self.starting_age: int = starting_age

    def __str__(self) -> str:
        """Return a formatted string representation of the plant."""
        return f"{self.name} ({self.starting_height}cm, {self.starting_age} days)"


def create_plants(data: list) -> None:
    """Factory function to create multiple plants efficiently."""

    plants: list = [Plant(**props) for props in data]
    for plant in plants:
        print(f"Created: {plant}")
    print()
    print(f"Total plants created: {len(plants)}")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants_data: list = [
        { 'name': 'Rose', 'starting_height': 25, 'starting_age': 30 },
        { 'name': 'Oak', 'starting_height': 200, 'starting_age': 365 },
        { 'name': 'Cactus', 'starting_height': 5, 'starting_age': 90 },
        { 'name': 'Sunflower', 'starting_height': 80, 'starting_age': 45 },
        { 'name': 'Fern', 'starting_height': 15, 'starting_age': 120 },
    ]
    create_plants(plants_data)
