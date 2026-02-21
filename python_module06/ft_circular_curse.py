from alchemy.grimoire import validate_ingredients, record_spell

def main():
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    # Explicitly include the function name in the print string
    print(f'validate_ingredients("fire air"): {validate_ingredients("fire air")}')
    print(f'validate_ingredients("dragon scales"): {validate_ingredients("dragon scales")}\n')

    print("Testing spell recording with validation:")
    # Formatting to match 'record_spell("Name", "Ing"): Result'
    print(f'record_spell("Fireball", "fire air"): {record_spell("Fireball", "fire air")}')
    print(f'record_spell("Dark Magic", "shadow"): {record_spell("Dark Magic", "shadow")}\n')

    print("Testing late import technique:")
    print(f'record_spell("Lightning", "air"): {record_spell("Lightning", "air")}\n')

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")

if __name__ == "__main__":
    main()
