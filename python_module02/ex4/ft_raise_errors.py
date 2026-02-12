def check_plant_health(
        plant_name: str, water_level: int, sunlight_hours: int) -> None:
    """Check for plant health."""

    try:
        if not plant_name:
            raise ValueError("Plant name cannot be empty!")
        elif water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        elif water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        elif sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)")
        elif sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)")
        else:
            print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print(f"Error: {e}")


def test_plant_checks() -> None:
    """Testing plant with good/bad values."""

    print("Testing good values...")
    check_plant_health("tomato", 5, 8)

    print()

    print("Testing empty plant name...")
    check_plant_health("", 5, 8)

    print()

    print("Testing bad water level...")
    check_plant_health("tomato", 15, 8)

    print()

    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 5, 0)


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")

    print()

    test_plant_checks()

    print()

    print("All error raising tests completed!")
