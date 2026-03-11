from typing import Dict
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")

    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    target = CreatureCard("Goblin Warrior", 4, "Legendary", 6, 4)

    game_state: Dict[str, int] = {"available_mana": 6}

    print("CreatureCard Info:")
    print(creature.get_card_info())
    print()

    print("Playing Fire Dragon with 6 mana available:")
    print(f"Playable: {creature.is_playable(game_state['available_mana'])}")
    print(f"Play result: {creature.play(game_state['available_mana'])}")
    print()

    print("Fire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {creature.attack_target(target)}")
    print()

    print("Testing insufficient mana (3 available):")
    print(f"Playable: {creature.is_playable(3)}")
    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
