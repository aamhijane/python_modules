import random
from enum import Enum
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class FantasyCardFactory(CardFactory):

    CREATURES = {
        "dragon": ("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5),
        "goblin": ("Goblin Warrior", 2, Rarity.COMMON.value, 2, 1),
    }
    SPELLS = {
        "fireball": ("Lightning Bolt", 3, Rarity.RARE.value, "damage"),
    }
    ARTIFACTS = {
        "mana_ring": (
            "Mana Crystal", 2, Rarity.UNCOMMON.value, 3, "+1 mana per turn"),
    }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        key = name_or_power if isinstance(name_or_power, str) else None
        if key and key in self.CREATURES:
            args = self.CREATURES[key]
        else:
            args = random.choice(list(self.CREATURES.values()))
        return CreatureCard(*args)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        key = name_or_power if isinstance(name_or_power, str) else None
        if key and key in self.SPELLS:
            args = self.SPELLS[key]
        else:
            args = random.choice(list(self.SPELLS.values()))
        return SpellCard(*args)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        key = name_or_power if isinstance(name_or_power, str) else None
        if key and key in self.ARTIFACTS:
            args = self.ARTIFACTS[key]
        else:
            args = random.choice(list(self.ARTIFACTS.values()))
        return ArtifactCard(*args)

    def create_themed_deck(self, size: int) -> dict:
        deck = {"creatures": [], "spells": [], "artifacts": []}
        creators = [
            self.create_creature,
            self.create_spell,
            self.create_artifact
        ]
        keys = ["creatures", "spells", "artifacts"]
        for i in range(size):
            creator = creators[i % 3]
            key = keys[i % 3]
            deck[key].append(creator())
        return deck

    def get_supported_types(self) -> dict:
        return {
            "creatures": list(self.CREATURES.keys()),
            "spells": list(self.SPELLS.keys()),
            "artifacts": list(self.ARTIFACTS.keys()),
        }
