def water_plants(plant_list: list) -> None:
    """Watering system with plant name validation."""

    print("Opening watering system")
    try:
        for plant in plant_list:
            if not isinstance(plant, str):
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Test watering system by passing invalid plant name."""

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")

    print()

    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])

    print()

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")

    print()

    test_watering_system()
