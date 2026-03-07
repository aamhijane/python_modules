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
    print(dragon.get_card_info())
    print()

    # Play
    print(f"Playing Fire Dragon with {state['available_mana']} mana available:")
    is_playable = state['available_mana'] >= dragon.cost
    print(f"Playable: {is_playable}")
    print(f"Play result: {dragon.play(state)}")
    
    # Attack
    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {dragon.attack_target(goblin)}")

    state = {'available_mana': 3}
    print("\nTesting insufficient mana (3 available):")
    is_playable = state['available_mana'] >= dragon.cost
    print(f"Playable: {is_playable}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
