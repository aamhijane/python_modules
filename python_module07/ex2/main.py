from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

    elite: EliteCard = EliteCard("Arcane Warrior", 4, "Legendary", 5, 3, 4)
    enemy: EliteCard = EliteCard("Enemy", 3, "Common", 3, 5, 2)

    print(f"Playing {elite.name} ({elite.type} Card):\n")

    print("Combat phase:")
    print(f"Attack result: {elite.attack(enemy)}")
    print(f"Defense result: {elite.defend(5)}\n")

    print("Magic phase:")
    print(f"Spell cast: {elite.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {elite.channel_mana(3)}\n")

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
