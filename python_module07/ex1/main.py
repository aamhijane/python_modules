from ex1.Deck import Deck, EmptyDeckError

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard



def main() -> None:
    print("=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    deck = Deck()
    creature_card = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    spell_card = SpellCard('Lightning Bolt', 4, 'Common', 'damage')
    artifact_card = ArtifactCard('Mana Crystal', 3, 'Common', 5, 'Permanent: +1 mana per turn')
    state = {'available_mana': 6}

    cards_list = [creature_card, spell_card, artifact_card]
    for card in cards_list:
        deck.add_card(card)

    print(f"Deck stats: {deck.get_deck_stats()}\n")

    print("Drawing and playing cards:\n")

    if not deck.cards:
        try:
            deck.draw_card()
        except EmptyDeckError as e:
            print(f"Game Error: {e}")
            return

    deck.shuffle()
    while True:
        try:
            drew = deck.draw_card()
            print(f"Drew: {drew.name} ({drew.type})")
            print(f"Play result: {drew.play(state)}\n")
        except EmptyDeckError as e:
            break

    print("Polymorphism in action: Same interface, different card behaviors!")
    

if __name__ == "__main__":
    main()
