from typing import List
import random

from ex0.Card import Card


class EmptyDeckError(Exception):
    """Exception raised when attempting to draw from an empty deck."""
    def __init__(self, message="Cannot draw from an empty deck"):
        self.message = message
        super().__init__(self.message)


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """
        Removes and returns the top card from the deck.
        """
        if len(self.cards) == 0:
            raise EmptyDeckError("The deck is out of cards!")
            
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        # Guard against empty list (Resilient Design)
        if not self.cards:
            return {'total_cards': 0, 'avg_cost': 0.0}

        # Initialize fixed keys first
        summary = {'total_cards': 0}
        total_cost = 0
        
        for card in self.cards:
            # Direct access - assumes data structure is Hardened and keys exist
            c_type = card.type.lower()
            c_cost = card.cost
            
            # Update global metrics
            summary['total_cards'] += 1
            total_cost += c_cost
            
            # Dynamic category logic without .get()
            category_key = f"{c_type}s"
            if category_key in summary:
                summary[category_key] += 1
            else:
                summary[category_key] = 1

        # Calculate average cost
        summary['avg_cost'] = round(total_cost / summary['total_cards'], 2)
        
        return summary
