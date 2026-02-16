from typing import List


def crisis_response(filename: str) -> None:
    """Briefly describes the crisis management operation."""

    if filename == "standard_archive.txt":
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
    try:
        with open(filename, "r+") as file:
            content: str = file.read()
            if content == "":
                text: str = "Knowledge preserved for humanity"
                file.write(text)
                print(f"SUCCESS: Archive recovered - ``{text}''")
            else:
                print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"RESPONSE: {e}")
        print("STATUS: Crisis handled, Unknown error")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    files: List[str] = [
            "lost_archive.txt",
            "classified_vault.txt",
            "standard_archive.txt"
    ]

    for f in files:
        crisis_response(f)
        print()

    print("All crisis scenarios handled successfully. Archives secure.")
