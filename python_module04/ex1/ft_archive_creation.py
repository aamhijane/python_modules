from typing import List


def create_archive(data: List[str], path: str) -> None:
    """Establish a new storage unit and inscribe preservation data."""

    try:
        print(f"Initializing new storage unit: {path}")
        entry_id: int = 1
        with open(path, "w") as file:
            print("Storage unit created successfully...\n")

            print("Inscribing preservation data...")
            for entry in data:
                file.write(f"[ENTRY {entry_id:03d}] {entry}\n")
                print(f"[ENTRY {entry_id:03d}] {entry}")
                entry_id += 1

        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{path}' ready for long-term preservation.")
    except PermissionError:
        print("ERROR: Security protocols deny write access to this sector.")
    except OSError as e:
        print(f"ERROR: System anomaly detected during inscription: {e}")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    data: List[str] = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist trainee"
    ]
    path: str = "new_discovery.txt"
    create_archive(data, path)
