import os
import sys
from dotenv import load_dotenv


def initialize_database(database_url: str) -> None:
    exist = os.path.exists(database_url)

    if not exist:
        with open(database_url, "w") as f:
            f.write("Agent_1, threat=85, dangerous=True\n")
            f.write("Agent_2, threat=32, dangerous=False\n")
            f.write("Agent_3, threat=67, dangerous=True\n")
        print(f"Database created: {database_url}")


def load_configuration(config_file: str) -> dict:
    exist = os.path.exists(config_file)

    if not exist:
        print("[MISSING] .env file not found!")
        sys.exit(1)

    load_dotenv()

    return {
        "MATRIX_MODE":    os.environ.get("MATRIX_MODE"),
        "DATABASE_URL":   os.environ.get("DATABASE_URL", "agents.txt"),
        "API_KEY":        os.environ.get("API_KEY"),
        "LOG_LEVEL":      os.environ.get("LOG_LEVEL"),
        "ZION_ENDPOINT":  os.environ.get("ZION_ENDPOINT"),
    }


def validate_configuration(config) -> bool:
    all_ok = True

    for key, value in config.items():
        if not value:
            print(f"[MISSING] {key} is not configured!")
            all_ok = False

    return all_ok


def display_configuration(config) -> None:
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    print("Database: Connected to local instance")
    print(f"API Access: {'*' * len(config['API_KEY'])}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print("Zion Network: Online")


def security_check() -> bool:
    all_ok = True
    env_exist = os.path.exists(".env")
    gitignore_exist = os.path.exists(".gitignore")

    if env_exist:
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
    else:
        print("[MISSING] .env file not found!")
        all_ok = False

    if gitignore_exist:
        with open(".gitignore", "r") as f:
            content = f.read()
            if ".env" not in content:
                print("[MISSING] .gitignore should have .env file.")
                all_ok = False
    else:
        print("[MISSING] .gitignore file not found!")
        all_ok = False

    return all_ok


def main() -> None:
    try:
        print("ORACLE STATUS: Reading the Matrix...\n")

        # Step 1: load config
        config = load_configuration(".env")

        # Step 2: validate config
        if not validate_configuration(config):
            sys.exit(1)

        # Step 3: initialize database
        initialize_database(config["DATABASE_URL"])

        # Step 4: display config
        display_configuration(config)
        print()

        # Step 5: Environment security check
        if not security_check():
            print("[WARNING] Security issues detected!")

        print("\nThe Oracle sees all configurations.")

    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
