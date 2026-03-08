from ex0.CreatureCard import CreatureCard

def main() -> None:
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")

    print("CreatureCard Info:")
    # Setup
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin = CreatureCard("Goblin Warrior", 2, "Common", 2, 3)
    state = {'available_mana': 6}
    
    # Info
    print(f"{dragon.get_card_info()}\n")

    # Play
    print(f"Playing {dragon.name} with {state['available_mana']} mana available:")
    print(f"Playable: {dragon.is_playable(state['available_mana'])}")
    print(f"Play result: {dragon.play(state)}")
    
    # Attack
    print(f"\n{dragon.name} attacks {goblin.name}")
    print(f"Attack result: {dragon.attack_target(goblin)}")

    # Mana Inavailable
    state = {'available_mana': 3}
    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(state['available_mana'])}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
