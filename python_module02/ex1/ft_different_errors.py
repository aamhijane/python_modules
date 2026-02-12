def garden_operations(test_value: str) -> None:
    """
    Simulates various garden-related failures
    to trigger specific exceptions.
    """
    if test_value == "value":
        int("not_number")
    elif test_value == "zero":
        10 / 0
    elif test_value == "file":
        open("missing.txt", "r")
    elif test_value == "key":
        person = {}
        print(person["_plant"])


def test_error_types() -> None:
    """
    Executes a series of tests to demonstrate
    catching specific Python errors.
    """

    print("=== Garden Error Types Demo ===")

    print()
    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print()
    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print()
    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print()
    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")

    print()
    print("Testing multiple errors together...")
    try:
        garden_operations("value")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
