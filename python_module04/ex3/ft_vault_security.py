from typing import List


def vault_security(source_path: str, dest_path: str, mode: str) -> None:
    """
    Function to handle both vaults
    is a master-level archivist move.
    """

    try:
        with open(source_path, "r") as source, open(dest_path, "a") as dest:
            content: str = source.read()
            dest.write(content)

            if mode == "EXTRACTION":
                print("SECURE EXTRACTION:")
                print(content)
            elif mode == "PRESERVATION":
                print("SECURE PRESERVATION:")
                print(content)
                print("Vault automatically sealed upon completion")
    except FileNotFoundError as e:
        print(f"Error {e.filename}: Not found.")
    except PermissionError as e:
        print(f"Error {e.filename}: Permission denied!")
    except OSError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    files: List[str] = [
        {"path": "classified_data.txt", "mode": "EXTRACTION"},
        {"path": "security_protocols.txt", "mode": "PRESERVATION"}
    ]
    dest_path: str = "security_report.txt"

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    for f in files:
        vault_security(f["path"], dest_path, f["mode"])
        print()

    print("All vault operations completed with maximum security.")
