import sys
import os
import site


def detect_virtual_env() -> tuple[bool, str | None, str | None]:
    """Detect if running inside a virtual environment."""
    venv_path = os.environ.get("VIRTUAL_ENV")
    if venv_path:
        venv_name = os.path.basename(venv_path)
        return True, venv_name, venv_path
    return False, None, None


def get_package_path() -> str:
    """Get the current environment's site-packages path."""
    try:
        packages = site.getsitepackages()
        return packages[0] if packages else "Unknown"
    except AttributeError:
        return site.getusersitepackages()


def display_outside_matrix(python_path: str) -> None:
    """Display info when not inside a virtual environment."""
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {python_path}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate    # On Windows\n")
    print("Then run this program again.")


def display_inside_matrix(
    python_path: str, venv_name: str, venv_path: str, package_path: str
) -> None:
    """Display info when inside a virtual environment."""
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {python_path}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")
    print("Package installation path:")
    print(f"{package_path}")


def main() -> None:
    """Main entry point for the construct program."""
    try:
        python_path = sys.executable
        is_venv, venv_name, venv_path = detect_virtual_env()
        package_path = get_package_path()

        if is_venv:
            display_inside_matrix(
                    python_path, venv_name, venv_path, package_path)
        else:
            display_outside_matrix(python_path)

    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
