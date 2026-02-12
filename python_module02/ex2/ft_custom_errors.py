class GardenError(Exception):
    """Base class for all garden related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for problems specific to plants."""
    pass


class WaterError(GardenError):
    """Exception raised for problems specific to watering."""
    pass


def check_plant_health(is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def check_water_level(liters: int) -> None:
    if liters < 5:
        raise WaterError("Not enough water in the tank!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    try:
        check_plant_health(True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print()
    print("Testing WaterError...")
    try:
        check_water_level(2)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print()
    print("Testing catching all garden errors...")
    for test_func, arg in [(check_plant_health, True), (check_water_level, 2)]:
        try:
            test_func(arg)
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
