#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    """Takes a string input from the user and handle exceptions."""

    try:
        temp: int = int(temp_str)
        if temp < 0:
            raise ValueError(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            raise ValueError(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
        print(f"Temperature {temp}°C is perfect for plants!")
        return temp
    except ValueError as err:
        if "invalid literal" in f"{err}":
            print(f"Error: '{temp_str}' is not a valid number")
        else:
            print(f"{err}")


def test_temperature_input() -> None:
    test_inputs: list = ["25", "abc", "100", "-50"]
    for inp in test_inputs:
        print(f"Testing temperature: {inp}")
        check_temperature(inp)
        print()


if  __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    
    test_temperature_input()

    print("All tests completed - program didn't crash!")
