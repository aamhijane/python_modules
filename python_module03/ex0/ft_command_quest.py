import sys


class NoArgumentsError(Exception):
    pass


if __name__ == "__main__":
    print("=== Command Quest ===")

    try:
        if len(sys.argv) == 1:
            raise NoArgumentsError("No arguments provided!")
    except NoArgumentsError as e:
        print(f"{e}")
    finally:
        print(f"Program name: {sys.argv[0]}")
        if len(sys.argv) > 1:
            print(f"Arguments received: {len(sys.argv) - 1}")
            i = 1
            while i < len(sys.argv):
                print(f"Argument {i}: {sys.argv[i]}")
                i = i + 1
        print(f"Total arguments: {len(sys.argv)}")
