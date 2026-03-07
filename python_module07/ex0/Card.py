from abc import ABC
from enum import Enum


class CardTypes(str, Enum):
    """
    String-based Enum for card types.
    """
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"
    ENCHANTMENT = "Enchantment"


class Card(ABC):
    """Card base blueprint."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Initialization of card variables."""
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    def play(self, game_state: dict) -> dict:
        print("PLAY")

    def get_card_info(self) -> dict:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        print(True)
