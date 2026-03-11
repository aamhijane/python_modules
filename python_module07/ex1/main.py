from enum import Enum

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard

from ex1.Deck import Deck


class EffectTypes(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")

    # Cards
    creature: Card = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    spell: Card = SpellCard(
        'Lightning Bolt', 4, 'Common', "3 " + EffectTypes.DAMAGE.value)
    artifact: Card = ArtifactCard(
        'Mana Crystal', 2, 'Common', 5, 'Permanent: +1 mana per turn')

    # Available mana
    game_state = {"available_mana": 6}

    # 1. Create a deck
    deck: Deck = Deck()

    # 2. Add a CreatureCard, SpellCard, and ArtifactCard
    deck.add_card(creature)
    deck.add_card(spell)
    deck.add_card(artifact)

    # 3. Print get_deck_stats()
    print("Building deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}\n")

    # 4. Shuffle cards
    deck.shuffle()

    # 5. Draw each card and call play() on it
    print("Drawing and playing cards:\n")

    while deck.cards:
        drew: Card = deck.draw_card()
        print(f"Drew: {drew.name} ({drew.type})")
        print(f"Play result: {drew.play(game_state)}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
