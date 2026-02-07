#!/usr/bin/env python3

class   Plant:
    """Represents a basic plant in the garden."""

    def __init__(self, name: str, height: int) -> None:
        """Initializes a new plant."""
        self.name: str = name
        self.height: int = height
        self.category: str = "regular"

    def grow(self, amount: int) -> None:
        """Increases the height of the plant and prints the growth."""
        self.height += amount
        print(f"{self.name} grew {amount}cm")


class   FloweringPlant(Plant):
    """Represents a plant that can produce flowers."""

    def __init__(self, name: str, height: int, color: str) -> None:
        """Initializes a flowering plant with a specific flower color."""
        super().__init__(name, height)
        self.color: str = color
        self.category: str = "flowering"
        self.is_blooming: bool = True

    def get_info(self) -> str:
        """Returns a string description of the flowering plant's status."""
        status: str = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"


class   PrizeFlower(FloweringPlant):
    """Represents a special flowering plant that awards prize points."""

    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        """Initializes a prize flower with points for a score boost."""
        super().__init__(name, height, color)
        self.category: str = "prize"
        self.prize: int = prize

    def get_info(self) -> str:
        """Extends information to include prize points."""
        return f"{super().get_info()}, Prize points: {self.prize}"


class   GardenManager:
    """Manages a collection of plants and provides analytics."""
    total_gardens: int = 0

    def __init__(self, owner_name: str) -> None:
        """Initializes the manager with an owner and an empty plant list."""
        self.owner_name: str = owner_name
        self.plants: list = []
        self.total_growth: int = 0
        GardenManager.total_gardens += 1

    def add_plant(self, plant: object) -> None:
        """Adds a plant to the list."""
        self.plants = self.plants + [plant]
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_all(self, amount: int) -> None:
        """Triggers the grow method for all plants in the garden."""
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)
            self.total_growth += amount

    class GardenStats:
        """Nested class for calculating garden performance metrics."""

        @staticmethod
        def calculate_score(plants: list) -> int:
            """Calculates total score based on height and prize multipliers."""
            score: int = 0
            for plant in plants:
                score += plant.height
                if plant.category == "prize":
                    multiplier: int = 4
                    score += (plant.prize * multiplier)
            return score

        @staticmethod
        def count_categories(plants: list) -> tuple:
            """Counts the number of each plant type in the list."""
            reg: int = 0
            flow: int = 0
            prz: int = 0
            for plant in plants:
                category: str = plant.category
                if category == "regular": reg += 1
                elif category == "flowering": flow += 1
                elif category == "prize": prz += 1
            return reg, flow, prz

    @classmethod
    def create_garden_network(cls, names_list: list) -> list:
        """Factory method to create a list of GardenManager instances."""
        networks: list = []
        for name in names_list:
            networks = networks + [cls(name)]
        return networks

    @staticmethod
    def validate_height(height: int) -> bool:
        """Validates if a plant height is a positive integer."""
        return height > 0

    def print_report(self) -> None:
        """Prints a full summary of the garden status."""
        print(f"=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if plant.category == "regular":
                print(f"- {plant.name}: {plant.height}cm")
            else:
                print(f"- {plant.get_info()}")
        print()
        tcount: tuple = self.GardenStats.count_categories(self.plants)
        plants_added: int = len(self.plants)
        print(f"Plants added: {plants_added}, Total growth: {self.total_growth}cm")
        print(f"Plant types: {tcount[0]} regular, {tcount[1]} flowering, {tcount[2]} prize flowers")
        print()
        valid: bool = False
        if len(self.plants) > 0:
            valid = self.validate_height(self.plants[0].height)
        print(f"Height validation test: {valid}")


if  __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    print()

    gardens: list = GardenManager.create_garden_network(["Alice", "Bob"])
    alice = gardens[0]
    bob = gardens[1]

    # Adding plants to Alice's garden
    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    # Adding plant to Bob's garden to reach 92 score.
    bob.plants += [Plant("Small Pine", 92)]

    print()

    # Grow all plants
    alice.grow_all(1)

    print()

    # Alice's garden report
    alice.print_report()
    alice_score = alice.GardenStats.calculate_score(alice.plants)
    bob_score = alice.GardenStats.calculate_score(bob.plants)
    print(f"Garden scores - {alice.owner_name}: {alice_score}, {bob.owner_name}: {bob_score}")
    print(f"Total gardens managed: {len(gardens)}")
