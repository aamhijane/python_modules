def recover_ancient_data(vault_path: str) -> None:
    """Recover ancient data."""

    try:
        print("Accessing Storage Vault: ancient_fragment.txt")
        print("Connection established...\n")

        print("RECOVERED DATA:")
        with open(vault_path, "r") as file:
            content: str = file.read()
            print(content)

        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    recover_ancient_data("ancient_fragment.txt")
