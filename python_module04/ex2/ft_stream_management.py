import sys


def manage_streams() -> None:
    """Access the three sacred data channels of the Archives."""

    archivist_id: str = input(
            "Input Stream active. Enter archivist ID: ")
    archivist_status: str = input(
            "Input Stream active. Enter status report: ")

    print()

    print(f"[STANDARD] Archive status from {archivist_id}: "
          f"{archivist_status}", file=sys.stdout)
    print("[ALERT] System diagnostic: Communication "
          "channels verified", file=sys.stderr)
    print(
        "[STANDARD] Data transmission complete\n", file=sys.stdout)

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    manage_streams()
