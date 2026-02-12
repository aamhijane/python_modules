class GardenError(Exception):
    """Base class for all garden related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for problems specific to plants."""
    pass


class WaterError(GardenError):
    """Exception raised for problems specific to watering."""
    pass


class SunlightError(GardenError):
    """Exception raised for problems specific to sunlight."""
    pass


class GardenManager:
    """The garden management system."""

    def __init__(self):
        """Initialize plants list."""
        self.plants: list = []
        self.tank: int = 2

    def add_plant(self, plant_name: str) -> None:
        """Adding new plant to the list."""
        try:
            if not plant_name:
                raise PlantError("adding plant: Plant name cannot be empty!")
            self.plants.append(plant_name)
            print(f"Added {plant_name} successfully")
        except PlantError as e:
            print(f"Error {e}")

    def water_plants(self) -> None:
        """Watering plants system."""
        try:
            print("Opening watering system")
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant_health(plant_name: str, water: int, sun: int) -> None:
        """Check for plant health."""
        try:
            if water > 10:
                raise WaterError(
                    f"Water level {water} is too high (max 10)")
            elif water < 1:
                raise WaterError(
                    f"Water level {water} is too low (min 1)")
            elif sun > 12:
                raise SunlightError(
                        f"Sunlight hours {sun} is too high (max 12)")
            elif sun < 2:
                raise SunlightError(
                        f"Sunlight hours {sun} is too low (min 2)")
            print(f"{plant_name}: healthy (water: {water}, sun: {sun})")
        except (WaterError, SunlightError) as e:
            print(f"Error checking lettuce: {e}")


def test_garden_management() -> None:
    """Testing garden management system."""

    alice: object = GardenManager()

    print("Adding plants to garden...")
    alice.add_plant("tomato")
    alice.add_plant("lettuce")
    alice.add_plant("")

    print()

    print("Watering plants...")
    alice.water_plants()

    print()

    print("Checking plant health...")
    water_levels = [5, 15]
    sunlight_hours = [8, 6]
    for n, w, s in zip(alice.plants, water_levels, sunlight_hours):
        alice.check_plant_health(n, w, s)

    print()

    print("Testing error recovery...")
    try:
        if alice.tank < 5:
            raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        alice.tank = 10
        print("System recovered and continuing...")


if __name__ == "__main__":
    print("=== Garden Management System ===")

    print()

    test_garden_management()

    print()

    print("Garden management system test complete!")
