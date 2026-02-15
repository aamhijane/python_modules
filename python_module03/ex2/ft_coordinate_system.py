import sys
import math


class NoArgumentError(Exception):
    """Custom exception: no argument provided"""
    pass


class InvalidArgumentError(Exception):
    """Custom exception: invalid argument input"""
    pass


class InvalidArgumentsLenError(Exception):
    """Custom exception: invalid arguments length."""
    pass


class CoordinateSystem:
    """Build a 3D coordinate system."""

    def __init__(self) -> None:
        """Initialize coordinates."""
        self.init_coords: tuple = (0, 0, 0)
        self.coords: tuple = ()

    def distance(self) -> float:
        """Calculate distance."""
        x1, y1, z1 = self.init_coords
        x2, y2, z2 = self.coords
        return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

    def create_position(self) -> None:
        """
        Porpuse of this function is to parse/validate
        user coordinates and create position.
        """

        raw_args: list = sys.argv[1:]
        if not raw_args or not raw_args[0]:
            raise NoArgumentError(
                    "No coordinates provided. "
                    f"Usage ./{sys.argv[0]} <x> <y> <z>")
        tmp: list = []
        arg_val: any = ""
        try:
            for c in raw_args:
                split_arg: list = c.split(',')
                for sa in split_arg:
                    arg_val = sa
                    tmp.append(int(sa))
            self.coords = tuple(tmp)
            if len(self.coords) != 3:
                raise InvalidArgumentsLenError(
                        "Please provide 3 coordinates (x, y, z).")
        except ValueError as e:
            arg: str = ', '.join(sys.argv[1:])
            print(f'Parsing invalid coordinates: "{arg}"')
            print(f"Error parsing coordinates: {e}")
            print(f'Error details - Type: {type(e).__name__}, Args: {e.args}')
            raise InvalidArgumentError(
                    f"I typed ’{arg_val}’ instead of ’123’") from None

    def unpacking_demonstration(self) -> None:
        """Unpacking demonstration."""
        print("Unpacking demonstration:")
        x, y, z = self.coords
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()

    player: object = CoordinateSystem()

    try:
        player.create_position()
        print(f"Position created: {player.coords}")

        distance: float = player.distance()
        print(
            f"Distance between {player.init_coords} "
            f"and {player.coords}: {distance:.2f}\n")

        player.unpacking_demonstration()

    except (
            NoArgumentError,
            InvalidArgumentError,
            InvalidArgumentsLenError) as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f'Parsing invalid coordinates: "{e.value}"')
        print(f"Error parsing coordinates: {e}")
        print(f'Error details - Type: {type(e).__name__}, Args: {e.args}')
