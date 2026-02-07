#!/usr/bin/env python3

class Plant:
    """Blueprint for creating plant objects with their attributes."""

    def __init__(self, name: str, height: int = 0, plant_age: int = 0) -> None:
        """Initialize a plant with name, height (cm), and age (days)."""
        self.name: str = name
        self.height: int = height
        self.plant_age: int = plant_age
        self.weekly_growth: int = 0 

    def grow(self, days: int) -> None:
        """Make the plant grow by 1cm."""
        growth: int = days * 1
        self.height += growth
        self.weekly_growth = growth
        
    def age(self, days: int) -> None:
        """Age the plant by 1 day."""
        self.plant_age += days

    def get_info(self) -> None:
        """Prints the current status of the plant."""
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")

if __name__ == "__main__":
    plant: object = Plant("Rose", 25, 30)

    # Day 1
    print("=== Day 1 ===")
    plant.get_info()

    # Simulate 6 more days passing (Total 7 days)
    days_passed: int = 6
    plant.grow(days_passed)
    plant.age(days_passed)

    # Day 7
    print("=== Day 7 ===")
    plant.get_info()
    print(f"Growth this week: +{plant.weekly_growth}cm")
