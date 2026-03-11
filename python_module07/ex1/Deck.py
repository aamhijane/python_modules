from typing import List, Dict
from ex0.Card import Card
import random


class Deck:

    def __init__(self):
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
        if self.cards:
            random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            return self.cards.pop()

    def get_deck_stats(self) -> dict:
        deck_stats: Dict[str, int | float] = {}

        total_cost: int = 0
        total_cards: int = len(self.cards)
        deck_stats["total_cards"] = total_cards

        for card in self.cards:
            total_cost += card.cost
            card_type: str = card.type.lower() + "s"
            if card_type in deck_stats:
                deck_stats[card_type] += 1
            else:
                deck_stats[card_type] = 1

        avg_cost: int | float = round(total_cost / total_cards)
        deck_stats["avg_cost"] = round(avg_cost, 1) if total_cards > 0 else 0

        return deck_stats
